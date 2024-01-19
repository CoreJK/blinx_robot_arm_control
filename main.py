import json
import platform
import shelve
import sys
import time
from pathlib import Path
from functools import partial
from queue import PriorityQueue
from retrying import retry

# 正逆解相关模块
import numpy as np
from math import degrees
from spatialmath import SE3
from spatialmath.base import rpy2tr

# UI 相关模块
from PySide2.QtCore import Qt, QThreadPool
from PySide2.QtWidgets import (QApplication, QComboBox, QFileDialog, QMenu,
                               QTableWidgetItem, QWidget)
from qt_material import apply_stylesheet

# 三方通讯模块
from serial.tools import list_ports

# 导入转换后的 UI 文件
from app.BLinx_Robot_Arm_ui import Ui_Form
from componets.message_box import BlinxMessageBox
from common.socket_client import ClientSocket, Worker

# 机械臂MDH模型
from common.blinx_robot_module import Mirobot
from common.check_tools import check_robot_arm_connection

# 调试 segment 异常时，解除改注释
# import faulthandler;faulthandler.enable()

# 日志模块
from loguru import logger

# 项目根目录
PROJECT_ROOT_PATH = Path(__file__).resolve(strict=True).parent

# 配置文件路径
LOG_FILE_PATH = PROJECT_ROOT_PATH / "logs/record_{time}.log"
IP_PORT_INFO_FILE_PATH = PROJECT_ROOT_PATH / "config/Socket_Info"
WIFI_INFO_FILE_PATH = PROJECT_ROOT_PATH / "config/WiFi_Info"
logger.add(LOG_FILE_PATH, level="INFO")


class MainWindow(QWidget, Ui_Form):
    """机械臂上位机控制窗口"""
    
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("BLinx Robot Arm V1.0")
        
        # 初始化机械臂模型
        self.blinx_robot_arm = Mirobot()
        
        # 角度初始值
        self.q1 = 0.0
        self.q2 = 0.0
        self.q3 = 0.0
        self.q4 = 0.0
        self.q5 = 0.0
        self.q6 = 0.0
        
        # 末端工具坐标初始值
        self.X = 0.238
        self.Y = 0.0
        self.Z = 0.233
        
        # 末端工具姿态初始值
        self.rx = 0.0
        self.ry = -0.0
        self.rz = 0.0
        
        # 获取操作系统的版本信息
        self.os_name = platform.system()
        self.os_version = platform.release()
        
        # 开启 QT 线程池
        self.threadpool = QThreadPool()
        self.command_queue = PriorityQueue()

        # 机械臂的查询循环控制位
        self.loop_flag = False
        self.robot_arm_is_connected = False

        # 初始化消息提示窗口
        self.message_box = BlinxMessageBox(self)
        
        # 示教控制页面回调函数绑定
        self.ActionAddButton.clicked.connect(self.add_item)
        self.ActionDeleteButton.clicked.connect(self.remove_item)
        self.ActionUpdateButton.clicked.connect(self.update_item)
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
        self.AngleOneAddButton.clicked.connect(partial(self.arm_one_control, -140, 140, increase=True))
        self.AngleOneSubButton.clicked.connect(partial(self.arm_one_control, -140, 140, increase=False))
        self.AngleTwoAddButton.clicked.connect(partial(self.arm_two_control, -70, 70, increase=True))
        self.AngleTwoSubButton.clicked.connect(partial(self.arm_two_control, -70, 70, increase=False))
        self.AngleThreeAddButton.clicked.connect(partial(self.arm_three_control, -60, 45, increase=True))
        self.AngleThreeSubButton.clicked.connect(partial(self.arm_three_control, -60, 45, increase=False))
        self.AngleFourAddButton.clicked.connect(partial(self.arm_four_control, -150, 150, increase=True))
        self.AngleFourSubButton.clicked.connect(partial(self.arm_four_control, -150, 150, increase=False))
        self.AngleFiveAddButton.clicked.connect(partial(self.arm_five_control, -180, 10, increase=True))
        self.AngleFiveSubButton.clicked.connect(partial(self.arm_five_control, -180, 10, increase=False))
        self.AngleSixAddButton.clicked.connect(partial(self.arm_six_control, -180, 180, increase=True))
        self.AngleSixSubButton.clicked.connect(partial(self.arm_six_control, -180, 180, increase=False))
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
        self.RobotArmLinkButton.clicked.connect(self.connect_to_robot_arm)

        # 命令控制页面回调函数绑定
        self.CommandSendButton.clicked.connect(self.send_json_command)

        # 复位和急停按钮绑定
        self.RobotArmResetButton.clicked.connect(self.reset_robot_arm)
        # 禁用急停按钮
        self.RobotArmStopButton.setEnabled(False)
        self.RobotArmStopButton.clicked.connect(self.stop_robot_arm)
        
        # 末端工具控制组回调函数绑定
        self.ArmClawOpenButton.clicked.connect(self.tool_open)
        self.ArmClawCloseButton.clicked.connect(self.tool_close)
        
        # 末端工具坐标增减回调函数绑定 
        self.XAxisAddButton.clicked.connect(partial(self.tool_x_operate, action="add"))
        self.XAxisSubButton.clicked.connect(partial(self.tool_x_operate, action="sub"))
        self.YAxisAddButton.clicked.connect(partial(self.tool_y_operate, action="add"))
        self.YAxisSubButton.clicked.connect(partial(self.tool_y_operate, action="sub"))
        self.ZAxisAddButton.clicked.connect(partial(self.tool_z_operate, action="add"))
        self.ZAxisSubButton.clicked.connect(partial(self.tool_z_operate, action="sub"))
        self.CoordinateAddButton.clicked.connect(self.tool_coordinate_step_add)
        self.CoordinateStepSubButton.clicked.connect(self.tool_coordinate_step_sub)
        
        # 末端工具姿态增减回调函数绑定
        self.RxAxisAddButton.clicked.connect(partial(self.tool_rx_operate, action="add"))
        self.RxAxisSubButton.clicked.connect(partial(self.tool_rx_operate, action="sub"))
        self.RyAxisAddButton.clicked.connect(partial(self.tool_ry_operate, action="add"))
        self.RyAxisSubButton.clicked.connect(partial(self.tool_ry_operate, action="sub"))
        self.RzAxisAddButton.clicked.connect(partial(self.tool_rz_operate, action="add"))
        self.RzAxisSubButton.clicked.connect(partial(self.tool_rz_operate, action="sub"))
        self.ApStepAddButton.clicked.connect(self.tool_pose_step_add)
        self.ApStepSubButton.clicked.connect(self.tool_pose_step_sub)
        
    # 机械臂连接配置回调函数
    def reload_ip_port_history(self):
        """获取历史IP和Port填写记录"""
        try:
            socket_info = shelve.open(str(IP_PORT_INFO_FILE_PATH))
            self.TargetIpEdit.setText(socket_info["target_ip"])
            self.TargetPortEdit.setText(str(socket_info["target_port"]))
            socket_info.close()
        except KeyError:
            logger.warning("IP 和 Port 未找到对应记录, 请填写配置信息!")
            self.TargetIpEdit.setText("")
            self.TargetPortEdit.setText("")

    def submit_ip_port_info(self):
        """配置机械臂的通讯IP和端口"""
        ip = self.TargetIpEdit.text().strip()
        port = self.TargetPortEdit.text().strip()
        
        # 保存 IP 和 Port 信息
        if all([ip, port]):
            socket_info = shelve.open(str(IP_PORT_INFO_FILE_PATH))
            socket_info["target_ip"] = ip
            socket_info["target_port"] = int(port)
            self.message_box.success_message_box(message="配置添加成功!")
            socket_info.close()
        else:
            self.message_box.warning_message_box(message="IP 或 Port 号为空，请重新填写!")

    def reset_ip_port_info(self):
        """重置 IP 和 Port 输入框内容"""
        self.TargetIpEdit.clear()
        self.TargetPortEdit.clear()

    # 机械臂 WiFi AP 模式配置回调函数
    def reload_ap_passwd_history(self):
        """获取历史 WiFi 名称和 Passwd 记录"""            
        try:
            wifi_info = shelve.open(str(WIFI_INFO_FILE_PATH))
            self.WiFiSsidEdit.setText(wifi_info["SSID"])
            self.WiFiPasswdEdit.setText(wifi_info["passwd"])
            wifi_info.close()
        except KeyError:
            logger.warning("WiFi 配置未找到历史记录,请填写配置信息!")
            self.WiFiSsidEdit.setText("")
            self.WiFiPasswdEdit.setText("")

    def submit_ap_passwd_info(self):
        """配置机械臂的通讯 WiFi 名称和 passwd"""
        ip = self.WiFiSsidEdit.text().strip()
        port = self.WiFiPasswdEdit.text().strip()
        
        # 保存 IP 和 Port 信息
        if all([ip, port]):
            wifi_info = shelve.open(str(WIFI_INFO_FILE_PATH))
            wifi_info["SSID"] = ip
            wifi_info["passwd"] = port
            wifi_info.close()
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

    # 机械臂复位按钮回调函数
    @check_robot_arm_connection
    def reset_robot_arm(self):
        """机械臂复位
        :param mode:
        """
        self.command_queue.put((1, '{"command":"set_joint_Auto_zero"}\r\n'.encode()))
        self.message_box.warning_message_box("机械臂复位中!\n请注意手臂姿态")
        logger.warning("机械臂复位中!请注意手臂姿态")
    
    # 机械臂急停按钮回调函数
    @check_robot_arm_connection
    def stop_robot_arm(self):
        """机械臂急停"""
        # 线程标志设置为停止
        self.loop_flag = True
        # 清空队列中的命令
        self.command_queue = PriorityQueue()
        # 恢复连接机械臂按钮
        self.RobotArmLinkButton.setText("连接机械臂")
        self.RobotArmLinkButton.setEnabled(True)
        # 禁用急停按钮
        self.RobotArmStopButton.setEnabled(False)
        
        self.message_box.error_message_box("机械臂急停!")
        self.loop_flag = False  # 恢复线程池的初始标志位
        self.robot_arm_is_connected = False # 机械臂连接标志位设置为 False
                            
    @logger.catch
    def get_angle_value(self):
        """实时获取关节的角度值"""        
        while not self.loop_flag:
            time.sleep(1)
            self.command_queue.put((3, '{"command":"get_joint_angle_all"}\r\n'.encode()))
                

    def update_joint_degrees_text(self):
        """更新界面上的角度值, 并返回实时角度值

        Args:
            rs_data_dict (_dict_): 与机械臂通讯获取到的机械臂角度值
        """
        display_q1 = str(round(self.q1, 2))
        display_q2 = str(round(self.q2, 2))
        display_q3 = str(round(self.q3, 2))
        display_q4 = str(round(self.q4, 2))
        display_q5 = str(round(self.q5, 2))
        display_q6 = str(round(self.q6, 2))
        self.AngleOneEdit.setText(display_q1)
        self.AngleTwoEdit.setText(display_q2)
        self.AngleThreeEdit.setText(display_q3)
        self.AngleFourEdit.setText(display_q4)
        self.AngleFiveEdit.setText(display_q5)
        self.AngleSixEdit.setText(display_q6)
        logger.debug(f"显示的角度值: {[display_q1, display_q2, display_q3, display_q4, display_q5, display_q6]}")
    
    def update_arm_pose_text(self):
        """更新界面上机械臂末端工具的坐标和姿态值"""
        self.XAxisEdit.setText(str(round(self.X, 3)))
        self.YAxisEdit.setText(str(round(self.Y, 3)))
        self.ZAxisEdit.setText(str(round(self.Z, 3)))
        self.RxAxisEdit.setText(str(round(self.rx, 3)))
        self.RyAxisEdit.setText(str(round(self.ry, 3)))
        self.RzAxisEdit.setText(str(round(self.rz, 3)))
    
    @logger.catch
    def connect_to_robot_arm(self):
        """连接机械臂"""
        
        # 初始化步长和速度值
        self.AngleStepEdit.setText(str(5))
        self.ArmSpeedEdit.setText(str(50))
        
        try:
            # 检查网络连接状态
            robot_arm_client = self.get_robot_arm_connector()
            with robot_arm_client as rac:
                remote_address = rac.getpeername()
                logger.info("机械臂连接成功!")
                self.message_box.success_message_box(message=f"机械臂连接成功！\nIP：{remote_address[0]} \nPort: {remote_address[1]}")
                
            if self.RobotArmLinkButton.isEnabled() and remote_address:
                # 机械臂连接成功标志
                self.RobotArmLinkButton.setText("已连接")
                self.robot_arm_is_connected = True
                # 连接成功后，将连接机械臂按钮禁用，避免用户操作重复发起连接
                self.RobotArmLinkButton.setEnabled(False)
                # 启用急停按钮
                self.RobotArmStopButton.setEnabled(True)
                
                # 启用实时获取机械臂角度线程
                get_all_angle = Worker(self.get_angle_value)
                self.threadpool.start(get_all_angle)
                logger.info("开始后台获取机械臂角度")
                
                # 启用轮询队列中所有命令的线程
                command_sender_thread = Worker(self.command_sender)
                self.threadpool.start(command_sender_thread)
                logger.info("开启命令发送线程")
                logger.warning("禁用连接机械臂按钮!")
                
        except Exception as e:
            # 连接失败后，将连接机械臂按钮启用
            self.RobotArmLinkButton.setEnabled(True)
            # 清空队列
            self.command_queue = PriorityQueue(maxsize=100)
            # 关闭线程池
            self.loop_flag = True
            # 弹出错误提示框
            logger.error(f"机械臂连接失败: {e}")
            self.message_box.error_message_box(message="机械臂连接失败！\n请检查设备网络连接状态！")
            # 恢复线程池的初始标志位
            self.loop_flag = False
            
            
    # 命令控制页面 json 发送与调试
    @check_robot_arm_connection
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
    
    
    def command_sender(self):
        """后台获取命令池命令，并发送的线程"""
        with self.get_robot_arm_connector() as con:
            while not self.loop_flag:
                if not self.command_queue.empty():
                    try:
                        command_str = self.command_queue.get()
                        
                        # 发送命令
                        con.send(command_str[1])
                        logger.debug(f"发送命令：{command_str[1].decode().strip()}")
                        
                        # 接收命令返回的信息
                        response = json.loads(con.recv(1024).decode('utf-8').strip())
                        logger.debug(f"返回信息: {response}")
                        
                        # todo 命令返回的信息放入另外一个队列
                        # 解析机械臂角度获取返回的信息
                        if response["return"] == "get_joint_angle_all":
                            angle_data_list = response['data']
                            self.q1, self.q2, self.q3, self.q4, self.q5, self.q6 = angle_data_list
                            # 实时更新 AngleOneEdit ~ AngleOneSixEdit 标签的角度值
                            self.update_joint_degrees_text()
                            
                            # 计算并更新机械臂的正运动解
                            arm_joint_radians = np.radians(angle_data_list)
                            translation_vector = self.blinx_robot_arm.fkine(arm_joint_radians)
                            self.X, self.Y, self.Z = translation_vector.t  # 末端坐标
                            self.rz, self.ry, self.rx = translation_vector.rpy(unit='deg')  # 末端姿态
                            self.update_arm_pose_text()
                            
                    except Exception as e:
                        logger.error(f"发送命令失败: {e}")
                        self.message_box.error_message_box(message="发送命令失败!")
                        self.command_queue = PriorityQueue(maxsize=100)

                
    # 机械臂关节控制回调函数
    @check_robot_arm_connection
    def arm_one_control(self, min_degrade=-140, max_degrade=140, increase=True):
        """机械臂关节控制"""
        old_degrade = self.q1
        step_degrade = float(self.AngleStepEdit.text().strip())
        speed_percentage = float(self.ArmSpeedEdit.text().strip())

        if increase:
            degrade = old_degrade + step_degrade
        else:
            degrade = old_degrade - step_degrade

        if degrade < min_degrade or degrade > max_degrade:
            self.message_box.error_message_box(message=f"关节角度超出范围: {min_degrade} ~ {max_degrade}")
        else:
            # 使用线性回归方程限制关节角度
            degrade = np.clip(degrade, min_degrade, max_degrade)

            # 构造发送命令
            command = json.dumps(
                {"command": "set_joint_angle_speed_percentage", "data": [1, degrade, speed_percentage]}) + '\r\n'
            self.command_queue.put((1.5, command.encode()))

    @check_robot_arm_connection
    def arm_two_control(self, min_degrade=-70, max_degrade=70, increase=True):
        """机械臂关节控制"""
        old_degrade = self.q2
        step_degrade = float(self.AngleStepEdit.text().strip())
        speed_percentage = float(self.ArmSpeedEdit.text().strip())

        if increase:
            degrade = old_degrade + step_degrade
        else:
            degrade = old_degrade - step_degrade

        self.AngleTwoEdit.setText(str(degrade))  # 更新关节角度值

        if degrade < min_degrade or degrade > max_degrade:
            self.message_box.error_message_box(message=f"关节角度超出范围: {min_degrade} ~ {max_degrade}")
        else:
            # 使用线性回归方程限制关节角度
            degrade = np.clip(degrade, min_degrade, max_degrade)

            # 构造发送命令
            command = json.dumps(
                {"command": "set_joint_angle_speed_percentage", "data": [2, degrade, speed_percentage]}) + '\r\n'
            self.command_queue.put((1.5, command.encode()))
    
    @check_robot_arm_connection
    def arm_three_control(self, min_degrade=-60, max_degrade=45, increase=True):
        """机械臂关节控制"""
        old_degrade = self.q3
        step_degrade = float(self.AngleStepEdit.text().strip())
        speed_percentage = float(self.ArmSpeedEdit.text().strip())

        if increase:
            degrade = old_degrade + step_degrade
        else:
            degrade = old_degrade - step_degrade

        self.AngleThreeEdit.setText(str(degrade))  # 更新关节角度值

        if degrade < min_degrade or degrade > max_degrade:
            self.message_box.error_message_box(message=f"关节角度超出范围: {min_degrade} ~ {max_degrade}")
        else:
            # 使用线性回归方程限制关节角度
            degrade = np.clip(degrade, min_degrade, max_degrade)

            # 构造发送命令
            command = json.dumps(
                {"command": "set_joint_angle_speed_percentage", "data": [3, degrade, speed_percentage]}) + '\r\n'
            self.command_queue.put((1.5, command.encode()))

    @check_robot_arm_connection
    def arm_four_control(self, min_degrade=-150, max_degrade=150, increase=True):
        """机械臂关节控制"""
        old_degrade = self.q4
        step_degrade = float(self.AngleStepEdit.text().strip())
        speed_percentage = float(self.ArmSpeedEdit.text().strip())

        if increase:
            degrade = old_degrade + step_degrade
        else:
            degrade = old_degrade - step_degrade

        self.AngleFourEdit.setText(str(degrade))  # 更新关节角度值

        if degrade < min_degrade or degrade > max_degrade:
            self.message_box.error_message_box(message=f"关节角度超出范围: {min_degrade} ~ {max_degrade}")
        else:
            # 使用线性回归方程限制关节角度
            degrade = np.clip(degrade, min_degrade, max_degrade)

            # 构造发送命令
            command = json.dumps(
                {"command": "set_joint_angle_speed_percentage", "data": [4, degrade, speed_percentage]}) + '\r\n'
            self.command_queue.put((1.5, command.encode()))

    @check_robot_arm_connection
    def arm_five_control(self, min_degrade=-180, max_degrade=10, increase=True):
        """机械臂关节控制"""
        old_degrade = self.q5
        step_degrade = float(self.AngleStepEdit.text().strip())
        speed_percentage = float(self.ArmSpeedEdit.text().strip())

        if increase:
            degrade = old_degrade + step_degrade
        else:
            degrade = old_degrade - step_degrade

        self.AngleFiveEdit.setText(str(degrade))  # 更新关节角度值

        if degrade < min_degrade or degrade > max_degrade:
            self.message_box.error_message_box(message=f"关节角度超出范围: {min_degrade} ~ {max_degrade}")
        else:
            # 使用线性回归方程限制关节角度
            degrade = np.clip(degrade, min_degrade, max_degrade)

            # 构造发送命令
            command = json.dumps(
                {"command": "set_joint_angle_speed_percentage", "data": [5, degrade, speed_percentage]}) + '\r\n'
            self.command_queue.put((1.5, command.encode()))

    @check_robot_arm_connection
    def arm_six_control(self, min_degrade=-180, max_degrade=180, increase=True):
        """机械臂关节控制"""
        old_degrade = self.q6
        step_degrade = float(self.AngleStepEdit.text().strip())
        speed_percentage = float(self.ArmSpeedEdit.text().strip())

        if increase:
            degrade = old_degrade + step_degrade
        else:
            degrade = old_degrade - step_degrade

        self.AngleSixEdit.setText(str(degrade))  # 更新关节角度值

        if degrade < min_degrade or degrade > max_degrade:
            self.message_box.error_message_box(message=f"关节角度超出范围: {min_degrade} ~ {max_degrade}")
        else:
            # 使用线性回归方程限制关节角度
            degrade = np.clip(degrade, min_degrade, max_degrade)

            # 构造发送命令
            command = json.dumps(
                {"command": "set_joint_angle_speed_percentage", "data": [6, degrade, speed_percentage]}) + '\r\n'
            self.command_queue.put((1.5, command.encode()))
        

    @check_robot_arm_connection
    def arm_angle_step_add(self):
        """机械臂关节步长增加"""
        old_degrade = int(self.AngleStepEdit.text().strip())
        degrade = old_degrade + 5
        if 0 < degrade <= 20:
            self.AngleStepEdit.setText(str(degrade))
        else:
            self.message_box.warning_message_box(message="步长不能超过 20")
    
    @check_robot_arm_connection
    def arm_angle_step_sub(self):
        """机械臂关节步长减少"""
        old_degrade = int(self.AngleStepEdit.text().strip())
        degrade = old_degrade - 5
        if degrade > 0:
            self.AngleStepEdit.setText(str(degrade))
        else:
            self.message_box.warning_message_box(message="步长不能为负!")
    
    @check_robot_arm_connection
    def arm_speed_percentage_add(self):
        """关节运动速度百分比增加"""
        speed_percentage_edit = self.ArmSpeedEdit.text()
        if speed_percentage_edit is not None and speed_percentage_edit.isdigit():
            old_speed_percentage = int(speed_percentage_edit.strip())
            new_speed_percentage = old_speed_percentage + 5
            if 0 <= new_speed_percentage <= 100:
                self.ArmSpeedEdit.setText(str(new_speed_percentage))
            else:
                self.message_box.warning_message_box(message=f"关节速度范围 50 ~ 100")
        else:
            self.message_box.error_message_box(message="请输入整数字符!")
    
    @check_robot_arm_connection
    def arm_speed_percentage_sub(self):
        """关节运动速度百分比减少"""
        speed_percentage_edit = self.ArmSpeedEdit.text()
        if speed_percentage_edit is not None and speed_percentage_edit.isdigit():
            old_speed_percentage = int(speed_percentage_edit.strip())
            new_speed_percentage = old_speed_percentage - 5
            if new_speed_percentage >= 0:
                self.ArmSpeedEdit.setText(str(new_speed_percentage))
            else:
                self.message_box.warning_message_box(message=f"速度不能为负!")
        else:
            self.message_box.error_message_box(message="请输入整数字符!")

    # 末端工具控制回调函数
    @check_robot_arm_connection
    def tool_open(self):
        """吸盘工具开"""
        type_of_tool = self.ArmToolComboBox.currentText()
        if type_of_tool == "吸盘":
            command = json.dumps({"command":"set_robot_io_interface", "data": [0, True]}) + '\r\n'
            self.command_queue.put((1, command.encode()))
        else:
            self.message_box.warning_message_box("末端工具未选择吸盘!")

    @check_robot_arm_connection
    def tool_close(self):
        """吸盘工具关"""
        type_of_tool = self.ArmToolComboBox.currentText()
        if type_of_tool == "吸盘":
            command = json.dumps({"command":"set_robot_io_interface", "data": [0, False]}) + '\r\n'
            self.command_queue.put((1, command.encode()))
        else:
            self.message_box.warning_message_box("末端工具未选择吸盘!")

    @check_robot_arm_connection
    def tool_x_operate(self, action="add"):
        """末端工具坐标 x 增减函数"""
        # 获取末端工具的坐标
        old_x_coordinate = self.X
        y_coordinate = self.Y
        z_coordinate = self.Z
        
        # 获取末端工具的姿态
        rx_pose = self.rx
        ry_pose = self.ry
        rz_pose = self.rz
        
        change_value = round(float(self.CoordinateStepEdit.text().strip()), 3)  # 步长值
        speed_percentage = round(float(self.ArmSpeedEdit.text().strip()), 3)  # 速度值
        
        # 根据按钮加减增减数值
        if action == "add":
            new_x_coordinate = old_x_coordinate + change_value
            self.XAxisEdit.setText(str(new_x_coordinate))  # 更新末端工具坐标 X
            
        else:
            new_x_coordinate = old_x_coordinate - change_value
            self.XAxisEdit.setText(str(new_x_coordinate))  
        
        # 通过逆解算出机械臂各个关节角度值
        R_T = SE3([new_x_coordinate, y_coordinate, z_coordinate]) * rpy2tr([rz_pose, ry_pose, rx_pose], unit='deg')
        sol = self.blinx_robot_arm.ikine_LM(R_T, joint_limits=True)
        degrade = [round(degrees(d), 2) for d in sol.q]
        degrade.extend([0, speed_percentage])
        
        # 构造发送命令
        command = json.dumps({"command": "set_joint_angle_all_time", "data": degrade}).replace(' ', "") + '\r\n'
        self.command_queue.put((2, command.encode('utf-8')))
        
    @check_robot_arm_connection
    def tool_y_operate(self, action="add"):
        """末端工具坐标 y 增减函数"""
       # 获取末端工具的坐标
        x_coordinate = self.X
        old_y_coordinate = self.Y
        z_coordinate = self.Z
        
        # 获取末端工具的姿态
        rx_pose = self.rx
        ry_pose = self.ry
        rz_pose = self.rz
        
        change_value = round(float(self.CoordinateStepEdit.text().strip()), 2)  # 步长值
        speed_percentage = round(float(self.ArmSpeedEdit.text().strip()), 2)  # 速度值
        
        # 根据按钮加减增减数值
        if action == "add":
            new_y_coordinate = old_y_coordinate + change_value
            self.YAxisEdit.setText(str(new_y_coordinate))  # 更新末端工具坐标 Y
            
        else:
            new_y_coordinate = old_y_coordinate - change_value
            self.YAxisEdit.setText(str(new_y_coordinate))  
        
        # 通过逆解算出机械臂各个关节角度值
        R_T = SE3([x_coordinate, new_y_coordinate, z_coordinate]) * rpy2tr([rz_pose, ry_pose, rx_pose], unit='deg')
        sol = self.blinx_robot_arm.ikine_LM(R_T, joint_limits=True)
        degrade = [round(degrees(d), 2) for d in sol.q]
        degrade.extend([0, speed_percentage])
        
        # 构造发送命令
        command = json.dumps({"command": "set_joint_angle_all_time", "data": degrade}).replace(' ', "") + '\r\n'

        # 发送命令
        self.command_queue.put((2, command.encode()))

    @check_robot_arm_connection
    def tool_z_operate(self, action="add"):
        """末端工具坐标 z 增减函数"""
        # 获取末端工具的坐标
        x_coordinate = self.X
        y_coordinate = self.Y
        old_z_coordinate = self.Z
        
        # 获取末端工具的姿态
        rx_pose = self.rx
        ry_pose = self.ry
        rz_pose = self.rz
        
        change_value = round(float(self.CoordinateStepEdit.text().strip()), 2)  # 步长值
        speed_percentage = round(float(self.ArmSpeedEdit.text().strip()), 2)  # 速度值
        
        # 根据按钮加减增减数值
        if action == "add":
            new_z_coordinate = old_z_coordinate + change_value
            self.ZAxisEdit.setText(str(new_z_coordinate))  # 更新末端工具坐标 Z
            
        else:
            new_z_coordinate = old_z_coordinate - change_value
            self.ZAxisEdit.setText(str(new_z_coordinate))  
        
        # 通过逆解算出机械臂各个关节角度值
        R_T = SE3([x_coordinate, y_coordinate, new_z_coordinate]) * rpy2tr([rz_pose, ry_pose, rx_pose], unit='deg')
        sol = self.blinx_robot_arm.ikine_LM(R_T, joint_limits=True)
        degrade = [round(degrees(d), 2) for d in sol.q]
        degrade.extend([0, speed_percentage])
        
        # 构造发送命令
        command = json.dumps(
                {"command": "set_joint_angle_all_time", "data": degrade}).replace(' ', "") + '\r\n'

        # 发送命令
        self.command_queue.put((2, command.encode()))

    @check_robot_arm_connection
    def tool_coordinate_step_add(self):
        """末端工具坐标步长增加"""
        # 获取末端工具 edit 的值
        old_coordiante_step = round(float(self.CoordinateStepEdit.text().strip()), 2)
        now_coordiante_step = round(old_coordiante_step + 0.01, 2)
        # 更新末端工具坐标步长值
        self.CoordinateStepEdit.setText(str(now_coordiante_step))
    
    @check_robot_arm_connection
    def tool_coordinate_step_sub(self):
        """末端工具坐标步长减少"""
        # 获取末端工具 edit 的值
        old_coordiante_step = round(float(self.CoordinateStepEdit.text().strip()), 2)
        new_coordiante_step = round(old_coordiante_step - 0.01, 2)
        # 更新末端工具坐标步长值
        self.CoordinateStepEdit.setText(str(new_coordiante_step))
    
    @check_robot_arm_connection
    def tool_rx_operate(self, action="add"):
        """末端工具坐标 Rx 增减函数"""
        # 获取末端工具的坐标
        x_coordinate = round(float(self.XAxisEdit.text().strip()), 2)
        y_coordinate = round(float(self.YAxisEdit.text().strip()), 2)
        z_coordinate = round(float(self.ZAxisEdit.text().strip()), 2)
        old_rx_pose = round(float(self.RxAxisEdit.text().strip()), 2)
        
        # 获取末端工具的姿态
        ry_pose = round(float(self.RyAxisEdit.text().strip()), 2)
        rz_pose = round(float(self.RzAxisEdit.text().strip()), 2)
        
        change_value = round(float(self.ApStepEdit.text().strip()), 2)  # 步长值
        speed_percentage = round(float(self.ArmSpeedEdit.text().strip()), 2)  # 速度值
        
        # 根据按钮加减增减数值
        if action == "add":
            new_rx_pose = old_rx_pose + change_value
            self.RxAxisEdit.setText(str(new_rx_pose))  # 更新末端工具姿态 Rx
        else:
            new_rx_pose = old_rx_pose - change_value
            self.RxAxisEdit.setText(str(new_rx_pose))  # 更新末端工具姿态 Rx
            
        # 根据增减后的位姿数值，逆解出机械臂关节的角度并发送命令
        R_T = SE3([x_coordinate, y_coordinate, z_coordinate]) * rpy2tr([rz_pose, ry_pose, new_rx_pose], unit='deg')
        sol = self.blinx_robot_arm.ikine_LM(R_T, joint_limits=True)
        degrade = [round(degrees(d), 2) for d in sol.q]
        
        # 更新关节控制界面中的角度值
        degrade.extend([0, speed_percentage])
        
        # 构造发送命令
        command = json.dumps({"command": "set_joint_angle_all_time", "data": degrade}).replace(' ', "") + '\r\n'

        # 发送命令
        self.command_queue.put((2, command.encode()))
    
    @check_robot_arm_connection           
    def tool_ry_operate(self, action="add"):
        """末端工具坐标 Ry 增减函数"""
        # 获取末端工具的坐标
        x_coordinate = round(float(self.XAxisEdit.text().strip()), 2)
        y_coordinate = round(float(self.YAxisEdit.text().strip()), 2)
        z_coordinate = round(float(self.ZAxisEdit.text().strip()), 2)
        
        # 获取末端工具的姿态
        rx_pose = round(float(self.RxAxisEdit.text().strip()), 2)
        old_ry_pose = round(float(self.RyAxisEdit.text().strip()), 2)
        rz_pose = round(float(self.RzAxisEdit.text().strip()), 2)
        
        change_value = round(float(self.ApStepEdit.text().strip()), 2)  # 步长值
        speed_percentage = round(float(self.ArmSpeedEdit.text().strip()), 2)  # 速度值
        
        # 根据按钮加减增减数值
        if action == "add":
            new_ry_pose = old_ry_pose + change_value
            self.RyAxisEdit.setText(str(new_ry_pose))  # 更新末端工具姿态 Ry
        else:
            new_ry_pose = old_ry_pose - change_value
            self.RyAxisEdit.setText(str(new_ry_pose))  # 更新末端工具姿态 Ry
            
        # 根据增减后的位姿数值，逆解出机械臂关节的角度并发送命令
        R_T = SE3([x_coordinate, y_coordinate, z_coordinate]) * rpy2tr([rz_pose, new_ry_pose, rx_pose], unit='deg')
        sol = self.blinx_robot_arm.ikine_LM(R_T, joint_limits=True)
        degrade = [round(degrees(d), 2) for d in sol.q]
        
        # 更新关节控制界面中的角度值
        degrade.extend([0, speed_percentage])
        
        # 构造发送命令
        command = json.dumps(
                {"command": "set_joint_angle_all_time", "data": degrade}).replace(' ', "") + '\r\n'

        # 发送命令
        self.command_queue.put((2, command.encode()))
    
    @check_robot_arm_connection    
    def tool_rz_operate(self, action="add"):
        """末端工具坐标 Rz 增减函数"""
        # 获取末端工具的坐标、姿态数值
        x_coordinate = round(float(self.XAxisEdit.text().strip()), 2)
        y_coordinate = round(float(self.YAxisEdit.text().strip()), 2)
        z_coordinate = round(float(self.ZAxisEdit.text().strip()), 2)
        
        # 获取末端工具的姿态
        rx_pose = round(float(self.RxAxisEdit.text().strip()), 2)
        ry_pose = round(float(self.RyAxisEdit.text().strip()), 2)
        old_rz_pose = round(float(self.RzAxisEdit.text().strip()), 2)
        
        change_value = round(float(self.ApStepEdit.text().strip()), 2)  # 步长值
        speed_percentage = round(float(self.ArmSpeedEdit.text().strip()), 2)  # 速度值
        
        # 根据按钮加减增减数值
        if action == "add":
            new_rz_pose = old_rz_pose + change_value
            self.RzAxisEdit.setText(str(new_rz_pose))  # 更新末端工具姿态 Rz
        else:
            new_rz_pose = old_rz_pose - change_value
            self.RzAxisEdit.setText(str(new_rz_pose))  # 更新末端工具姿态 Rz
            
        # 根据增减后的位姿数值，逆解出机械臂关节的角度并发送命令
        R_T = SE3([x_coordinate, y_coordinate, z_coordinate]) * rpy2tr([new_rz_pose, ry_pose, rx_pose], unit='deg')
        sol = self.blinx_robot_arm.ikine_LM(R_T, joint_limits=True)
        degrade = [round(degrees(d), 2) for d in sol.q]
        
        # 更新完关节角度值后，发送命令
        degrade.extend([0, speed_percentage])
        
        # 构造发送命令
        command = json.dumps(
                {"command": "set_joint_angle_all_time", "data": degrade}).replace(' ', "") + '\r\n'

        # 发送命令
        self.command_queue.put((2, command.encode()))
    
    @check_robot_arm_connection
    def tool_pose_step_add(self):
        """末端工具姿态步长增加"""
        # 获取末端工具姿态步长值
        old_pose_step = round(float(self.ApStepEdit.text().strip()), 2)
        new_poset_step = round(old_pose_step + 1, 2)
        # 更新末端工具姿态步长值
        self.ApStepEdit.setText(str(new_poset_step))
    
    @check_robot_arm_connection
    def tool_pose_step_sub(self):
        """末端工具姿态步长减少"""
        # 校验末端工具姿态步长值，必须为数字
        old_pose_step = round(float(self.ApStepEdit.text().strip()), 2)
        new_poset_step = round(old_pose_step - 1, 2)
        # 更新末端工具姿态步长值
        self.ApStepEdit.setText(str(new_poset_step))
    
    # 示教控制回调函数编写
    @check_robot_arm_connection
    def add_item(self):
        """示教控制添加一行动作"""
        speed_percentage = self.ArmSpeedEdit.text()  # 速度值，暂定百分比
        type_of_tool = self.ArmToolComboBox.currentText()  # 获取末端工具类型
        
        row_position = self.ActionTableWidget.rowCount()
        self.ActionTableWidget.insertRow(row_position)
        self.ActionTableWidget.setItem(row_position, 0, QTableWidgetItem(str(round(self.q1, 2))))
        self.ActionTableWidget.setItem(row_position, 1, QTableWidgetItem(str(round(self.q2, 2))))
        self.ActionTableWidget.setItem(row_position, 2, QTableWidgetItem(str(round(self.q3, 2))))
        self.ActionTableWidget.setItem(row_position, 3, QTableWidgetItem(str(round(self.q4, 2))))
        self.ActionTableWidget.setItem(row_position, 4, QTableWidgetItem(str(round(self.q5, 2))))
        self.ActionTableWidget.setItem(row_position, 5, QTableWidgetItem(str(round(self.q6, 2))))
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
        

    @check_robot_arm_connection
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

    @check_robot_arm_connection
    def update_item(self):
        """示教控制更新指定行的动作"""
        selected_rows = self.ActionTableWidget.selectionModel().selectedRows()
        if selected_rows:
            for row in selected_rows:
                for col in range(self.ActionTableWidget.columnCount()):
                    if col == 0:
                        self.ActionTableWidget.setItem(row.row(), col, QTableWidgetItem(str(round(self.q1, 2))))
                    elif col == 1:
                        self.ActionTableWidget.setItem(row.row(), col, QTableWidgetItem(str(round(self.q2, 2))))
                    elif col == 2:
                        self.ActionTableWidget.setItem(row.row(), col, QTableWidgetItem(str(round(self.q3, 2))))
                    elif col == 3:
                        self.ActionTableWidget.setItem(row.row(), col, QTableWidgetItem(str(round(self.q4, 2))))
                    elif col == 4:
                        self.ActionTableWidget.setItem(row.row(), col, QTableWidgetItem(str(round(self.q5, 2))))
                    elif col == 5:
                        self.ActionTableWidget.setItem(row.row(), col, QTableWidgetItem(str(round(self.q6, 2))))
                    elif col == 6:
                        self.ActionTableWidget.setItem(row.row(), col, QTableWidgetItem(str(self.ArmSpeedEdit.text())))
                    elif col == 7:
                        # 更新工具列
                        arm_tool_combobox = QComboBox()
                        arm_tool_combobox.setModel(self.ArmToolOptions)
                        arm_tool_combobox.setCurrentText(self.ArmToolComboBox.currentText())
                        self.ActionTableWidget.setCellWidget(row.row(), col, arm_tool_combobox)
                    elif col == 8:
                        # 更新开关列
                        arm_tool_control = QComboBox()
                        arm_tool_control.addItems(["", "关", "开"])
                        self.ActionTableWidget.setCellWidget(row.row(), col, arm_tool_control)
                
    
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
        logger.info(f"开始导入 {file_name} 动作文件")
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
        logger.info("导入动作文件成功!")  
                    
    def export_data(self):
        """导出动作"""
        options = QFileDialog.Options()
        file_name, _ = QFileDialog.getSaveFileName(self, "Save Data to JSON", "", "JSON Files (*.json);;All Files (*)",
                                                   options=options)
        logger.info("开始导出动作文件")
        logger.debug(f"导出的配置文件的路径 {file_name}")
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
                logger.info("导出配置文件成功!")

    def tale_action_thread(self):
        for row in range(self.ActionTableWidget.rowCount()):
            delay_time = self.run_action(row)
            self.TeachArmRunLogWindow.append(f"机械臂正在执行第 {row + 1} 个动作")
            time.sleep(delay_time)  # 等待动作执行完成
    
    @check_robot_arm_connection
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
        angle_1 = float(self.ActionTableWidget.item(row, 0).text())
        angle_2 = float(self.ActionTableWidget.item(row, 1).text())
        angle_3 = float(self.ActionTableWidget.item(row, 2).text())
        angle_4 = float(self.ActionTableWidget.item(row, 3).text())
        angle_5 = float(self.ActionTableWidget.item(row, 4).text())
        angle_6 = float(self.ActionTableWidget.item(row, 5).text())
        speed_percentage = float(self.ActionTableWidget.item(row, 6).text())
        type_of_tool = self.ActionTableWidget.cellWidget(row, 7).currentText()
        tool_switch = self.ActionTableWidget.cellWidget(row, 8).currentText()
        delay_time = float(self.ActionTableWidget.item(row, 9).text())  # 执行动作需要的时间
        
        # 机械臂执行命令
        json_command = {"command": "set_joint_angle_all_time",
                                "data": [angle_1, angle_2, angle_3, angle_4, angle_5, angle_6, 0,
                                        speed_percentage]}
        str_command = json.dumps(json_command).replace(' ', "") + '\r\n'
        self.command_queue.put((2, str_command.encode()))
        
        # 末端工具动作
        logger.info("单次执行，开关控制")
        if type_of_tool == "吸盘":
            tool_status = True if tool_switch == "开" else False
            json_command = {"command":"set_robot_io_interface", "data": [0, tool_status]}
            str_command = json.dumps(json_command).replace(' ', "") + '\r\n'
            self.command_queue.put((1, str_command.encode()))
                    
        return delay_time

    @check_robot_arm_connection
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

    @check_robot_arm_connection
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

    @retry(stop_max_attempt_number=3, wait_fixed=1000)
    @logger.catch
    def get_robot_arm_connector(self):
        """获取与机械臂的连接对象"""
        try:
            socket_info = shelve.open(str(IP_PORT_INFO_FILE_PATH))
            host = socket_info['target_ip']
            port = int(socket_info['target_port'])
            robot_arm_client = ClientSocket(host, port)
            socket_info.close()
        except Exception as e:
            logger.error(str(e))
            self.message_box.error_message_box(message="没有读取到 ip 和 port 信息，请前往机械臂配置 !")
        return robot_arm_client

    def closeEvent(self, event):
        """用户触发窗口关闭事件，所有线程标志位为退出"""
        self.loop_flag = True
        logger.info("比邻星六轴机械臂上位机窗口关闭！")
        event.accept()



if __name__ == '__main__':
    logger.info("欢迎使用比邻星六轴机械臂!")
    app = QApplication(sys.argv)
    window = MainWindow()
    apply_stylesheet(app, theme='light_blue.xml')
    window.show()
    logger.warning("系统初始化完成, 请在【连接配置】中填写机械臂连接配置信息后开始使用!")
    sys.exit(app.exec_())
