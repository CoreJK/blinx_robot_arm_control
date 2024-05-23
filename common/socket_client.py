import socket

from PySide6.QtCore import QRunnable, Slot

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
        logger.warning("线程开始")
        try:
            self.fn(*self.args, **self.kwargs)
        except Exception as e:
            logger.error(str(e))
        logger.warning("线程结束")


class ClientSocket:
    def __init__(self, host, port):
        super().__init__()
        self.host = host
        self.port = port
        self.client_socket_list = []
    
    def new_connect(self):
        try:
            logger.warning(f"尝试连接机械臂: {self.host}:{self.port}...")
            self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            # 设置保活心跳包
            self.client_socket.setsockopt(socket.SOL_SOCKET, socket.SO_KEEPALIVE, True)
            # 30s 发送一次，若 30s 后没有回应，3s/探测一次 ，十次失败断开连接
            self.client_socket.ioctl(socket.SIO_KEEPALIVE_VALS, (1, 30*1000, 3*1000))
            self.client_socket.connect((self.host, self.port))
        except socket.error as e:
            logger.error(f"机械臂连接失败: {e}")
            
        self.client_socket_list.append(self.client_socket)
        return self.client_socket
        
            
    def __enter__(self):
        return self.new_connect()
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.client_socket_list.pop().close()
