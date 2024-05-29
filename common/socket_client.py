import socket

from PySide6.QtCore import QRunnable, Slot

from loguru import logger

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
            self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.client_socket.settimeout(6)
            self.client_socket.connect((self.host, self.port))
        except (socket.timeout, socket.error) as e:
            logger.error(f"机械臂连接失败: {e}")
            self.client_socket.close()
            raise e
            
        self.client_socket_list.append(self.client_socket)
        return self.client_socket
        
            
    def __enter__(self):
        return self.new_connect()
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.client_socket_list.pop().close()
