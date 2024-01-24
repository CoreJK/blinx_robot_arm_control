from PySide6.QtWidgets import QMessageBox

class BlinxMessageBox:
    def __init__(self, parent=None):
        self.parent = parent

    def show_message(self, message, title):
        msg_box = QMessageBox(self.parent)
        msg_box.setWindowTitle(title)
        msg_box.setText(message)
        msg_box.exec_()

    def success_message_box(self, message="成功"):
        self.show_message(message, 'Success')

    def error_message_box(self, message="失败"):
        self.show_message(message, 'Error')

    def warning_message_box(self, message="警告"):
        self.show_message(message, 'Warning')

# 示例用法：
# message_box = BlinxMessageBox(self)
# message_box.success_message_box("操作成功")
# message_box.error_message_box("操作失败")
# message_box.warning_message_box("警告")
