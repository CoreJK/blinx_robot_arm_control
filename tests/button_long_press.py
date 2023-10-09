from PySide2.QtWidgets import QApplication, QPushButton, QVBoxLayout, QWidget, QLabel
from PySide2.QtCore import QTimer, Qt

class MyWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        # 创建一个标签用于显示数值
        self.label = QLabel('0')

        # 创建增加和减少按钮
        self.addButton = QPushButton('增加')
        self.subButton = QPushButton('减少')

        # 将标签和按钮添加到布局中
        layout.addWidget(self.label)
        layout.addWidget(self.addButton)
        layout.addWidget(self.subButton)

        # 将布局设置到窗口
        self.setLayout(layout)
        self.setWindowTitle('PySide2 长按增减示例')

        # 按钮状态标志
        self.add_button_pressed = False
        self.sub_button_pressed = False

        # 初始数值
        self.value = 0

        # 创建 QTimer 用于增加或减少数值
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.updateValue)

        # 连接按钮的按下和释放事件
        self.addButton.pressed.connect(self.startIncrement)
        self.addButton.released.connect(self.stopIncrement)
        self.subButton.pressed.connect(self.startDecrement)
        self.subButton.released.connect(self.stopDecrement)

        self.show()

    # 开始增加数值
    def startIncrement(self):
        self.add_button_pressed = True
        self.timer.start(100)  # 每100毫秒增加一次

    # 停止增加数值
    def stopIncrement(self):
        self.add_button_pressed = False
        self.timer.stop()

    # 开始减少数值
    def startDecrement(self):
        self.sub_button_pressed = True
        self.timer.start(100)  # 每100毫秒减少一次

    # 停止减少数值
    def stopDecrement(self):
        self.sub_button_pressed = False
        self.timer.stop()

    # 更新数值
    def updateValue(self):
        if self.add_button_pressed:
            self.value += 1
        elif self.sub_button_pressed:
            self.value -= 1

        # 更新标签显示的数值
        self.label.setText(str(self.value))

if __name__ == '__main__':
    app = QApplication([])
    widget = MyWidget()
    app.exec_()
