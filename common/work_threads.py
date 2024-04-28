import json
import shelve
from queue import PriorityQueue, Queue
import time

import numpy as np
from loguru import logger
from retrying import retry
from PySide6.QtCore import QRunnable, Signal, QObject

from common import settings
from common.blinx_robot_module import Mirobot
from common.socket_client import ClientSocket


class SingalEmitter(QObject):
    """用于 QRunnable 线程发送信号的类"""
    joint_angles_update_signal = Signal(list)
    arm_endfactor_positions_update_signal = Signal(list)
    joint_sync_move_time_update_signal = Signal(float)
    command_signal = Signal(str)


class UpdateJointAnglesTask(QRunnable):
    """更新上位机发送的关节角度数据的线程"""
    
    def __init__(self, joints_angle_queue: Queue):
        super().__init__()
        self.blinx_robot_arm = Mirobot(settings.ROBOT_MODEL_CONFIG_FILE_PATH, param_type='MDH')
        self.joints_angle_queue = joints_angle_queue
        self.singal_emitter = SingalEmitter()
        self.is_on = True
    
    @logger.catch
    def run(self):
        while self.is_on:
            time.sleep(0.1)
            if not self.joints_angle_queue.empty():
                angle_data_list = self.joints_angle_queue.get()
                # 关节角度更新信号
                self.singal_emitter.joint_angles_update_signal.emit(angle_data_list)
                
                # 末端坐标与位姿更新信号
                arm_joint_radians = np.radians(angle_data_list)
                translation_vector = self.blinx_robot_arm.fkine(arm_joint_radians)
                X, Y, Z = translation_vector.t  # 末端坐标
                R_x, P_y, Y_z = translation_vector.rpy(unit='deg', order='zyx')  # 末端姿态
                self.singal_emitter.arm_endfactor_positions_update_signal.emit([X, Y, Z, R_x, P_y, Y_z])
            

class UpdateDelayTimeTask(QRunnable):
    """更新上位机控制机械臂运动到目标位置所需的时间"""
    
    def __init__(self, joints_sync_move_time_queue: Queue):
        super().__init__()
        self.joints_sync_move_time_queue = joints_sync_move_time_queue
        self.singal_emitter = SingalEmitter()    
        self.is_on = True
    
    @logger.catch
    def run(self):
        while self.is_on:
            time.sleep(0.1)
            if not self.joints_sync_move_time_queue.empty():
                joint_sync_move_time = self.joints_sync_move_time_queue.get()
                self.singal_emitter.joint_sync_move_time_update_signal.emit(round(joint_sync_move_time, 3))
            
            
class AgnleDegreeWatchTask(QRunnable):
    """获取关节角度值的线程"""
    
    def __init__(self):
        super().__init__()
        self.is_on = True
        self.singal_emitter = SingalEmitter()
    
    @logger.catch        
    def run(self):
        while self.is_on:
            time.sleep(0.1)
            command = json.dumps({"command": "get_joint_angle_all"}).replace(' ',"") + '\r\n'
            self.singal_emitter.command_signal.emit(command)        
            
                
class CommandSenderTask(QRunnable):
    """发送命令的线程"""
    
    def __init__(self, command_queue: PriorityQueue, joints_angle_queue: Queue, joints_sync_move_time_queue: Queue):
        super().__init__()
        self.command_queue = command_queue
        self.joints_angle_queue = joints_angle_queue
        self.joints_sync_move_time_queue = joints_sync_move_time_queue
        self.is_on = True
    
    @logger.catch
    def run(self):
        with self.get_robot_arm_connector() as conn:
            while self.is_on:
                time.sleep(0.1)
                if not self.command_queue.empty():
                    try:
                        command_str = self.command_queue.get()
                        
                        # 发送命令
                        conn.send(command_str[1])
                        
                        # 接收命令返回的信息
                        original_response_str = conn.recv(1024).decode('utf-8')  # 原始的字符串返回的信息，可用于 Debug
                        # 验证返回的字符串是否完整 '\r\n', 不完整不发送
                        if original_response_str.endswith('\r\n'):
                            response = json.loads(original_response_str)
                        
                            # todo 需要抽象成处理不同命令返回的类
                            # 不同命令返回的信息, 放入不同的队列
                            if response["return"] == "get_joint_angle_all":
                                # 解析机械臂角度获取返回的信息
                                angle_data_list = response['data']
                                self.joints_angle_queue.put(angle_data_list)
                            
                            elif response["return"] == "set_joint_angle_all_time":
                                # 解析机械臂协同运动到目标位置所需耗时的信息
                                if response['data'] != False:
                                    joint_sync_move_time = response['data']
                                    self.joints_sync_move_time_queue.put(joint_sync_move_time)
                                    logger.debug(f"运动到目标位置预计耗时: {joint_sync_move_time} s")
                                else:
                                    logger.warning("机械臂无法运动到目标位置!")
                            
                    except Exception as e:
                        logger.error(f"解析命令处理异常: {e}")
                        logger.error(rf"异常命令: {original_response_str}")
                
                    
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
    
            
            
    