import json
import sys
import shelve
from queue import PriorityQueue, Queue

import numpy as np
from loguru import logger
from retrying import retry
from PySide6.QtCore import QThread, Signal

from common import settings
from common.blinx_robot_module import Mirobot
from common.socket_client import ClientSocket


class UpdateJointAnglesTask(QThread):
    """更新上位机发送的关节角度数据的线程"""
    joint_angles_update_signal = Signal(list)
    arm_endfactor_positions_update_signal = Signal(list)
    
    def __init__(self, joints_angle_queue: Queue):
        super().__init__()
        self.blinx_robot_arm = Mirobot(settings.ROBOT_MODEL_CONFIG_FILE_PATH)
        self.joints_angle_queue = joints_angle_queue
        self.is_on = True
        
    def run(self):
        while self.is_on:
            if not self.joints_angle_queue.empty():
                angle_data_list = self.joints_angle_queue.get()
                # 关节角度更新信号
                self.joint_angles_update_signal.emit(angle_data_list)
                
                # 末端坐标与位姿更新信号
                arm_joint_radians = np.radians(angle_data_list)
                translation_vector = self.blinx_robot_arm.fkine(arm_joint_radians)
                X, Y, Z = translation_vector.t  # 末端坐标
                R_x, P_y, Y_z = translation_vector.rpy(unit='deg', order='zyx')  # 末端姿态
                self.arm_endfactor_positions_update_signal.emit([X, Y, Z, R_x, P_y, Y_z])
            self.sleep(0.1)
    
            
class AgnleDegreeWatchTask(QThread):
    """获取关节角度值的线程"""
    command_signal = Signal(str)
    
    def __init__(self):
        super().__init__()
        self.is_on = True
        
    def run(self):
        while self.is_on:
            command = json.dumps({"command": "get_joint_angle_all"}).replace(' ',"") + '\r\n'
            self.command_signal.emit(command)        
            self.sleep(0.5)
                
                
class CommandSenderTask(QThread):
    """发送命令的线程"""
    
    
    def __init__(self, command_queue: PriorityQueue, joints_angle_queue: Queue, joints_sync_move_time_queue: Queue):
        super().__init__()
        self.command_queue = command_queue
        self.joints_angle_queue = joints_angle_queue
        self.joints_sync_move_time_queue = joints_sync_move_time_queue
        self.is_on = True
        
    def run(self):
        with self.get_robot_arm_connector() as conn:
            while self.is_on:
                if not self.command_queue.empty():
                    try:
                        command_str = self.command_queue.get()
                        
                        # 发送命令
                        conn.send(command_str[1])
                        
                        # 接收命令返回的信息
                        response = json.loads(conn.recv(1024).decode('utf-8').strip())
                        
                        # todo 需要抽象成处理不同命令返回的类
                        # 不同命令返回的信息, 放入不同的队列
                        if response["return"] == "get_joint_angle_all":
                            # 解析机械臂角度获取返回的信息
                            angle_data_list = response['data']
                            self.joints_angle_queue.put(angle_data_list)
                        elif response["return"] == "set_joint_angle":
                            joint_move_time = response['data']
                            # todo 获取单个 joint 运动到目标位置所需的时间
                            logger.debug(f"单个 joint 运动到目标位置预计耗时: {joint_move_time} s")
                        elif response["return"] == "set_joint_angle_all_time":
                            # 解析机械臂协同运动到目标位置所需耗时的信息
                            if response['data'] != False:
                                joint_sync_move_time = response['data']
                                self.joints_sync_move_time_queue.put(joint_sync_move_time)
                                logger.debug(f"运动到目标位置预计耗时: {joint_sync_move_time} s")
                            else:
                                logger.warning("机械臂无法运动到目标位置!")
                            
                    except Exception as e:
                        logger.warning(f"命令处理异常: {e}")
                        continue
                    self.sleep(0.2)
                    
    @retry(stop_max_attempt_number=3, wait_fixed=1000)
    @logger.catch
    def get_robot_arm_connector(self):
        """获取与机械臂的连接对象"""
        try:
            socket_info = shelve.open(str(settings.IP_PORT_INFO_FILE_PATH))
            host = socket_info['target_ip']
            port = int(socket_info['target_port'])
            robot_arm_client = ClientSocket(host, port)
            socket_info.close()
        except Exception as e:
            logger.error(str(e))
        return robot_arm_client
    

class ActionTableTask(QThread):
    """执行表格任务的线程"""
    def __init__(self, table_object, select_row, command_queue: PriorityQueue):
        super().__init__()
        self.is_on = True
        self.table_object = table_object
        self.select_row = select_row
        self.command_queue = command_queue
        
    def run(self):
        angle_1 = float(self.table_object.item(self.select_row, 0).text())
        angle_2 = float(self.table_object.item(self.select_row, 1).text())
        angle_3 = float(self.table_object.item(self.select_row, 2).text())
        angle_4 = float(self.table_object.item(self.select_row, 3).text())
        angle_5 = float(self.table_object.item(self.select_row, 4).text())
        angle_6 = float(self.table_object.item(self.select_row, 5).text())
        speed_percentage = float(self.table_object.item(self.select_row, 6).text())
        type_of_tool = self.table_object.cellWidget(self.select_row, 7).currentText()
        tool_switch = self.table_object.cellWidget(self.select_row, 8).currentText()
        delay_time = float(self.table_object.item(self.select_row, 9).text())  # 执行动作需要的时间
        
        # 机械臂执行命令
        json_command = {"command": "set_joint_angle_all_time",
                                "data": [angle_1, angle_2, angle_3, angle_4, angle_5, angle_6, 0,
                                        speed_percentage]}
        str_command = json.dumps(json_command).replace(' ', "") + '\r\n'
        self.command_queue.put((2, str_command.encode()))
        
        # 末端工具动作
        logger.info("单次执行，开关控制")
        if type_of_tool == "吸盘":
            tool_status = True if tool_switch == "开" else False
            json_command = {"command":"set_robot_io_interface", "data": [0, tool_status]}
            str_command = json.dumps(json_command).replace(' ', "") + '\r\n'
            self.command_queue.put((1, str_command.encode()))
                    
        return delay_time
            
            
    