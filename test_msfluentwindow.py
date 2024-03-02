# -*- coding:utf-8 -*-
import sys

from PySide6.QtCore import Qt
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication, QFrame

# qfluent GUI 组件库
from qfluentwidgets import SplitFluentWindow, FluentWindow, MSFluentWindow
from qfluentwidgets import FluentIcon as FIF
from app.command_page import command_page_frame
from app.teach_page import teach_page_frame



class CommandPage(QFrame, command_page_frame):
    """命令控制页面"""
    def __init__(self, page_name, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.setObjectName(page_name.replace(' ', '-'))
        self.PushButton.setIcon(FIF.SEND)
        self.PushButton.setText('发送')


class TeachPage(QFrame, teach_page_frame):
    """示教控制页面"""
    def __init__(self, page_name, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.setObjectName(page_name.replace(' ', '-'))



class Window(MSFluentWindow):
    """上位机主窗口"""    
    def __init__(self):
        super().__init__()
        self.commandInterface = CommandPage('命令控制', self)
        self.teachInterface = TeachPage('示教控制', self)
        
        self.initNavigation()
        self.initWindow()
        
        
    def initWindow(self):
        """初始化窗口"""
        self.resize(1300, 700)
        self.setWindowTitle("比邻星六轴机械臂上位机")
        self.setWindowIcon(QIcon(":/icons/icons/Robot_arm_log.png"))  # 设置窗口图标
        
        # 根据屏幕大小居中显示
        desktop = QApplication.screens()[0].availableGeometry()
        w, h = desktop.width(), desktop.height()
        self.move(w//2 - self.width()//2, h//2 - self.height()//2)
    
    def initNavigation(self):
        """初始化导航栏"""
        self.addSubInterface(self.commandInterface, FIF.COMMAND_PROMPT, '命令控制')
        self.addSubInterface(self.teachInterface, FIF.APPLICATION, '示教控制')
        
        # 设置默认打开的页面
        self.navigationInterface.setCurrentItem(self.commandInterface.objectName())


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = Window()
    w.show()
    app.exec()
    