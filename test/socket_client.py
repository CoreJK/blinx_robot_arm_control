import socket


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
    HOST = '192.168.10.242'  # 服务端IP地址
    PORT = 1234  # 服务端端口号
    robot_arm_client = ClientSocket(HOST, PORT)
    with robot_arm_client as rac:
        rac.send(b'{"command":"set_joint_Auto_zero"}\r\n')
        rs_data = rac.recv(1024).decode('utf-8')
        print(rs_data)

