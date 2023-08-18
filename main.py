import sys
import json
import queue
import shelve
from pathlib import Path

from serial.tools import list_ports

from PySide2.QtWidgets import QApplication, QWidget, QMessageBox

# 导入转换后的 UI 文件
from BLinx_Robot_Arm_ui import Ui_Form
from test.socket_client import ClientSocket


class MainWindow(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("BLinx_Robot_Arm_V1.0")

        # todo 初始化队列
        self.command_queue = queue.Queue()

        # 机械臂连接配置页面回调函数绑定
        self.reload_ip_port_history()  # 加载上一次的配置
        self.IpPortInfoSubmitButton.clicked.connect(self.submit_ip_port_info)
        self.IpPortInfoRestButton.clicked.connect(self.reset_ip_port_info)

        # 机械臂 WiFi AP 模式配置页面回调函数绑定
        self.reload_ap_passwd_history()  # 加载上一次的配置
        self.WiFiInfoSubmit.clicked.connect(self.submit_ap_passwd_info)
        self.WiFiInfoReset.clicked.connect(self.reset_ap_passwd_info)

        # 机械臂串口连接配置页面回调函数绑定
        self.SbInfoFreshButton.clicked.connect(self.get_sb_info)

        # todo 连接机械臂按钮回调函数绑定
        self.RobotArmLinkButton.clicked.connect(self.reset_robot_arm)

        # todo 命令控制页面回调函数绑定
        self.CommandSendButton.clicked.connect(self.send_json_command)

        # 复位和急停按钮绑定
        self.RobotArmResetButton.clicked.connect(self.reset_robot_arm)

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
                    socket_info = shelve.open("./config_files/Socket_info")
                    self.TargetIpEdit.setText(socket_info["target_ip"])
                    self.TargetPortEdit.setText(str(socket_info["target_port"]))
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
                connect_info["target_port"] = int(port)
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
                    socket_info = shelve.open("./config_files/WiFi_info")
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

    # todo: 机械臂连接按钮回调函数
    def reset_robot_arm(self, mode="connect"):
        """机械臂复位"""
        try:
            socket_info = shelve.open("./config_files/Socket_info")
            host = socket_info['target_ip']
            port = int(socket_info['target_port'])
        except Exception as e:
            self.error_message_box(message="没有读取到 ip 和 port 信息，请前往机械臂配置 ！")

        robot_arm_client = ClientSocket(host, port)
        with robot_arm_client as rac:
            rac.send(b'{"command":"set_joint_Auto_zero"}\r\n')
            rs_data = json.loads(rac.recv(1024).decode('utf-8').strip()).get("data")
            if rs_data == "true" and mode == "connect":
                self.success_message_box("机械臂连接成功")
            else:
                self.warning_message_box("机械臂复位中!请注意手臂姿态")

    # todo: 命令控制页面 json 发送与调试
    def send_json_command(self):
        """json数据发送按钮"""
        json_data = self.CommandEditWindow.toPlainText() + '\r\n'
        self.CommandSendWindow.append(json_data.strip())

        # 读取机械臂连接配置
        socket_info = shelve.open("./config_files/Socket_info")
        host = socket_info['target_ip']
        port = int(socket_info['target_port'])

        # 发送机械臂命令
        robot_arm_client = ClientSocket(host, port)
        with robot_arm_client as rac:
            rac.send(json_data.encode('utf-8'))
            rs_data = json.loads(rac.recv(1024).decode('utf-8').strip())
            self.CommandResWindow.append(json.dumps(rs_data))  # 命令响应填入到
            if rs_data.get("data") == "true":
                self.CommandArmRunLogWindow.append("机械臂执行指令中...")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
