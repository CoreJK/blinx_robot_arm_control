import sys
import time
from PySide6.QtCore import Qt, QThread, Signal
from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout
from qfluentwidgets import PushButton, StrongBodyLabel, VBoxLayout


class MyThread(QThread):
    my_signal = Signal(str)
    
    def __init__(self):
        super().__init__()
        self.count = 0
        self.is_on = True
        
    def run(self):
        while self.is_on:
            print(self.count)
            self.count += 1
            self.my_signal.emit(str(self.count))
            self.sleep(1)
        

class Demo(QWidget):
    def __init__(self, parent=None):
        super(Demo, self).__init__()
        self.count = 0
        
        self.button = PushButton('Count', self)
        self.button.clicked.connect(self.count_func)
        
        self.button2 = PushButton('Stop', self)
        self.button2.clicked.connect(self.stop_func)
        
        self.label = StrongBodyLabel('0', self)
        self.label.setAlignment(Qt.AlignCenter)
        
        self.my_thread = MyThread()
        self.my_thread.my_signal.connect(self.set_lable_func)
        
        self.v_layout = VBoxLayout(self)
        self.h_layout = QHBoxLayout()
        self.h_layout.addWidget(self.button)
        self.h_layout.addWidget(self.button2)
        self.v_layout.addWidget(self.label)
        self.v_layout.addLayout(self.h_layout)
        
        self.setLayout(self.v_layout)
        
    def count_func(self):
        self.my_thread.is_on = True
        self.my_thread.start()
    
    def stop_func(self):
        self.my_thread.is_on = False
        
    def set_lable_func(self, value):
        self.label.setText(value)
        
        
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    app.exec()