import numpy as np
from queue import PriorityQueue

from PySide6.QtCore import QThread, Signal
from common.blinx_robot_module import Mirobot
from common import settings


class UpdateJointAnglesThread(QThread):
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
    
            
