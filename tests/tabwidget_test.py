from PySide2.QtWidgets import QApplication, QMainWindow, QTabWidget, QWidget, QVBoxLayout, QTabBar
from PySide2.QtCore import Qt
import sys


class VerticalTextTabBar(QTabBar):
    def __init__(self, parent=None):
        super().__init__(parent)

    def paintEvent(self, event):
        painter = self.tabBarRect(0).adjusted(0, 0, 0, -20)
        for index in range(self.count()):
            option = QStyleOptionTab()
            self.initStyleOption(option, index)
            painter.save()
            painter.translate(option.rect.topLeft())
            painter.rotate(-90)
            self.style().drawControl(QStyle.CE_TabBarTabShape, option, painter)
            self.style().drawControl(QStyle.CE_TabBarTabLabel, option, painter)
            painter.restore()


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        tab_widget = QTabWidget(self)
        tab_widget.setTabBar(VerticalTextTabBar())  # 使用自定义的标签栏

        for i in range(3):
            tab_content = QWidget()
            layout = QVBoxLayout()
            tab_content.setLayout(layout)
            tab_widget.addTab(tab_content, f"Tab {i}")

        self.setCentralWidget(tab_widget)
        self.setWindowTitle("Vertical Tab Text Example")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
