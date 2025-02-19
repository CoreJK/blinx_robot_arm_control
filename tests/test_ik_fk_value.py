import sys
sys.path.append("..")
import unittest
from common.blinx_robot_module import Mirobot
import numpy as np
import pandas as pd


class TestMirobot(unittest.TestCase):
    def setUp(self):
        self.robot = Mirobot()
        self.joint_angle_datas = self.generate_joint_angles_data()
        
    def generate_joint_angles(self, num_joints, angle_range, step_size):
        joint_angles = []
        for i in range(num_joints):
            angles = np.arange(angle_range[i][0], angle_range[i][1] + step_size, step_size)
            angles = np.round(angles, 2)  # 角度值保留两位小数的精度
            joint_angles.append(angles)
        return joint_angles

    
    def generate_joint_angles_data(self):
        num_joints = 6
        angle_range = [[0, 140], [0, 70], [0, 45], [0, 150], [0, 10], [0, 180]]
        step_size = 0.1
        joint_angles = self.generate_joint_angles(num_joints, angle_range, step_size)
        return joint_angles

    # 通过角度计算末端位姿集合
    def test_xyz(self):
        #  将角度集合转为 pandas 中的 dataframe 对象
        df = pd.DataFrame(self.joint_angle_datas).T
        # 修改列名，列名为 joint1 ~ joint6
        df.fillna(0, inplace=True)
        df.columns = ['joint' + str(i) for i in range(1, 7)]
        # 遍历每一行，计算末端位姿
        for i in range(df.shape[0]):
            joint_angles = np.array(df.iloc[i].values)
            # 通过末端位姿计算角度
            translation_vector = self.robot.fkine(joint_angles)
            print("joint_angles: ", joint_angles)
            x, y, z = translation_vector.t
            R, P, Y = translation_vector.rpy(unit='deg')
            print("x: ", round(x, 3), "y: ", round(y, 3), "z: ", round(z, 3))
            print("R: ", round(R, 3), "P: ", round(P, 3), "Y: ", round(Y, 3))
            # 用 x, y, z, R, P, Y 数据生成新的 DataFrame 对象
            endfactor_pose = pd.DataFrame([[x, y, z, R, P, Y]], columns=['x', 'y', 'z', 'R', 'P', 'Y'])
            # 用于测试逆解



if __name__ == '__main__':
    unittest.main()
