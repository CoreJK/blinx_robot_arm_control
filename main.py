import json
import platform
import shelve
import socket
import sys
import time
from pathlib import Path

from PySide2.QtCore import Qt, QThreadPool
from PySide2.QtWidgets import (QApplication, QComboBox, QFileDialog, QMenu,
                               QTableWidgetItem, QWidget)
from qt_material import apply_stylesheet
from serial.tools import list_ports

# 导入转换后的 UI 文件
from app.BLinx_Robot_Arm_ui import Ui_Form
from componets.message_box import BlinxMessageBox
from common.socket_client import ClientSocket, Worker

import faulthandler;faulthandler.enable()

class MainWindow(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("BLinx Robot Arm V1.0")
        
        # 获取操作系统的版本信息
        self.os_name = platform.system()
        self.os_version = platform.release()
        
        # 开启 QT 线程池
        self.threadpool = QThreadPool()

        # 机械臂的查询循环控制位
        self.loop_flag = False

        # 初始化消息提示窗口
        self.message_box = BlinxMessageBox(self)
        
        # 示教控制页面回调函数绑定
        self.ActionAddButton.clicked.connect(self.add_item)
        self.ActionDeleteButton.clicked.connect(self.remove_item)
        self.ActionImportButton.clicked.connect(self.import_data)
        self.ActionOutputButton.clicked.connect(self.export_data)
        self.ActionRunButton.clicked.connect(self.run_all_action)
        self.ActionStepRunButton.clicked.connect(self.run_action_step)
        self.ActionLoopRunButton.clicked.connect(self.run_action_loop)

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

        # 实例化机械臂关节控制回调函数绑定
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
        self.ArmSpeedUpButton.clicked.connect(self.arm_speed_percentage_add)
        self.ArmSpeedDecButton.clicked.connect(self.arm_speed_percentage_sub)

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

        # 连接机械臂按钮回调函数绑定
        self.RobotArmLinkButton.clicked.connect(self.check_arm_connect_state)

        # 命令控制页面回调函数绑定
        self.CommandSendButton.clicked.connect(self.send_json_command)

        # 复位和急停按钮绑定
        self.RobotArmResetButton.clicked.connect(self.reset_robot_arm)

        # todo 末端工具控制组回调函数绑定
        self.ArmClawOpenButton.clicked.connect(self.tool_open)
        self.ArmClawCloseButton.clicked.connect(self.tool_close)
        
    # 机械臂连接配置回调函数
    def reload_ip_port_history(self):
        """获取历史IP和Port填写记录"""
        if self.os_name == "Windows":
            ip_port_info_file = './config/Socket_Info.dat'
        else:
            ip_port_info_file = './config/Socket_Info'
            
        with Path(ip_port_info_file) as socket_file_info:
            if socket_file_info.exists():
                try:
                    socket_info = shelve.open("./config/Socket_Info")
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
        with shelve.open('./config/Socket_Info') as connect_info:
            if all([ip, port]):
                connect_info["target_ip"] = ip
                connect_info["target_port"] = int(port)
                self.message_box.success_message_box(message="配置添加成功!")
            else:
                self.message_box.warning_message_box(message="IP 或 Port 号为空，请重新填写!")

    def reset_ip_port_info(self):
        """重置 IP 和 Port 输入框内容"""
        self.TargetIpEdit.clear()
        self.TargetPortEdit.clear()

    # 机械臂 WiFi AP 模式配置回调函数
    def reload_ap_passwd_history(self):
        """获取历史 WiFi 名称和 Passwd 记录"""
        if self.os_name == "Windows":
            ap_passwd_info_file = './config/WiFi_Info.dat'
        else:
            ap_passwd_info_file = './config/WiFi_Info'
            
        with Path(ap_passwd_info_file) as socket_file_info:
            if socket_file_info.exists():
                try:
                    socket_info = shelve.open("./config/WiFi_Info")
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
        with shelve.open('./config/WiFi_Info') as connect_info:
            if all([ip, port]):
                connect_info["SSID"] = ip
                connect_info["passwd"] = port
                self.message_box.success_message_box(message="WiFi 配置添加成功!")
            else:
                self.message_box.warning_message_box(message="WiFi名称 或密码为空，请重新填写!")

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
    def reset_robot_arm(self):
        """机械臂复位
        :param mode:
        """
        robot_arm_client = self.get_robot_arm_connector()
        with robot_arm_client as rac:
            rac.send(b'{"command":"set_joint_Auto_zero"}\r\n')
            rs_data = json.loads(rac.recv(1024).decode('utf-8').strip()).get("data")
            if rs_data == "true":
                self.message_box.warning_message_box("机械臂复位中!\n请注意手臂姿态")


    def get_angle_value(self):
        """实时获取关节的角度值"""
        with self.get_robot_arm_connector() as rac:
            while not self.loop_flag:
                try:
                    time.sleep(1)
                    rac.sendall(b'{"command":"get_joint_angle_all"}\r\n')  # 获取机械臂角度值 API
                    rs_data = rac.recv(1024).decode('utf-8')
                    rs_data_dict = json.loads(rs_data)
                    
                    # 只获取关节角度的回执
                    if rs_data_dict["return"] == "get_joint_angle_all":
                        print(rs_data_dict)
                        # 实时更新 AngleOneEdit ~ AngleOneSixEdit 标签
                        self.AngleOneEdit.setText(str(round(float(rs_data_dict['data'][0]))))
                        self.AngleTwoEdit.setText(str(round(float(rs_data_dict['data'][1]))))
                        self.AngleThreeEdit.setText(str(round(float(rs_data_dict['data'][2]))))
                        self.AngleFourEdit.setText(str(round(float(rs_data_dict['data'][3]))))
                        self.AngleFiveEdit.setText(str(round(float(rs_data_dict['data'][4]))))
                        self.AngleSixEdit.setText(str(round(float(rs_data_dict['data'][5]))))

                except (UnicodeError, json.decoder.JSONDecodeError) as e:
                    # 等待其他指令完成操作，跳过获取机械臂角度值
                    print(str(e))

    def check_arm_connect_state(self):
        """检查机械臂的连接状态"""
        
        # 初始化步长和速度值
        self.AngleStepEdit.setText(str(5))
        self.ArmSpeedEdit.setText(str(50))
        
        robot_arm_client = self.get_robot_arm_connector()
        with robot_arm_client as rac:
            try:
                remote_address = rac.getpeername()
                self.message_box.success_message_box(message=f"机械臂连接成功！\nIP：{remote_address[0]} \nPort: {remote_address[1]}")
                # 连接没有问题后，运行后台线程
                get_all_angle = Worker(self.get_angle_value)
                self.threadpool.start(get_all_angle)
                
                #  连接成功后，将连接机械臂按钮禁用，避免重复连接
                self.RobotArmLinkButton.setEnabled(False)

            except socket.error as e:
                self.message_box.error_message_box(message="机械臂连接失败！\n请检查设备网络连接状态！")

       
        
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
        old_degrade = int(self.AngleOneEdit.text().strip())
        increase_degrade = int(self.AngleStepEdit.text().strip())
        speed_percentage = int(self.ArmSpeedEdit.text().strip())
        degrade = old_degrade + increase_degrade
        # 每个关节的最大限位值不同
        if 0 <= degrade <= 300:
            self.AngleOneEdit.setText(str(degrade))  # 更新关节角度值

            # 构造发送命令
            command = json.dumps(
                {"command": "set_joint_angle_speed_percentage", "data": [1, degrade, speed_percentage]}) + '\r\n'

            # 发送命令
            robot_arm_client = self.get_robot_arm_connector()
            with robot_arm_client as rc:
                rc.send(command.replace(' ', '').encode())
                response = rc.recv(1024).decode('utf-8').strip()
                self.TeachArmRunLogWindow.append(response)
        else:
            degrade = 300
            self.AngleOneEdit.setText(str(degrade))
            self.message_box.warning_message_box(message="关节 1 最大角度值为 300 度！")

    def arm_one_sub(self):
        """机械臂关节角度减少"""
        old_degrade = int(self.AngleOneEdit.text().strip())
        decrease_degrade = int(self.AngleStepEdit.text().strip())
        speed_percentage = int(self.ArmSpeedEdit.text().strip())
        degrade = old_degrade - decrease_degrade
        if 0 <= degrade <= 300:
            self.AngleOneEdit.setText(str(degrade))
            # 发送命令
            command = json.dumps(
                {"command": "set_joint_angle_speed_percentage", "data": [1, degrade, speed_percentage]}) + '\r\n'
            robot_arm_client = self.get_robot_arm_connector()
            with robot_arm_client as rc:
                rc.send(command.replace(' ', '').encode())
                response = rc.recv(1024).decode('utf-8').strip()
                self.TeachArmRunLogWindow.append(response)
        else:
            self.message_box.warning_message_box(message="关节 1 角度不能为负！")

    def arm_two_add(self):
        """机械臂关节增加"""
        old_degrade = int(self.AngleTwoEdit.text().strip())
        increase_degrade = int(self.AngleStepEdit.text().strip())
        speed_percentage = int(self.ArmSpeedEdit.text().strip())
        degrade = old_degrade + increase_degrade
        self.AngleTwoEdit.setText(str(degrade))  # 更新关节角度值

        # 构造发送命令
        command = json.dumps(
            {"command": "set_joint_angle_speed_percentage", "data": [2, degrade, speed_percentage]}) + '\r\n'

        # 发送命令
        robot_arm_client = self.get_robot_arm_connector()
        with robot_arm_client as rc:
            rc.send(command.replace(' ', '').encode())
            response = rc.recv(1024).decode('utf-8').strip()
            self.TeachArmRunLogWindow.append(response)

    def arm_two_sub(self):
        """机械臂关节角度减少"""
        # 获取机械臂当前的角度(手臂未提供该接口)
        old_degrade = int(self.AngleTwoEdit.text().strip())
        decrease_degrade = int(self.AngleStepEdit.text().strip())
        speed_percentage = int(self.ArmSpeedEdit.text().strip())
        degrade = old_degrade - decrease_degrade
        if 0 <= degrade:
            self.AngleTwoEdit.setText(str(degrade))
            # 发送命令
            command = json.dumps(
                {"command": "set_joint_angle_speed_percentage", "data": [2, degrade, speed_percentage]}) + '\r\n'
            robot_arm_client = self.get_robot_arm_connector()
            with robot_arm_client as rc:
                rc.send(command.replace(' ', '').encode())
                response = rc.recv(1024).decode('utf-8').strip()
                self.TeachArmRunLogWindow.append(response)
        else:
            self.message_box.warning_message_box(message="关节 2 角度不能为负！")

    def arm_three_add(self):
        """机械臂关节增加"""
        old_degrade = int(self.AngleThreeEdit.text().strip())
        increase_degrade = int(self.AngleStepEdit.text().strip())
        speed_percentage = int(self.ArmSpeedEdit.text().strip())
        degrade = old_degrade + increase_degrade
        self.AngleThreeEdit.setText(str(degrade))  # 更新关节角度值

        # 构造发送命令
        command = json.dumps(
            {"command": "set_joint_angle_speed_percentage", "data": [3, degrade, speed_percentage]}) + '\r\n'

        # 发送命令
        robot_arm_client = self.get_robot_arm_connector()
        with robot_arm_client as rc:
            rc.send(command.replace(' ', '').encode())
            response = rc.recv(1024).decode('utf-8').strip()
            self.TeachArmRunLogWindow.append(response)

    def arm_three_sub(self):
        """机械臂关节角度减少"""
        old_degrade = int(self.AngleThreeEdit.text().strip())
        decrease_degrade = int(self.AngleStepEdit.text().strip())
        speed_percentage = int(self.ArmSpeedEdit.text().strip())
        degrade = old_degrade - decrease_degrade
        if 0 <= degrade:
            self.AngleThreeEdit.setText(str(degrade))
            # 发送命令
            command = json.dumps(
                {"command": "set_joint_angle_speed_percentage", "data": [3, degrade, speed_percentage]}) + '\r\n'
            robot_arm_client = self.get_robot_arm_connector()
            with robot_arm_client as rc:
                rc.send(command.replace(' ', '').encode())
                response = rc.recv(1024).decode('utf-8').strip()
                self.TeachArmRunLogWindow.append(response)
        else:
            self.message_box.warning_message_box(message="关节 3 角度不能为负！")

    def arm_four_add(self):
        """机械臂关节增加"""
        old_degrade = int(self.AngleFourEdit.text().strip())
        increase_degrade = int(self.AngleStepEdit.text().strip())
        speed_percentage = int(self.ArmSpeedEdit.text().strip())
        degrade = old_degrade + increase_degrade
        self.AngleFourEdit.setText(str(degrade))  # 更新关节角度值

        # 构造发送命令
        command = json.dumps(
            {"command": "set_joint_angle_speed_percentage", "data": [4, degrade, speed_percentage]}) + '\r\n'

        # 发送命令
        robot_arm_client = self.get_robot_arm_connector()
        with robot_arm_client as rc:
            rc.send(command.replace(' ', '').encode())
            response = rc.recv(1024).decode('utf-8').strip()
            self.TeachArmRunLogWindow.append(response)

    def arm_four_sub(self):
        """机械臂关节角度减少"""
        old_degrade = int(self.AngleFourEdit.text().strip())
        decrease_degrade = int(self.AngleStepEdit.text().strip())
        speed_percentage = int(self.ArmSpeedEdit.text().strip())
        degrade = old_degrade - decrease_degrade
        if 0 <= degrade:
            self.AngleFourEdit.setText(str(degrade))
            # 发送命令
            command = json.dumps(
                {"command": "set_joint_angle_speed_percentage", "data": [4, degrade, speed_percentage]}) + '\r\n'
            robot_arm_client = self.get_robot_arm_connector()
            with robot_arm_client as rc:
                rc.send(command.replace(' ', '').encode())
                response = rc.recv(1024).decode('utf-8').strip()
                self.TeachArmRunLogWindow.append(response)
        else:
            self.message_box.warning_message_box(message="关节 4 角度不能为负！")

    def arm_five_add(self):
        """机械臂关节增加"""
        old_degrade = int(self.AngleFiveEdit.text().strip())
        increase_degrade = int(self.AngleStepEdit.text().strip())
        speed_percentage = int(self.ArmSpeedEdit.text().strip())
        degrade = old_degrade + increase_degrade
        if 0 <= degrade:
            self.AngleFiveEdit.setText(str(degrade))  # 更新关节角度值

        # 构造发送命令
        command = json.dumps(
            {"command": "set_joint_angle_speed_percentage", "data": [5, degrade, speed_percentage]}) + '\r\n'

        # 发送命令
        robot_arm_client = self.get_robot_arm_connector()
        with robot_arm_client as rc:
            rc.send(command.replace(' ', '').encode())
            response = rc.recv(1024).decode('utf-8').strip()
            self.TeachArmRunLogWindow.append(response)

    def arm_five_sub(self):
        """机械臂关节角度减少"""
        old_degrade = int(self.AngleFiveEdit.text().strip())
        decrease_degrade = int(self.AngleStepEdit.text().strip())
        speed_percentage = int(self.ArmSpeedEdit.text().strip())
        degrade = old_degrade - decrease_degrade
        if 0 <= degrade:
            self.AngleFiveEdit.setText(str(degrade))
            # 发送命令
            command = json.dumps(
                {"command": "set_joint_angle_speed_percentage", "data": [5, degrade, speed_percentage]}) + '\r\n'
            robot_arm_client = self.get_robot_arm_connector()
            with robot_arm_client as rc:
                rc.send(command.replace(' ', '').encode())
                response = rc.recv(1024).decode('utf-8').strip()
                self.TeachArmRunLogWindow.append(response)
        else:
            self.message_box.warning_message_box(message="关节 5 角度不能为负！")

    def arm_six_add(self):
        """机械臂关节增加"""
        old_degrade = int(self.AngleSixEdit.text().strip())
        increase_degrade = int(self.AngleStepEdit.text().strip())
        speed_percentage = int(self.ArmSpeedEdit.text().strip())
        degrade = old_degrade + increase_degrade
        self.AngleSixEdit.setText(str(degrade))  # 更新关节角度值

        # 构造发送命令
        command = json.dumps(
            {"command": "set_joint_angle_speed_percentage", "data": [6, degrade, speed_percentage]}) + '\r\n'

        # 发送命令
        robot_arm_client = self.get_robot_arm_connector()
        with robot_arm_client as rc:
            rc.send(command.replace(' ', '').encode())
            response = rc.recv(1024).decode('utf-8').strip()
            self.TeachArmRunLogWindow.append(response)

    def arm_six_sub(self):
        """机械臂关节角度减少"""
        old_degrade = int(self.AngleSixEdit.text().strip())
        decrease_degrade = int(self.AngleStepEdit.text().strip())
        speed_percentage = int(self.ArmSpeedEdit.text().strip())
        degrade = old_degrade - decrease_degrade
        if 0 <= degrade:
            self.AngleSixEdit.setText(str(degrade))
            # 发送命令
            command = json.dumps(
                {"command": "set_joint_angle_speed_percentage", "data": [6, degrade, speed_percentage]}) + '\r\n'
            robot_arm_client = self.get_robot_arm_connector()
            with robot_arm_client as rc:
                rc.send(command.replace(' ', '').encode())
                response = rc.recv(1024).decode('utf-8').strip()
                self.TeachArmRunLogWindow.append(response)
        else:
            self.message_box.warning_message_box(message="关节 6 角度不能为负！")

    def arm_angle_step_add(self):
        """机械臂关节步长增加"""
        old_degrade = int(self.AngleStepEdit.text().strip())
        degrade = old_degrade + 5
        if 0 < degrade <= 20:
            self.AngleStepEdit.setText(str(degrade))
        else:
            self.message_box.warning_message_box(message="步长不能超过 20")

    def arm_angle_step_sub(self):
        """机械臂关节步长减少"""
        old_degrade = int(self.AngleStepEdit.text().strip())
        degrade = old_degrade - 5
        if degrade > 0:
            self.AngleStepEdit.setText(str(degrade))
        else:
            self.message_box.warning_message_box(message="步长不能为负!")

    def arm_speed_percentage_add(self):
        """关节运动速度百分比增加"""
        speed_percentage_edit = self.ArmSpeedEdit.text()
        if speed_percentage_edit is not None and speed_percentage_edit.isdigit():
            old_speed_percentage = int(speed_percentage_edit.strip())
            new_speed_percentage = old_speed_percentage + 5
            if 50 <= new_speed_percentage <= 100:
                self.ArmSpeedEdit.setText(str(new_speed_percentage))
            else:
                self.message_box.warning_message_box(message=f"关节速度范围 50 ~ 100")
        else:
            self.message_box.error_message_box(message="请输入整数字符!")

    def arm_speed_percentage_sub(self):
        """关节运动速度百分比减少"""
        speed_percentage_edit = self.ArmSpeedEdit.text()
        if speed_percentage_edit is not None and speed_percentage_edit.isdigit():
            old_speed_percentage = int(speed_percentage_edit.strip())
            new_speed_percentage = old_speed_percentage - 5
            if new_speed_percentage >= 50:
                self.ArmSpeedEdit.setText(str(new_speed_percentage))
            else:
                self.message_box.warning_message_box(message=f"关节最低速度为 50 ，速度不能为负!")
        else:
            self.message_box.error_message_box(message="请输入整数字符!")

    # 末端工具控制回调函数
    def tool_open(self):
        """吸盘工具开"""
        type_of_tool = self.ArmToolComboBox.currentText()
        if type_of_tool == "吸盘":
            command = json.dumps({"command":"set_robot_io_interface", "data": [0, True]}) + '\r\n'
            robot_arm_client = self.get_robot_arm_connector()
            with robot_arm_client as rc:
                rc.send(command.replace(' ', '').encode())
                response = rc.recv(1024).decode('utf-8').strip()
                self.TeachArmRunLogWindow.append(response)
        else:
            self.message_box.warning_message_box("末端工具未选择吸盘!")

    def tool_close(self):
        """吸盘工具关"""
        type_of_tool = self.ArmToolComboBox.currentText()
        if type_of_tool == "吸盘":
            command = json.dumps({"command":"set_robot_io_interface", "data": [0, False]}) + '\r\n'
            robot_arm_client = self.get_robot_arm_connector()
            with robot_arm_client as rc:
                rc.send(command.replace(' ', '').encode())
                response = rc.recv(1024).decode('utf-8').strip()
                self.TeachArmRunLogWindow.append(response)
        else:
            self.message_box.warning_message_box("末端工具未选择吸盘!")

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
        type_of_tool = self.ArmToolComboBox.currentText()  # 获取末端工具类型

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
            arm_tool_combobox.setCurrentText(type_of_tool)
            self.ActionTableWidget.setCellWidget(row_position, 7, arm_tool_combobox)

            # 开关列添加下拉选择框
            arm_tool_control = QComboBox()
            arm_tool_control.addItems(["", "关", "开"])
            self.ActionTableWidget.setCellWidget(row_position, 8, arm_tool_control)
            
            # 默认延时给 1 s
            self.ActionTableWidget.setItem(row_position, 9, QTableWidgetItem("1"))
        else:
            self.message_box.warning_message_box(message="角度值不能为空!")

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
                    arm_action_delay_time = item.get("延时", "")

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

                    # 延时列
                    self.ActionTableWidget.setItem(row_position, 9, QTableWidgetItem(arm_action_delay_time))
                    
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
                speed_percentage = self.ActionTableWidget.item(row, 6).text()  # 速度列
                arm_tool_widget = self.ActionTableWidget.cellWidget(row, 7)  # 工具列
                arm_tool_control_widget = self.ActionTableWidget.cellWidget(row, 8)  # 开关列
                arm_action_delay_time = self.ActionTableWidget.item(row, 9).text()  # 延时列

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
                    "开关": arm_tool_control_widget,
                    "延时": arm_action_delay_time,
                })

            with open(file_name, "w") as json_file:
                json.dump(data, json_file, indent=4, ensure_ascii=False)

    def tale_action_thread(self):
        for row in range(self.ActionTableWidget.rowCount()):
            delay_time = self.run_action(row)
            self.TeachArmRunLogWindow.append(f"机械臂正在执行第 {row + 1} 个动作")
            time.sleep(delay_time)  # 等待动作执行完成
    
    def run_all_action(self):
        """顺序执行示教动作"""
        self.TeachArmRunLogWindow.append('【顺序执行】开始')
        run_all_action_thread = Worker(self.tale_action_thread)
        self.threadpool.start(run_all_action_thread)
        
    def run_action(self, row):
        """机械臂示执行示教动作

        Args:
            row (QTableWidget): 用户在示教界面，点击选中的行

        Returns:
            delay_time (int): 返回动作的执行耗时
        """
        with self.get_robot_arm_connector() as robot_client:
            angle_1 = int(self.ActionTableWidget.item(row, 0).text())
            angle_2 = int(self.ActionTableWidget.item(row, 1).text())
            angle_3 = int(self.ActionTableWidget.item(row, 2).text())
            angle_4 = int(self.ActionTableWidget.item(row, 3).text())
            angle_5 = int(self.ActionTableWidget.item(row, 4).text())
            angle_6 = int(self.ActionTableWidget.item(row, 5).text())
            speed_percentage = int(self.ActionTableWidget.item(row, 6).text())
            delay_time = float(self.ActionTableWidget.item(row, 9).text())  # 执行动作需要的时间
            
            # 机械臂执行命令
            json_command = {"command": "set_joint_angle_all_time",
                                    "data": [angle_1, angle_2, angle_3, angle_4, angle_5, angle_6, delay_time,
                                            speed_percentage]}
            str_command = json.dumps(json_command).replace(' ', "") + '\r\n'
            robot_client.send(str_command.encode('utf-8'))
        return delay_time

    def run_action_step(self):
        """单次执行选定的动作"""
        # 获取到选定的动作
        selected_row = self.ActionTableWidget.currentRow()
        if selected_row >= 0:
            self.TeachArmRunLogWindow.append("正在执行第 " + str(selected_row + 1) + " 个动作")
            # 启动机械臂动作执行线程
            run_action_step_thread = Worker(self.run_action, selected_row)
            self.threadpool.start(run_action_step_thread)
            
        else:
            self.message_box.warning_message_box("请选择需要执行的动作!")
            

    def run_action_loop(self):
        """循环执行动作"""
        # 获取循环动作循环执行的次数
        if self.ActionLoopTimes.text().isdigit():
            loop_times = int(self.ActionLoopTimes.text().strip()) 
            for _ in range(loop_times):
                self.tale_action_thread()
        else:
            self.message_box.warning_message_box(f"请输入所以动作循环次数[0-9]")
        
        
    def show_context_menu(self, pos):
        """右键复制粘贴菜单"""
        self.context_menu.exec_(self.ActionTableWidget.mapToGlobal(pos))


    def get_robot_arm_connector(self):
        """获取与机械臂的连接对象"""
        try:
            socket_info = shelve.open("./config/Socket_Info")
            host = socket_info['target_ip']
            port = int(socket_info['target_port'])
            robot_arm_client = ClientSocket(host, port)
        except Exception as e:
            print(str(e))
            self.message_box.error_message_box(message="没有读取到 ip 和 port 信息，请前往机械臂配置 ！")
        return robot_arm_client

    def closeEvent(self, event):
        """用户触发窗口关闭事件，所有线程标志位为退出"""
        self.loop_flag = True
        print("窗口关闭！")
        event.accept()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    apply_stylesheet(app, theme='light_blue.xml')
    window.show()
    sys.exit(app.exec_())
