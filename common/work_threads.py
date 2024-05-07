import json
import shelve
from queue import PriorityQueue, Queue
import time

import numpy as np
from loguru import logger
from retrying import retry
from pubsub import pub
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
            pub.subscribe(self.check_flag, 'thread_work_flag')
            if not self.joints_angle_queue.empty():
                angle_data_list = self.joints_angle_queue.get()
                # 关节角度更新信号
                self.singal_emitter.joint_angles_update_signal.emit(list(np.round(angle_data_list, 3)))
                
                # 末端坐标与位姿更新信号
                arm_joint_radians = np.radians(angle_data_list)  # 正逆解需要弧度制
                translation_vector = self.blinx_robot_arm.fkine(arm_joint_radians)
                X, Y, Z = translation_vector.t  # 末端坐标
                R_x, P_y, Y_z = translation_vector.rpy(unit='deg', order='zyx')  # 末端姿态
                self.singal_emitter.arm_endfactor_positions_update_signal.emit(list(np.round([X, Y, Z, R_x, P_y, Y_z], 3)))
            

    def check_flag(self, flag=True):
        self.is_on = flag
            
            
class AgnleDegreeWatchTask(QRunnable):
    """获取关节角度值的线程"""
    
    def __init__(self, joints_angle_queue: Queue):
        super().__init__()
        self.is_on = True
        self.joints_angle_queue = joints_angle_queue        
    
    @logger.catch        
    def run(self):
        with self.get_robot_arm_connector() as coon:
            while self.is_on:
                time.sleep(0.1)
                pub.subscribe(self.check_flag, 'thread_work_flag')
                try:
                    response_str = coon.recv(1024).decode('utf-8')
                    if response_str.startswith('{') and response_str.endswith('\r\n'):
                        # 命令缓冲区
                        recv_buffer = list(filter(lambda s: s and s.strip(), response_str.split('\r\n')))
                        for recv in recv_buffer:
                            joints_angle = json.loads(recv)
                            if joints_angle['return'] == 'get_joint_angle_all':
                                joints_angle_list = joints_angle['data']
                                self.joints_angle_queue.put(joints_angle_list)
                except Exception as e:
                    logger.error(f"解析命令处理异常: {e}")
                    logger.error(rf"异常命令: {response_str}")
                            
    def check_flag(self, flag=True):
        self.is_on = flag
    
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

    
class CommandSenderTask(QRunnable):
    """发送命令的线程"""
    
    def __init__(self, command_queue: PriorityQueue):
        super().__init__()
        self.command_queue = command_queue
        self.is_on = True
    
    @logger.catch
    def run(self):
        with self.get_robot_arm_connector() as conn:
            while self.is_on:
                pub.subscribe(self.check_flag, 'thread_work_flag')  # 检查线程是否需要继续运行
                time.sleep(0.1)
                if not self.command_queue.empty():
                    try:
                        # 发送命令
                        command_str = self.command_queue.get()
                        conn.sendall(command_str[1])
                        
                        # 接收命令返回的信息
                        original_response_str = conn.recv(1024).decode('utf-8')  # 原始的字符串返回的信息，可用于 Debug
                        # 验证返回的字符串是否完整 '\r\n', 不完整不发送
                        if original_response_str.startswith('{') and original_response_str.endswith('\r\n'):
                            # todo 添加缓冲区
                            recv_buffer = list(filter(lambda s: s and s.strip(), original_response_str.split('\r\n')))
                            for recv in recv_buffer:
                                response = json.loads(recv)
                                # todo 需要抽象成处理不同命令返回的类
                                # 不同命令返回的信息, 放入不同的队列
                                if response["return"] == "set_joint_angle_all_time" and response["data"] == "delay":
                                    logger.warning("机械臂运动中, 请等待...")
                                if response["return"] == "move_in_place" and response["data"] == "true":
                                    logger.warning("机械臂已到达目标位置!")
                                    
                    except Exception as e:
                        logger.error(f"解析命令处理异常: {e}")
                        logger.error(rf"异常命令: {original_response_str}")
                
    def check_flag(self, flag=True):
        self.is_on = flag
                    
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
    