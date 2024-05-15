from functools import wraps

from PySide6.QtCore import Qt
from qfluentwidgets import InfoBar, InfoBarPosition

def check_robot_arm_connection(func):
    """
    Decorator function to check if the robot arm is connected before executing the decorated function.

    Args:
        func (function): The function to be decorated.

    Returns:
        function: The decorated function.

    Raises:
        None

    """
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