import sys
import json
import shelve
import time
from pathlib import Path

from serial.tools import list_ports

from PySide2.QtWidgets import QApplication, QWidget, QMessageBox, QTableWidgetItem, QMenu, QFileDialog, QComboBox
from PySide2.QtCore import Qt

# 导入转换后的 UI 文件
from BLinx_Robot_Arm_ui import Ui_Form
from test.socket_client import ClientSocket


class MainWindow(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("BLinx_Robot_Arm_V1.0")

        # 示教控制页面回调函数绑定
        self.ActionAddButton.clicked.connect(self.add_item)
        self.ActionDeleteButton.clicked.connect(self.remove_item)
        self.ActionImportButton.clicked.connect(self.import_data)
        self.ActionOutputButton.clicked.connect(self.export_data)
        self.ActionRunButton.clicked.connect(self.run_action)
        # self.ActionStepRunButton.cllicked.connect(self.run_action_step)
        # self.ActionLoopRunButton.clicked.connect(self.run_action_loop)

        self.ArmToolOptions = self.ArmToolComboBox.model()

        # 示教控制添加右键的上下文菜单
        self.context_menu = QMenu(self)
        self.copy_action = self.context_menu.addAction("复制动作")
        self.paste_action = self.context_menu.addAction("粘贴动作")
        self.copy_action.triggered.connect(self.copy_selected_row)
        self.paste_action.triggered.connect(self.paste_row)
        self.ActionTableWidget.setContextMenuPolicy(Qt.CustomContextMenu)
        self.ActionTableWidget.customContextMenuRequested.connect(self.show_context_menu)

        self.copied_row = None

        # todo 实例化机械臂关节控制回调函数绑定
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

    # 示教控制回调函数编写
    def add_item(self):
        """示教控制添加一行动作"""
        # 获取所有的关节角度数值
        angle_1 = self.AngleOneEdit.text()
        angle_2 = self.AngleTwoEdit.text()
        angle_3 = self.AngleThreeEdit.text()
        angle_4 = self.AngleFourEdit.text()
        angle_5 = self.AngleFiveEdit.text()
        angle_6 = self.AngleSixEdit.text()
        speed_percentage = self.ArmSpeedEdit.text()  # 速度值，暂定百分比

        if all([angle_1, angle_2, angle_3, angle_4, angle_5, angle_6]):
            row_position = self.ActionTableWidget.rowCount()
            self.ActionTableWidget.insertRow(row_position)
            self.ActionTableWidget.setItem(row_position, 0, QTableWidgetItem(angle_1))
            self.ActionTableWidget.setItem(row_position, 1, QTableWidgetItem(angle_2))
            self.ActionTableWidget.setItem(row_position, 2, QTableWidgetItem(angle_3))
            self.ActionTableWidget.setItem(row_position, 3, QTableWidgetItem(angle_4))
            self.ActionTableWidget.setItem(row_position, 4, QTableWidgetItem(angle_5))
            self.ActionTableWidget.setItem(row_position, 5, QTableWidgetItem(angle_6))
            self.ActionTableWidget.setItem(row_position, 6, QTableWidgetItem(speed_percentage))

            # 工具列添加下拉选择框
            arm_tool_combobox = QComboBox()
            arm_tool_combobox.setModel(self.ArmToolOptions)
            self.ActionTableWidget.setCellWidget(row_position, 7, arm_tool_combobox)

            # 开关列添加下拉选择框
            arm_tool_control = QComboBox()
            arm_tool_control.addItems(["", "关", "开"])
            self.ActionTableWidget.setCellWidget(row_position, 8, arm_tool_control)
        else:
            self.warning_message_box(message="角度值不能为空!")

    def remove_item(self):
        """示教控制删除一行动作"""
        selected_rows = self.ActionTableWidget.selectionModel().selectedRows()

        if not selected_rows:
            # 如果没有选中行，则删除最后一行
            last_row = self.ActionTableWidget.rowCount() - 1
            if last_row >= 0:
                self.ActionTableWidget.removeRow(last_row)
        else:
            for row in reversed(selected_rows):
                self.ActionTableWidget.removeRow(row.row())

    def copy_selected_row(self):
        """复制选择行"""
        selected_row = self.ActionTableWidget.currentRow()
        if selected_row >= 0:
            self.copied_row = []
            for col in range(self.ActionTableWidget.columnCount()):
                # 工具列、开关列，需要获取下拉框中的文本
                if col in (7, 8):
                    item_widget = self.ActionTableWidget.cellWidget(selected_row, col)
                    if item_widget is not None:
                        self.copied_row.append(item_widget.currentText())
                else:
                    item = self.ActionTableWidget.item(selected_row, col)
                    if item is not None:
                        self.copied_row.append(item.text())

    def paste_row(self):
        """粘贴选择行"""
        if self.copied_row:
            row_position = self.ActionTableWidget.rowCount()
            self.ActionTableWidget.insertRow(row_position)
            for col, value in enumerate(self.copied_row):
                if col == 7:  # 工具列、开关列需要获取下拉框的选中值
                    # 工具列添加下拉选择框
                    arm_tool_combobox = QComboBox()
                    arm_tool_combobox.setModel(self.ArmToolOptions)
                    arm_tool_combobox.setCurrentText(value)
                    self.ActionTableWidget.setCellWidget(row_position, col, arm_tool_combobox)
                elif col == 8:
                    # 开关列添加下拉选择框
                    arm_tool_control = QComboBox()
                    arm_tool_control.addItems(["", "关", "开"])
                    arm_tool_control.setCurrentText(value)
                    self.ActionTableWidget.setCellWidget(row_position, col, arm_tool_control)
                else:
                    self.ActionTableWidget.setItem(row_position, col, QTableWidgetItem(value))

    def import_data(self):
        """导入动作"""
        options = QFileDialog.Options()
        file_name, _ = QFileDialog.getOpenFileName(self, "Import Data from JSON", "",
                                                   "JSON Files (*.json);;All Files (*)", options=options)

        if file_name:
            with open(file_name, "r") as json_file:
                data = json.load(json_file)

                self.ActionTableWidget.setRowCount(0)  # 清空表格

                for item in data:
                    angle_1 = item.get("J1/X", "")
                    angle_2 = item.get("J2/X", "")
                    angle_3 = item.get("J3/X", "")
                    angle_4 = item.get("J4/X", "")
                    angle_5 = item.get("J5/X", "")
                    angle_6 = item.get("J6/X", "")
                    speed_percentage = item.get("速度", 30)  # 速度百分比默认为 30%
                    arm_tool_option = item.get("工具", "")
                    arm_tool_control = item.get("开关", "")

                    row_position = self.ActionTableWidget.rowCount()
                    self.ActionTableWidget.insertRow(row_position)
                    self.ActionTableWidget.setItem(row_position, 0, QTableWidgetItem(angle_1))
                    self.ActionTableWidget.setItem(row_position, 1, QTableWidgetItem(angle_2))
                    self.ActionTableWidget.setItem(row_position, 2, QTableWidgetItem(angle_3))
                    self.ActionTableWidget.setItem(row_position, 3, QTableWidgetItem(angle_4))
                    self.ActionTableWidget.setItem(row_position, 4, QTableWidgetItem(angle_5))
                    self.ActionTableWidget.setItem(row_position, 5, QTableWidgetItem(angle_6))
                    self.ActionTableWidget.setItem(row_position, 6, QTableWidgetItem(speed_percentage))

                    # 工具列
                    arm_tool_combobox = QComboBox()
                    arm_tool_combobox.setModel(self.ArmToolOptions)
                    arm_tool_combobox.setCurrentText(arm_tool_option)
                    self.ActionTableWidget.setCellWidget(row_position, 7, arm_tool_combobox)

                    # 开关列
                    arm_tool_control_combobox = QComboBox()
                    arm_tool_control_combobox.addItems(["", "关", "开"])
                    arm_tool_control_combobox.setCurrentText(arm_tool_control)
                    self.ActionTableWidget.setCellWidget(row_position, 8, arm_tool_control_combobox)

    def export_data(self):
        """导出动作"""
        options = QFileDialog.Options()
        file_name, _ = QFileDialog.getSaveFileName(self, "Save Data to JSON", "", "JSON Files (*.json);;All Files (*)",
                                                   options=options)

        if file_name:
            data = []
            for row in range(self.ActionTableWidget.rowCount()):
                angle_1 = self.ActionTableWidget.item(row, 0).text()
                angle_2 = self.ActionTableWidget.item(row, 1).text()
                angle_3 = self.ActionTableWidget.item(row, 2).text()
                angle_4 = self.ActionTableWidget.item(row, 3).text()
                angle_5 = self.ActionTableWidget.item(row, 4).text()
                angle_6 = self.ActionTableWidget.item(row, 5).text()
                speed_percentage = self.ActionTableWidget.item(row, 6).text()
                arm_tool_widget = self.ActionTableWidget.cellWidget(row, 7)  # 工具列
                arm_tool_control_widget = self.ActionTableWidget.cellWidget(row, 8)  # 开关列

                if arm_tool_widget is not None:
                    arm_tool_option = arm_tool_widget.currentText()
                else:
                    arm_tool_option = ""

                if arm_tool_control_widget is not None:
                    arm_tool_control_widget = arm_tool_control_widget.currentText()
                else:
                    arm_tool_control_widget = ""

                data.append({
                             "J1/X": angle_1,
                             "J2/X": angle_2,
                             "J3/X": angle_3,
                             "J4/X": angle_4,
                             "J5/X": angle_5,
                             "J6/X": angle_6,
                             "速度": speed_percentage,
                             "工具": arm_tool_option,
                             "开关": arm_tool_control_widget
                })

            with open(file_name, "w") as json_file:
                json.dump(data, json_file, indent=4, ensure_ascii=False)

    def run_action(self):
        """顺序执行动作"""
        # todo 遍历动作
        self.TeachArmRunLogWindow.append("【顺序执行】开始！")
        with self.get_robot_arm_connector() as robot_client:
            for row in range(self.ActionTableWidget.rowCount()):
                angle_1 = int(self.ActionTableWidget.item(row, 0).text())
                angle_2 = int(self.ActionTableWidget.item(row, 1).text())
                angle_3 = int(self.ActionTableWidget.item(row, 2).text())
                angle_4 = int(self.ActionTableWidget.item(row, 3).text())
                angle_5 = int(self.ActionTableWidget.item(row, 4).text())
                angle_6 = int(self.ActionTableWidget.item(row, 5).text())
                speed_percentage = int(self.ActionTableWidget.item(row, 6).text())
                delay_time = int(self.ActionTableWidget.item(row, 9).text())
                # todo 构造命令
                json_command = {"command": "set_joint_angle_all_time",
                                "data": [angle_1, angle_2, angle_3, angle_4, angle_5, angle_6, delay_time, speed_percentage]}
                str_command = json.dumps(json_command).replace(' ', "") + '\r\n'
                robot_client.send(str_command.encode('utf-8'))
                self.TeachArmRunLogWindow.append(f"机械臂正在执行第 {row + 1} 个动作")
                time.sleep(delay_time)  # 等待动作执行完成
        self.TeachArmRunLogWindow.append("【顺序执行】结束！")

    def run_action_step(self):
        """单次执行选定的动作"""
        pass

    def run_action_loop(self):
        """循环执行动作"""
        pass

    def show_context_menu(self, pos):
        """右键复制粘贴菜单"""
        self.context_menu.exec_(self.ActionTableWidget.mapToGlobal(pos))

    def get_robot_arm_connector(self):
        """获取与机械臂的连接对象"""
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
