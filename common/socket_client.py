import socket

from PySide2.QtCore import QRunnable, Slot


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
        print("线程开始")
        try:
            self.fn(*self.args, **self.kwargs)
        except Exception as e:
            print(str(e))
        print("线程结束")


class ClientSocket:
    def __init__(self, host, port):
        super().__init__()
        self.host = host
        self.port = port
        self.client_socket_list = []

    def __enter__(self):
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket.connect((self.host, self.port))
        self.client_socket_list.append(self.client_socket)
        return self.client_socket

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.client_socket_list.pop().close()


if __name__ == "__main__":
    import time
    import json
    HOST = '192.168.10.242'  # 机械臂 IP 地址
    PORT = 1234  # 机械臂端口号
    robot_arm_client = ClientSocket(HOST, PORT)
    with robot_arm_client as rac:
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
                    print(rs_data_dict)
            except (UnicodeError, json.decoder.JSONDecodeError):
                # 等待其他指令完成操作，跳过获取机械臂角度值
                print("等待操作完成")
