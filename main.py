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

        # todo 实例化机械臂关节控制回调函数类
        self.AngleStepAddButton.clicked.connect(self.arm_angle_step_add)
        self.AngleStepSubButton.clicked.connect(self.arm_angle_step_sub)
        self.AngleOneAddButton.clicked.connect(self.arm_one_add)
        self.AngleOneSubButton.clicked.connect(self.arm_one_sub)
        self.AngleTwoAddButton.clicked.connect(self.arm_two_add)
        self.AngleTwoSubButton.clicked.connect(self.arm_two_sub)
        self.AngleThreeAddButton.clicked.connect(self.arm_three_add)
        self.AngleThreeSubButton.clicked.connect(self.arm_three_sub)
        self.AngleFourAddButton.clicked.connect(self.arm_four_add)
        self.AngleFourSubButton.clicked.connect(self.arm_four_sub)
        self.AngleFiveAddButton.clicked.connect(self.arm_five_add)
        self.AngleFiveSubButton.clicked.connect(self.arm_five_sub)
        self.AngleSixAddButton.clicked.connect(self.arm_six_add)
        self.AngleSixSubButton.clicked.connect(self.arm_six_sub)

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
        """操作成功提示框
        :param message: 提示框显示的消息
        """
        msg_box = QMessageBox(self)
        msg_box.setWindowTitle('⚠️Success')
        msg_box.setText(message)
        msg_box.exec_()

    def error_message_box(self, message="失败"):
        """操作失败提示框
        :param message: 提示框显示的消息
        """
        msg_box = QMessageBox(self)
        msg_box.setWindowTitle('⚠️Error')
        msg_box.setText(message)
        msg_box.exec_()

    def warning_message_box(self, message="警告"):
        """操作失败警告框
        :param message: 提示框显示的消息
        """
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

    # 机械臂连接按钮回调函数
    def reset_robot_arm(self, mode="connect"):
        """机械臂复位
        :param mode:
        """
        # 初始化步长和速度值
        self.AngleStepEdit.setText(str(5))
        self.ArmSpeedEdit.setText(str(80))
        robot_arm_client = self.get_robot_arm_connector()
        with robot_arm_client as rac:
            rac.send(b'{"command":"set_joint_Auto_zero"}\r\n')
            rs_data = json.loads(rac.recv(1024).decode('utf-8').strip()).get("data")
            if rs_data == "true" and mode == "connect":
                self.success_message_box("机械臂连接成功")
            else:
                self.warning_message_box("机械臂复位中!请注意手臂姿态")

    # 命令控制页面 json 发送与调试
    def send_json_command(self):
        """json数据发送按钮"""
        json_data = self.CommandEditWindow.toPlainText() + '\r\n'
        self.CommandSendWindow.append(json_data.strip())

        # 发送机械臂命令
        robot_arm_client = self.get_robot_arm_connector()
        with robot_arm_client as rac:
            rac.send(json_data.encode('utf-8'))
            rs_data = json.loads(rac.recv(1024).decode('utf-8').strip())
            self.CommandResWindow.append(json.dumps(rs_data))  # 命令响应填入到
            if rs_data.get("data") == "true":
                self.CommandArmRunLogWindow.append("机械臂执行指令中...")
            else:
                self.CommandArmRunLogWindow.append("机械臂命令执行失败!")

    # 机械臂关节控制回调函数
    def arm_one_add(self):
        """机械臂关节增加"""
        # todo 获取机械臂当前的角度(手臂未提供该接口)
        old_degrade = int(self.AngleOneEdit.text().strip())
        increase_degrade = int(self.AngleStepEdit.text().strip())
        degrade = old_degrade + increase_degrade
        # 每个关节的最大限位值不同
        if 0 <= degrade <= 300:
            self.AngleOneEdit.setText(str(degrade))  # 更新关节角度值

            # todo 构造发送命令
            command = json.dumps({"command": "set_joint_angle", "data": [1, degrade]}) + '\r\n'

            # 发送命令
            robot_arm_client = self.get_robot_arm_connector()
            with robot_arm_client as rc:
                rc.send(command.replace(' ', '').encode())
                response = rc.recv(1024).decode('utf-8').strip()
                self.TeachArmRunLogWindow.append(response)
        else:
            degrade = 300
            self.AngleOneEdit.setText(str(degrade))
            self.warning_message_box(message="关节 1 最大角度值为 300 度！")



    def arm_one_sub(self):
        """机械臂关节角度减少"""
        # todo 获取机械臂当前的角度(手臂未提供该接口)
        old_degrade = int(self.AngleOneEdit.text().strip())
        decrease_degrade = int(self.AngleStepEdit.text().strip())
        degrade = old_degrade - decrease_degrade
        if 0 <= degrade <= 300:
            self.AngleOneEdit.setText(str(degrade))
            # 发送命令
            command = json.dumps({"command": "set_joint_angle", "data": [1, degrade]}) + '\r\n'
            robot_arm_client = self.get_robot_arm_connector()
            with robot_arm_client as rc:
                rc.send(command.replace(' ', '').encode())
                response = rc.recv(1024).decode('utf-8').strip()
                self.TeachArmRunLogWindow.append(response)
        else:
            self.warning_message_box(message="关节 1 角度不能为负！")



    def arm_two_add(self):
        """机械臂关节增加"""
        # todo 获取机械臂当前的角度(手臂未提供该接口)
        old_degrade = int(self.AngleTwoEdit.text().strip())
        increase_degrade = int(self.AngleStepEdit.text().strip())
        degrade = old_degrade + increase_degrade
        self.AngleTwoEdit.setText(str(degrade))  # 更新关节角度值

        # todo 构造发送命令
        command = json.dumps({"command": "set_joint_angle", "data": [2, degrade]}) + '\r\n'

        # 发送命令
        robot_arm_client = self.get_robot_arm_connector()
        with robot_arm_client as rc:
            rc.send(command.replace(' ', '').encode())
            response = rc.recv(1024).decode('utf-8').strip()
            self.TeachArmRunLogWindow.append(response)

    def arm_two_sub(self):
        """机械臂关节角度减少"""
        # todo 获取机械臂当前的角度(手臂未提供该接口)
        old_degrade = int(self.AngleTwoEdit.text().strip())
        decrease_degrade = int(self.AngleStepEdit.text().strip())
        degrade = old_degrade - decrease_degrade
        if 0 <= degrade:
            self.AngleTwoEdit.setText(str(degrade))
            # 发送命令
            command = json.dumps({"command": "set_joint_angle", "data": [2, degrade]}) + '\r\n'
            robot_arm_client = self.get_robot_arm_connector()
            with robot_arm_client as rc:
                rc.send(command.replace(' ', '').encode())
                response = rc.recv(1024).decode('utf-8').strip()
                self.TeachArmRunLogWindow.append(response)
        else:
            self.warning_message_box(message="关节 2 角度不能为负！")



    def arm_three_add(self):
        """机械臂关节增加"""
        # todo 获取机械臂当前的角度(手臂未提供该接口)
        old_degrade = int(self.AngleThreeEdit.text().strip())
        increase_degrade = int(self.AngleStepEdit.text().strip())
        degrade = old_degrade + increase_degrade
        self.AngleThreeEdit.setText(str(degrade))  # 更新关节角度值

        # todo 构造发送命令
        command = json.dumps({"command": "set_joint_angle", "data": [3, degrade]}) + '\r\n'

        # 发送命令
        robot_arm_client = self.get_robot_arm_connector()
        with robot_arm_client as rc:
            rc.send(command.replace(' ', '').encode())
            response = rc.recv(1024).decode('utf-8').strip()
            self.TeachArmRunLogWindow.append(response)

    def arm_three_sub(self):
        """机械臂关节角度减少"""
        # todo 获取机械臂当前的角度(手臂未提供该接口)
        old_degrade = int(self.AngleThreeEdit.text().strip())
        decrease_degrade = int(self.AngleStepEdit.text().strip())
        degrade = old_degrade - decrease_degrade
        if 0 <= degrade:
            self.AngleThreeEdit.setText(str(degrade))
            # 发送命令
            command = json.dumps({"command": "set_joint_angle", "data": [3, degrade]}) + '\r\n'
            robot_arm_client = self.get_robot_arm_connector()
            with robot_arm_client as rc:
                rc.send(command.replace(' ', '').encode())
                response = rc.recv(1024).decode('utf-8').strip()
                self.TeachArmRunLogWindow.append(response)
        else:
            self.warning_message_box(message="关节 3 角度不能为负！")



    def arm_four_add(self):
        """机械臂关节增加"""
        # todo 获取机械臂当前的角度(手臂未提供该接口)
        old_degrade = int(self.AngleFourEdit.text().strip())
        increase_degrade = int(self.AngleStepEdit.text().strip())
        degrade = old_degrade + increase_degrade
        self.AngleFourEdit.setText(str(degrade))  # 更新关节角度值

        # todo 构造发送命令
        command = json.dumps({"command": "set_joint_angle", "data": [4, degrade]}) + '\r\n'

        # 发送命令
        robot_arm_client = self.get_robot_arm_connector()
        with robot_arm_client as rc:
            rc.send(command.replace(' ', '').encode())
            response = rc.recv(1024).decode('utf-8').strip()
            self.TeachArmRunLogWindow.append(response)

    def arm_four_sub(self):
        """机械臂关节角度减少"""
        # todo 获取机械臂当前的角度(手臂未提供该接口)
        old_degrade = int(self.AngleFourEdit.text().strip())
        decrease_degrade = int(self.AngleStepEdit.text().strip())
        degrade = old_degrade - decrease_degrade
        if 0 <= degrade:
            self.AngleFourEdit.setText(str(degrade))
            # 发送命令
            command = json.dumps({"command": "set_joint_angle", "data": [4, degrade]}) + '\r\n'
            robot_arm_client = self.get_robot_arm_connector()
            with robot_arm_client as rc:
                rc.send(command.replace(' ', '').encode())
                response = rc.recv(1024).decode('utf-8').strip()
                self.TeachArmRunLogWindow.append(response)
        else:
            self.warning_message_box(message="关节 4 角度不能为负！")



    def arm_five_add(self):
        """机械臂关节增加"""
        # todo 获取机械臂当前的角度(手臂未提供该接口)
        old_degrade = int(self.AngleFiveEdit.text().strip())
        increase_degrade = int(self.AngleStepEdit.text().strip())
        degrade = old_degrade + increase_degrade
        if 0 <= degrade:
            self.AngleFiveEdit.setText(str(degrade))  # 更新关节角度值

        # todo 构造发送命令
        command = json.dumps({"command": "set_joint_angle", "data": [5, degrade]}) + '\r\n'

        # 发送命令
        robot_arm_client = self.get_robot_arm_connector()
        with robot_arm_client as rc:
            rc.send(command.replace(' ', '').encode())
            response = rc.recv(1024).decode('utf-8').strip()
            self.TeachArmRunLogWindow.append(response)

    def arm_five_sub(self):
        """机械臂关节角度减少"""
        # todo 获取机械臂当前的角度(手臂未提供该接口)
        old_degrade = int(self.AngleFiveEdit.text().strip())
        decrease_degrade = int(self.AngleStepEdit.text().strip())
        degrade = old_degrade - decrease_degrade
        if 0 <= degrade:
            self.AngleFiveEdit.setText(str(degrade))
            # 发送命令
            command = json.dumps({"command": "set_joint_angle", "data": [5, degrade]}) + '\r\n'
            robot_arm_client = self.get_robot_arm_connector()
            with robot_arm_client as rc:
                rc.send(command.replace(' ', '').encode())
                response = rc.recv(1024).decode('utf-8').strip()
                self.TeachArmRunLogWindow.append(response)
        else:
            self.warning_message_box(message="关节 5 角度不能为负！")



    def arm_six_add(self):
        """机械臂关节增加"""
        # todo 获取机械臂当前的角度(手臂未提供该接口)
        old_degrade = int(self.AngleSixEdit.text().strip())
        increase_degrade = int(self.AngleStepEdit.text().strip())
        degrade = old_degrade + increase_degrade
        self.AngleSixEdit.setText(str(degrade))  # 更新关节角度值

        # todo 构造发送命令
        command = json.dumps({"command": "set_joint_angle", "data": [6, degrade]}) + '\r\n'

        # 发送命令
        robot_arm_client = self.get_robot_arm_connector()
        with robot_arm_client as rc:
            rc.send(command.replace(' ', '').encode())
            response = rc.recv(1024).decode('utf-8').strip()
            self.TeachArmRunLogWindow.append(response)

    def arm_six_sub(self):
        """机械臂关节角度减少"""
        # todo 获取机械臂当前的角度(手臂未提供该接口)
        old_degrade = int(self.AngleSixEdit.text().strip())
        decrease_degrade = int(self.AngleStepEdit.text().strip())
        degrade = old_degrade - decrease_degrade
        if 0 <= degrade:
            self.AngleSixEdit.setText(str(degrade))
            # 发送命令
            command = json.dumps({"command": "set_joint_angle", "data": [6, degrade]}) + '\r\n'
            robot_arm_client = self.get_robot_arm_connector()
            with robot_arm_client as rc:
                rc.send(command.replace(' ', '').encode())
                response = rc.recv(1024).decode('utf-8').strip()
                self.TeachArmRunLogWindow.append(response)
        else:
            self.warning_message_box(message="关节 6 角度不能为负！")



    def arm_angle_step_add(self):
        """机械臂关节步长增加"""
        old_degrade = int(self.AngleStepEdit.text().strip())
        degrade = old_degrade + 5
        if 0 < degrade <= 20:
            self.AngleStepEdit.setText(str(degrade))
        else:
            self.warning_message_box(message="步长不能超过 20")

    def arm_angle_step_sub(self):
        """机械臂关节步长减少"""
        old_degrade = int(self.AngleStepEdit.text().strip())
        degrade = old_degrade - 5
        if degrade > 0:
            self.AngleStepEdit.setText(str(degrade))
        else:
            self.warning_message_box(message="步长不能为负!")

    def get_robot_arm_connector(self):
        try:
            socket_info = shelve.open("./config_files/Socket_info")
            host = socket_info['target_ip']
            port = int(socket_info['target_port'])
        except Exception as e:
            self.error_message_box(message="没有读取到 ip 和 port 信息，请前往机械臂配置 ！")
        robot_arm_client = ClientSocket(host, port)
        return robot_arm_client


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
