from decimal import Decimal
import socket
import simplejson as json
import shelve
from queue import Queue
import time

import numpy as np
from loguru import logger
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
        self.update_joint_angles_thread_flag = True
    
    @logger.catch
    def run(self):
        while self.update_joint_angles_thread_flag:
            time.sleep(0.1)
            pub.subscribe(self.check_update_joint_angles_thread_flag, 'update_joint_angles_thread_flag')
            if not self.joints_angle_queue.empty():
                angle_data_list = self.joints_angle_queue.get()
                # 关节角度更新信号
                self.singal_emitter.joint_angles_update_signal.emit(list(map(self.decimal_round_for_joints, angle_data_list)))
                
                # 末端坐标与位姿更新信号
                arm_joint_radians = np.radians(angle_data_list)  # 正逆解需要弧度制
                translation_vector = self.blinx_robot_arm.fkine(arm_joint_radians)
                X, Y, Z = map(self.decimal_round_for_positions, translation_vector.t)  # 末端坐标
                R_x, P_y, Y_z = map(self.decimal_round_for_joints, translation_vector.rpy(unit='deg', order='zyx'))  # 末端姿态
                self.singal_emitter.arm_endfactor_positions_update_signal.emit([X, Y, Z, R_x, P_y, Y_z])
    
    def decimal_round_for_joints(self, joints_angle: float) -> Decimal:
        """用精确的方式四舍五入, 保留关节角度的三位小数"""
        joints_angle_str = str(joints_angle)
        joints_angle_decimal = Decimal(joints_angle_str).quantize(Decimal("0.001"), rounding="ROUND_HALF_UP")
        return joints_angle_decimal
    
    def decimal_round_for_positions(self, value: float) -> Decimal:
        """用精确的方式四舍五入, 保留末端坐标和姿态的三位小数"""
        value = Decimal(str(value)) * Decimal('1000')
        value_decimal = value.quantize(Decimal("0.001"), rounding="ROUND_HALF_UP")
        return value_decimal

    def check_update_joint_angles_thread_flag(self, flag=True):
        self.update_joint_angles_thread_flag = flag
            

class AgnleDegreeWatchTask(QRunnable):
    """订阅关节角度值的线程"""
    
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
                    response_str = coon.recv(2048).decode('utf-8')
                    if response_str.startswith('{') and response_str.endswith('\r\n'):
                        recv_buffer = self.split_by_symbol(response_str)  # 命令缓冲区
                        recv_joint_angle_datas = list(filter(self.keep_joint_datas_str, recv_buffer))  # 保留关节角度值
                        for recv in recv_joint_angle_datas:
                            
                            try:
                                joints_angle = json.loads(recv)
                            except json.JSONDecodeError as e:
                                logger.exception(f"解析命令处理异常: {e}")
                                logger.error(rf"异常命令: {recv}")
                                
                            joints_angle_list = joints_angle['data']
                            self.joints_angle_queue.put(joints_angle_list)
                    else:
                        logger.warning(f"数据不完整: {response_str}")
                except socket.timeout:
                    self.is_on = False        
                    logger.error("机械臂连接超时！")
                
    def split_by_symbol(self, response_str: str, split_symbol='\r\n') -> list:
        """根据指定的分隔符拆分字符串, 并清理空字符串"""
        recv_buffer = list(filter(lambda s: s and s.strip(), response_str.split(split_symbol)))
        return recv_buffer
    
    def keep_joint_datas_str(self, json_str: str):
        """保留关节角度值"""
        if 'get_joint_angle_all' in json_str:
            return True
        else:
            return False
    
    def check_flag(self, flag=True):
        self.is_on = flag
    
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
            logger.exception(str(e))
        return robot_arm_client

    
class CommandSenderTask(QRunnable):
    """发送命令的线程"""
    
    def __init__(self, command_queue: Queue):
        super().__init__()
        self.command_queue = command_queue
        self.is_on = True
    
    @logger.catch
    def run(self):
        while self.is_on:
            pub.subscribe(self.check_flag, 'thread_work_flag')  # 检查线程是否需要继续运行
            time.sleep(0.1)
            if not self.command_queue.empty():
                try:
                    # 发送命令
                    command_str = self.command_queue.get()
                    with self.get_robot_arm_connector() as conn:
                        conn.sendall(command_str)
                        logger.debug(f"命令发送线程，发送的命令: {command_str}")
                                
                except Exception as e:
                    logger.error(f"命令发送异常: {e}")
                    logger.error(rf"异常命令: {command_str.decode('utf-8')}")
                    
    def check_flag(self, flag=True):
        self.is_on = flag
                    
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
    

class CommandReceiverTask(QRunnable):
    """命令接收与分流(发布)线程"""
    
    def __init__(self):
        super().__init__()
        self.is_on = True
        
    @logger.catch
    def run(self):
        """接收命令并发布对应的响应数据"""
        with self.get_robot_arm_connector() as conn:
            while self.is_on:
                pub.subscribe(self.check_flag, 'thread_work_flag')
                time.sleep(0.1)
                try:
                    response_str = conn.recv(2048).decode('utf-8')
                    if response_str.startswith('{') and response_str.endswith('\r\n'):
                        # 命令缓冲区
                        recv_buffer = self.split_by_symbol(response_str, split_symbol='\r\n')
                        # TODO: 分流命令, 需要做并发处理
                        self.get_joints_move_status(recv_buffer)
                    else:
                        logger.warning(f"数据不完整: {response_str}")

                except Exception as e:
                    logger.error(f"解析命令处理异常: {e}")
                    logger.error(rf"异常命令: {recv_buffer}")

    def split_by_symbol(self, response_str: str, split_symbol='\r\n') -> list:
        """根据指定的分隔符拆分字符串"""
        recv_buffer = list(filter(lambda s: s and s.strip(), response_str.split(split_symbol)))
        return recv_buffer

    def get_joints_move_status(self, recv_buffer: list):
        """获取并发布机械臂运动状态"""
        # 剔除不需要的命令
        recv_arm_move_status = list(filter(self.get_arm_move_state, recv_buffer))
        try:
            for move_status in recv_arm_move_status:
                json_data = json.loads(move_status)
                if json_data['data'] == 'true':
                    logger.warning(f"机械臂运动状态: {json_data}")
                    pub.sendMessage('joints/move_status', move_status=True)
                else:
                    logger.warning(f"机械臂运动状态: {json_data}")
                    pub.sendMessage('joints/move_status', move_status=False)
        except Exception as e:
            logger.error(f"解析命令处理异常: {e}")
            logger.error(rf"异常命令: {move_status}")
    
    def get_arm_move_state(self, json_str):
        """获取机械臂运动到位状态"""
        if'move_in_place' in json_str:
            return True
        else:
            return False
        
    def check_flag(self, flag=True):
        """线程工作控制位"""
        self.is_on = flag
        
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
            logger.exception(str(e))
        return robot_arm_client