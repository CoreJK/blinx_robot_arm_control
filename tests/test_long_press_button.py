from PySide2.QtWidgets import QApplication
from PySide2.QtWidgets import QPushButton
from PySide2.QtCore import QTimer

class LongPressButton(QPushButton):
    def __init__(self, parent=None):
        super(LongPressButton, self).__init__(parent)
        self.timer = QTimer()
        self.timer.setInterval(500)  # 设置长按时间为0.5秒
        self.timer.timeout.connect(self.on_long_press)
        self.data = 0
        self.setText("Long Press Me")

    def mousePressEvent(self, event):
        self.timer.start()
        super(LongPressButton, self).mousePressEvent(event)

    def mouseReleaseEvent(self, event):
        self.timer.stop()
        super(LongPressButton, self).mouseReleaseEvent(event)

    def on_long_press(self):
        self.data -= 1
        print(self.data)
        self.timer.start()

if __name__ == "__main__":
    app = QApplication([])
    w = LongPressButton()
    w.show()
    app.exec_()