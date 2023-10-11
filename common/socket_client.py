import socket

from PySide2.QtCore import QRunnable, Slot
from loguru import logger
from retrying import retry

class Worker(QRunnable):
    """Worker thread

    用于在 PySide 中实现界面的线程
    """

    def __init__(self, fn, *args, **kwargs):
        super(Worker, self).__init__()
        self.fn = fn
        self.args = args
        self.kwargs = kwargs

    @Slot()
    def run(self):
        """运行需要作为线程运行的函数"""
        logger.info("线程开始")
        try:
            self.fn(*self.args, **self.kwargs)
        except Exception as e:
            logger.error(str(e))
        logger.info("线程结束")


class ClientSocket:
    def __init__(self, host, port):
        super().__init__()
        self.host = host
        self.port = port
        self.client_socket_list = []

    @retry(stop_max_attempt_number=3, wait_fixed=1000)
    def new_connect(self):
        logger.info("正在尝试连接机械臂...")
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket.connect((self.host, self.port))
        self.client_socket_list.append(self.client_socket)
        logger.info("连接成功!")
        return self.client_socket
            
    def __enter__(self):
        return self.new_connect()
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.client_socket_list.pop().close()



if __name__ == "__main__":
    import time
    import json
    from blinx_robot_module import Mirobot
    import numpy as np
    from math import degrees
    from spatialmath import SE3
    from spatialmath.base import rpy2tr
    
    @retry(wait_fixed=2000)
    def get_robot_arm_value(ClientSocket, robot_arm, HOST, PORT):
        """测试 socket 通讯的代码"""
        robot_arm_client = ClientSocket(HOST, PORT)
        with robot_arm_client as rac:
            logger.warning("机械臂开始复位!")
            rac.send(b'{"command":"set_joint_Auto_zero"}\r\n')
            while True:
                try:
                    time.sleep(2)
                    # 获取机械臂角度值 API
                    rac.sendall(b'{"command":"get_joint_angle_all"}\r\n')
                    rs_data = rac.recv(1024).decode('utf-8')
                    rs_data_dict = json.loads(rs_data)
                    # 只获取关节角度的回执
                    if rs_data_dict["return"] == "get_joint_angle_all":
                        # todo 实时解析出末端工具坐标和姿态值
                        q1 = round(float(rs_data_dict['data'][0]), 2)
                        q2 = round(float(rs_data_dict['data'][1]), 2)
                        q3 = round(float(rs_data_dict['data'][2]), 2)
                        q4 = round(float(rs_data_dict['data'][3]), 2)
                        q5 = round(float(rs_data_dict['data'][4]), 2)
                        q6 = round(float(rs_data_dict['data'][5]), 2)
                        logger.info("机械臂角度", [q1, q2, q3, q4, q5, q6])
                        arm_pose_degree = np.array([q1, q2, q3, q4, q5, q6])
                        translation_vector = robot_arm.fkine(arm_pose_degree)

                        logger.info("机械臂正解结果")
                        logger.info(translation_vector.printline())
                        x, y, z = translation_vector.t  # 平移向量
                        logger.info(f"x = {round(x, 2)}")
                        logger.info(f"y = {round(y, 2)}")
                        logger.info(f"z = {round(z, 2)}")
                        logger.info('')
                        Rz, Ry, Rx = map(lambda x: degrees(x), translation_vector.rpy())  # 旋转角
                        logger.info(f"Rz ={round(Rz, 2)} ", )
                        logger.info(f"Ry ={round(Ry, 2)} ", )
                        logger.info(f"Rx ={round(Rx, 2)} ", )
                        logger.info("")
                        
                        logger.info("机械臂逆解结果")
                        R_T = SE3([x, y, z]) * rpy2tr([Rz, Ry, Rx], unit='deg')
                        sol = robot_arm.ikine_LM(R_T, joint_limits=True)

                        def get_value(number):
                            res = round(degrees(number), 2)
                            return res

                        logger.info(list(map(get_value, sol.q)))
                except (UnicodeError, json.decoder.JSONDecodeError):
                    # 等待其他指令完成操作，跳过获取机械臂角度值
                    logger.info("等待操作完成")
    
    # 实例化机械臂模型
    robot_arm = Mirobot()
    
    HOST = '192.168.10.242'  # 机械臂 IP 地址
    PORT = 1234  # 机械臂端口号
    logger.info("开始连接机械臂...")
    get_robot_arm_value(ClientSocket, robot_arm, HOST, PORT)
