import sys
import shelve
from pathlib import Path

from serial.tools import list_ports

from PySide2.QtWidgets import QApplication, QWidget, QMessageBox

# 导入转换后的 UI 文件
from BLinx_Robot_Arm_ui import Ui_Form


class MainWindow(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("BLinx_Robot_Arm_V1.0")
        # 机械臂连接配置页面回调函数绑定
        self.reload_ip_port_history()  #  加载上一次的配置
        self.IpPortInfoSubmitButton.clicked.connect(self.submit_ip_port_info)
        self.IpPortInfoRestButton.clicked.connect(self.reset_ip_port_info)
        # 机械臂 WiFi AP 模式配置页面回调函数绑定
        self.reload_ap_passwd_history()  # 加载上一次的配置
        self.WiFiInfoSubmit.clicked.connect(self.submit_ap_passwd_info)
        self.WiFiInfoReset.clicked.connect(self.reset_ap_passwd_info)
        # 机械臂串口连接配置页面回调函数绑定
        self.SbInfoFreshButton.clicked.connect(self.get_sb_info)

    # 按钮执行结果消息弹窗
    def success_message_box(self, message="成功"):
        """操作成功提示框"""
        msg_box = QMessageBox(self)
        msg_box.setWindowTitle('⚠️Success')
        msg_box.setText(message)
        msg_box.exec_()

    def error_message_box(self, message="失败"):
        """操作失败提示框"""
        msg_box = QMessageBox(self)
        msg_box.setWindowTitle('⚠️Error')
        msg_box.setText(message)
        msg_box.exec_()

    def warning_message_box(self, message="警告"):
        """操作失败警告框"""
        msg_box = QMessageBox(self)
        msg_box.setWindowTitle('⚠️Warning')
        msg_box.setText(message)
        msg_box.exec_()

    # 机械臂连接配置回调函数
    def reload_ip_port_history(self):
        """获取历史IP和Port填写记录"""
        with Path('./config_files/Socket_Info.dat') as socket_file_info:
            if socket_file_info.exists():
                try:
                    socket_info = shelve.open("Socket_info")
                    self.TargetIpEdit.setText(socket_info["target_ip"])
                    self.TargetPortEdit.setText(socket_info["target_port"])
                except KeyError:
                    print("IP 和 Port 未找到对应记录")
            else:
                self.TargetIpEdit.setText("")
                self.TargetPortEdit.setText("")

    def submit_ip_port_info(self):
        """配置机械臂的通讯IP和端口"""
        ip = self.TargetIpEdit.text().strip()
        port = self.TargetPortEdit.text().strip()
        # 保存 IP 和 Port 信息
        with shelve.open('./config_files/Socket_Info') as connect_info:
            if all([ip, port]):
                connect_info["target_ip"] = ip
                connect_info["target_port"] = port
                self.success_message_box(message="配置添加成功!")
            else:
                self.warning_message_box(message="IP 或 Port 号为空，请重新填写!")

    def reset_ip_port_info(self):
        """重置 IP 和 Port 输入框内容"""
        self.TargetIpEdit.clear()
        self.TargetPortEdit.clear()

    # 机械臂 WiFi AP 模式配置回调函数
    def reload_ap_passwd_history(self):
        """获取历史 WiFi 名称和 Passwd 记录"""
        with Path('./config_files/Socket_Info.dat') as socket_file_info:
            if socket_file_info.exists():
                try:
                    socket_info = shelve.open("WiFi_info")
                    self.WiFiSsidEdit.setText(socket_info["SSID"])
                    self.WiFiPasswdEdit.setText(socket_info["passwd"])
                except KeyError:
                    print("WiFi 配置未找到历史记录")
            else:
                self.WiFiSsidEdit.setText("")
                self.WiFiPasswdEdit.setText("")

    def submit_ap_passwd_info(self):
        """配置机械臂的通讯 WiFi 名称和 passwd"""
        ip = self.WiFiSsidEdit.text().strip()
        port = self.WiFiPasswdEdit.text().strip()
        # 保存 IP 和 Port 信息
        with shelve.open('./config_files/WiFi_info') as connect_info:
            if all([ip, port]):
                connect_info["SSID"] = ip
                connect_info["passwd"] = port
                self.success_message_box(message="WiFi 配置添加成功!")
            else:
                self.warning_message_box(message="WiFi名称 或密码为空，请重新填写!")

    def reset_ap_passwd_info(self):
        """重置 WiFi 名称和 passwd 输入框内容"""
        self.WiFiSsidEdit.clear()
        self.WiFiPasswdEdit.clear()

    # todo: 机械臂串口连接配置回调函数
    def get_sb_info(self):
        """获取系统当前的串口信息并更新下拉框"""
        ports = list_ports.comports()
        self.SerialNumComboBox.addItems([f"{port.device}" for port in ports])


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
