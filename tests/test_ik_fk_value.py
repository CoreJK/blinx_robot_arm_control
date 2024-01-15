import sys
sys.path.append("..")
import unittest
from math import radians, degrees
from spatialmath import SE3
from common.blinx_robot_module import Mirobot
import numpy as np
from pprint import pprint

class TestMirobot(unittest.TestCase):
    def setUp(self):
        self.robot = Mirobot()
        self.joint_angle_range = self.generate_angle_range()
        
    def generate_joint_angles(self, num_joints, angle_range, step_size):
        joint_angles = []
        for i in range(num_joints):
            angles = np.arange(angle_range[i][0], angle_range[i][1] + step_size, step_size)
            angles = np.round(angles, 2)  # Round to two decimal places
            joint_angles.append(angles)
        return joint_angles

    # Example usage:
    def generate_angle_range(self):
        num_joints = 6
        angle_range = [[-165, 165], [-90, 90], [-60, 60], [-150, 170], [-30, 210], [-90, 180]]
        step_size = 0.1
        joint_angles = self.generate_joint_angles(num_joints, angle_range, step_size)
        return joint_angles
    
    def test_joint_range(self):
        pprint(list(self.joint_angle_range[0]))
    
    
    
        

if __name__ == '__main__':
    unittest.main()