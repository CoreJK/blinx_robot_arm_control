import json
import shelve
from queue import PriorityQueue

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
    
    def __init__(self, command_respose_queue: PriorityQueue):
        super().__init__()
        self.blinx_robot_arm = Mirobot(settings.ROBOT_MODEL_CONFIG_FILE_PATH)
        self.command_respose_queue = command_respose_queue
        self.is_on = True
        
    def run(self):
        while self.is_on:
            if not self.command_respose_queue.empty():
                angle_data_list = self.command_respose_queue.get()
                # 关节角度更新信号
                self.joint_angles_update_signal.emit(angle_data_list)
                
                # 末端坐标与位姿更新信号
                arm_joint_radians = np.radians(angle_data_list[1])
                translation_vector = self.blinx_robot_arm.fkine(arm_joint_radians)
                X, Y, Z = translation_vector.t  # 末端坐标
                rz, ry, rx = translation_vector.rpy(unit='deg')  # 末端姿态
                self.arm_endfactor_positions_update_signal.emit([X, Y, Z, rz, ry, rx])
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
    
    
    def __init__(self, command_queue: PriorityQueue, command_respose_queue: PriorityQueue):
        super().__init__()
        self.command_queue = command_queue
        self.command_res_queue = command_respose_queue
        self.is_on = True
        
    def run(self):
        with self.get_robot_arm_connector() as conn:
            while self.is_on:
                if not self.command_queue.empty():
                    try:
                        command_str = self.command_queue.get()
                        
                        # 发送命令
                        conn.send(command_str[1])
                        logger.debug(f"发送命令：{command_str[1].decode().strip()}")
                        
                        # 接收命令返回的信息
                        response = json.loads(conn.recv(1024).decode('utf-8').strip())
                        logger.debug(f"返回信息: {response}")
                        
                        # todo 命令返回的信息放入另外一个队列
                        # 解析机械臂角度获取返回的信息
                        if response["return"] == "get_joint_angle_all":
                            angle_data_list = response['data']
                            self.command_res_queue.put((1, angle_data_list))
                            
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
            
            
    