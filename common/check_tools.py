from functools import wraps

from PySide6.QtCore import Qt
from qfluentwidgets import InfoBar, InfoBarPosition

def check_robot_arm_connection(func):
    """检查机械臂臂是否已连接"""
    @wraps(func)
    def wrapper(self, *args, **kwargs):
        if not self.robot_arm_is_connected:
            InfoBar.warning(
                title="警告",
                content="⚠️机械臂未连接!\n👈前往连接设置页面\n🦾连接机械臂",
                orient=Qt.Horizontal,
                position=InfoBarPosition.TOP,
                isClosable=True,
                duration=2000,
                parent=self
            )
        else:
            return func(self, *args, **kwargs)
    return wrapper

def check_robot_arm_is_working(func):
    """检查机械臂是否正则执行任务的装饰器"""
    @wraps(func)
    def wrapper(self, *args, **kwargs):
        if self.robot_arm_table_action_status:
            InfoBar.warning(
                title="警告",
                content="⚠️机械臂正在执行任务中，请稍后再试！",
                orient=Qt.Horizontal,
                position=InfoBarPosition.TOP,
                isClosable=True,
                duration=3000,
                parent=self
            )
        else:
            return func(self, *args, **kwargs)
    return wrapper