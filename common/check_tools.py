from functools import wraps

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
            self.message_box.warning_message_box("机械臂未连接！")
        else:
            return func(self, *args, **kwargs)
    return wrapper