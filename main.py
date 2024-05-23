# -*- coding:utf-8 -*-
import sys
import simplejson as json
import shelve
import sys
import time
from decimal import Decimal
from functools import partial
from queue import Queue
from pubsub import pub

import common.settings as settings
from common.blinx_robot_module import Mirobot
from common.check_tools import check_robot_arm_connection
from common.socket_client import ClientSocket, Worker
from common.work_threads import UpdateJointAnglesTask, AgnleDegreeWatchTask, CommandSenderTask, CommandReceiverTask

# UI 相关模块
from PySide6.QtCore import Qt, QThreadPool, QTimer, Slot, QUrl, QRegularExpression
from PySide6.QtGui import QDesktopServices, QIcon, QRegularExpressionValidator
from PySide6.QtWidgets import (QApplication, QFrame, QMenu, QTableWidgetItem, QFileDialog)
from qfluentwidgets import (MSFluentWindow, CardWidget, ComboBox, 
                            NavigationItemPosition, MessageBox, setThemeColor, InfoBar, InfoBarPosition)
from qfluentwidgets import FluentIcon as FIF

# 导入子页面控件布局文件
from app.command_page import command_page_frame
from app.teach_page import teach_page_frame
from app.connect_page import connect_page_frame
from componets.message_box import BlinxMessageBox

# 正逆解相关模块
import numpy as np
from math import degrees
from spatialmath import SE3
from spatialmath.base import rpy2tr

# 日志模块
from loguru import logger
logger.add(settings.LOG_FILE_PATH, level="DEBUG", rotation="1 MB", retention="7 days")

# 三方通讯模块
from serial.tools import list_ports

# 遇到异常退出时，解除注释下面的代码，查看异常信息
import faulthandler;faulthandler.enable()


class CommandPage(QFrame, command_page_frame):
    """命令控制页面"""
    def __init__(self, page_name: str):
        super().__init__()
        self.setupUi(self)
        self.setObjectName(page_name.replace(' ', '-'))
        self.initButtonIcon()
        self.robot_arm_is_connected = False
        self.initGetRobotArmStatusTask()
        self.message_box = BlinxMessageBox(self)
        self.CommandSendButton.clicked.connect(self.send_json_command)
        
    def initButtonIcon(self):
        """初始化按钮图标"""
        self.CommandSendButton.setIcon(FIF.SEND)
        self.CommandSendButton.setText('发送')

    def initGetRobotArmStatusTask(self):
        """初始化获取机械臂连接状态定时器"""
        logger.warning("获取机械臂连接状态定时器，启动!")
        self.get_robot_arm_status_timer = QTimer()
        self.get_robot_arm_status_timer.timeout.connect(self.get_robot_arm_connect_status)
        self.get_robot_arm_status_timer.start(100)
        
    @check_robot_arm_connection
    @Slot()
    def send_json_command(self):
        """json数据发送按钮"""
        json_data = self.CommandEditWindow.toPlainText() + '\r\n'
        self.CommandSendWindow.appendPlainText(json_data.strip())

        # 发送机械臂命令
        robot_arm_client = self.get_robot_arm_connector()
        with robot_arm_client as rac:
            rac.send(json_data.encode('utf-8'))
            rs_data = json.loads(rac.recv(1024).decode('utf-8').strip())
            self.CommandResWindow.appendPlainText(json.dumps(rs_data, use_decimal=True))  # 命令响应填入到响应窗口
    
    def get_robot_arm_connect_status(self):
        """获取机械臂连接状态"""
        pub.subscribe(self._check_robot_arm_connect_status, 'robot_arm_connect_status')
        
    def _check_robot_arm_connect_status(self, status: bool):
        """订阅机械臂连接状态"""
        self.robot_arm_is_connected = status
    
    @logger.catch
    def get_robot_arm_connector(self):
        """获取与机械臂的连接对象"""
        try:
            socket_info = shelve.open(str(settings.IP_PORT_INFO_FILE_PATH))
            host = socket_info['target_ip']
            port = int(socket_info['target_port'])
            robot_arm_client = ClientSocket(host, port)
            socket_info.close()
        except Exception as e:
            logger.exception(str(e))
            self.message_box.error_message_box(message="没有读取到 ip 和 port 信息，请前往机械臂配置 !")
        return robot_arm_client
    

class TeachPage(QFrame, teach_page_frame):
    """示教控制页面"""
    def __init__(self, page_name: str, thread_pool: QThreadPool, command_queue: Queue, joints_angle_queue: Queue):
        super().__init__()
        self.setupUi(self)
        self.setObjectName(page_name.replace(' ', '-'))
        self.initButtonIcon()
        self.initJointControlWidiget()
        
        # 状态标志
        self.move_status = True  # 机械臂运动状态
        self.thread_is_on = True  # 线程工作标志位
        self.table_action_thread_flag = True  # 顺序执行示教动作线程标志位
        self.robot_arm_is_connected = False  # 机械臂连接状态
        self.command_model = "SEQ"  # 用于示教执行命令时，判断机械臂的命令模式的标志位 SEQ(顺序指令), INT(实时指令)
        self.thread_pool = thread_pool  
        self.command_queue = command_queue  # 控制命令队列
        self.joints_angle_queue = joints_angle_queue  # 查询到的机械臂关节角度队列
        self.blinx_robot_arm = Mirobot(settings.ROBOT_MODEL_CONFIG_FILE_PATH, param_type='MDH')
        self.message_box = BlinxMessageBox(self)
        
        # 开启角度更新与末端工具位姿的更新线程
        self.back_task_start()
        
        # 设置输入框的过滤器
        self.init_input_validator()
        
        # 示教控制页面
        self.tool_type = ["夹爪", "吸盘"]
        self.ArmToolOptions = self.ArmToolComboBox.addItems(self.tool_type)
        self.ArmToolComboBox.setCurrentText("吸盘")
        
        # 示教控制操作按钮槽函数绑定
        self.ActionImportButton.clicked.connect(self.import_data)
        self.ActionOutputButton.clicked.connect(self.export_data)
        self.ActionModelSwitchButton.checkedChanged.connect(self.change_command_model)
        self.ActionStepRunButton.clicked.connect(self.run_action_step)
        self.ActionRunButton.clicked.connect(self.run_all_action)
        self.ActionLoopRunButton.clicked.connect(self.run_action_loop)
        self.ActionDeleteButton.clicked.connect(self.remove_item)
        self.ActionAddButton.clicked.connect(self.add_item)
        self.ActionUpdateRowButton.clicked.connect(self.update_row)
        self.ActionUpdateColButton.clicked.connect(self.update_column)  # 当前组件中无法选择列更新

        # 示教控制页面的按钮提示信息
        self.ActionImportButton.setToolTip("导入动作文件")
        self.ActionImportButton.setToolTipDuration(2000)
        self.ActionOutputButton.setToolTip("导出动作文件")
        self.ActionOutputButton.setToolTipDuration(2000)
        self.ActionStepRunButton.setToolTip("单次执行选定的动作")
        self.ActionStepRunButton.setToolTipDuration(2000)
        self.ActionRunButton.setToolTip("顺序执行所有动作")
        self.ActionRunButton.setToolTipDuration(2000)
        self.ActionLoopRunButton.setToolTip("循环执行指定次数动作")
        self.ActionLoopRunButton.setToolTipDuration(2000)
        self.ActionDeleteButton.setToolTip("删除指定动作")
        self.ActionDeleteButton.setToolTipDuration(2000)
        self.ActionUpdateRowButton.setToolTip("更新指定行动作")
        self.ActionUpdateRowButton.setToolTipDuration(2000)
        self.ActionAddButton.setToolTip("添加一行动作")
        self.ActionAddButton.setToolTipDuration(2000)
        
        
        # 示教控制添加右键的上下文菜单
        self.context_menu = QMenu(self)
        self.copy_action = self.context_menu.addAction("复制")
        self.paste_action = self.context_menu.addAction("粘贴")  # 默认粘贴到最后一行
        self.updata_action = self.context_menu.addAction("更新单元格")  # 暂时无法使用
        self.insert_row_action = self.context_menu.addAction("插入一行")  # 默认插入到最后一行，无法插入当前行的下一行
        self.copy_action.triggered.connect(self.copy_selected_row)
        self.paste_action.triggered.connect(self.paste_row)
        self.updata_action.triggered.connect(self.update_cell)
        self.insert_row_action.triggered.connect(self.insert_row)
        self.ActionTableWidget.setContextMenuPolicy(Qt.CustomContextMenu)
        self.ActionTableWidget.customContextMenuRequested.connect(self.show_context_menu)
        self.copied_row = None


        # 实例化机械臂关节控制回调函数绑定
        self.JointOneAddButton.clicked.connect(partial(self.modify_joint_angle, 1, -130, 135, increase=True))
        self.JointOneSubButton.clicked.connect(partial(self.modify_joint_angle, 1, -130, 135, increase=False))
        self.JointTwoAddButton.clicked.connect(partial(self.modify_joint_angle, 2, -86, 96, increase=True))
        self.JointTwoSubButton.clicked.connect(partial(self.modify_joint_angle, 2, -86, 96, increase=False))
        self.JointThreeAddButton.clicked.connect(partial(self.modify_joint_angle, 3, -90, 46, increase=True))
        self.JointThreeSubButton.clicked.connect(partial(self.modify_joint_angle, 3, -90, 46, increase=False))
        self.JointFourAddButton.clicked.connect(partial(self.modify_joint_angle, 4, -143, 184, increase=True))
        self.JointFourSubButton.clicked.connect(partial(self.modify_joint_angle, 4, -143, 184, increase=False))
        self.JointFiveAddButton.clicked.connect(partial(self.modify_joint_angle, 5, -219, 36, increase=True))
        self.JointFiveSubButton.clicked.connect(partial(self.modify_joint_angle, 5, -219, 36, increase=False))
        self.JointSixAddButton.clicked.connect(partial(self.modify_joint_angle, 6, -360, 360, increase=True))
        self.JointSixSubButton.clicked.connect(partial(self.modify_joint_angle, 6, -360, 360, increase=False))
        self.JointStepAddButton.clicked.connect(partial(self.modify_joint_angle_step, increase=True))
        self.JointStepSubButton.clicked.connect(partial(self.modify_joint_angle_step, increase=False))
        self.JointSpeedUpButton.clicked.connect(partial(self.modify_joint_speed_percentage, increase=True))
        self.JointSpeedDecButton.clicked.connect(partial(self.modify_joint_speed_percentage, increase=False))
        self.JointDelayTimeAddButton.clicked.connect(partial(self.modify_joint_delay_time, increase=True))
        self.JointDelayTimeSubButton.clicked.connect(partial(self.modify_joint_delay_time, increase=False))

        
        # # 复位和急停按钮绑定
        self.RobotArmResetButton.clicked.connect(self.robot_arm_initialize)
        self.RobotArmZeroButton.clicked.connect(self.reset_to_zero)
        self.RobotArmStopButton.clicked.connect(self.stop_robot_arm_emergency)
        
        # # 末端工具控制组回调函数绑定
        self.ArmClawOpenButton.clicked.connect(partial(self.tool_control, action=1))
        self.ArmClawCloseButton.clicked.connect(partial(self.tool_control, action=0))
        
        # 末端工具坐标增减回调函数绑定 
        self.XAxisAddButton.clicked.connect(partial(self.end_tool_coordinate_operate, axis='x', action="add"))
        self.XAxisSubButton.clicked.connect(partial(self.end_tool_coordinate_operate, axis='x', action="sub"))
        self.YAxisAddButton.clicked.connect(partial(self.end_tool_coordinate_operate, axis='y', action="add"))
        self.YAxisSubButton.clicked.connect(partial(self.end_tool_coordinate_operate, axis='y', action="sub"))
        self.ZAxisAddButton.clicked.connect(partial(self.end_tool_coordinate_operate, axis='z', action="add"))
        self.ZAxisSubButton.clicked.connect(partial(self.end_tool_coordinate_operate, axis='z', action="sub"))
        self.CoordinateAddButton.clicked.connect(partial(self.tool_coordinate_step_modify, action="add"))
        self.CoordinateStepSubButton.clicked.connect(partial(self.tool_coordinate_step_modify, action="sub"))
        
        # 末端工具姿态增减回调函数绑定
        self.RxAxisAddButton.clicked.connect(partial(self.tool_rx_operate, action="add"))
        self.RxAxisSubButton.clicked.connect(partial(self.tool_rx_operate, action="sub"))
        self.RyAxisAddButton.clicked.connect(partial(self.tool_ry_operate, action="add"))
        self.RyAxisSubButton.clicked.connect(partial(self.tool_ry_operate, action="sub"))
        self.RzAxisAddButton.clicked.connect(partial(self.tool_rz_operate, action="add"))
        self.RzAxisSubButton.clicked.connect(partial(self.tool_rz_operate, action="sub"))
        self.ApStepAddButton.clicked.connect(partial(self.tool_pose_step_modify, action="add"))
        self.ApStepSubButton.clicked.connect(partial(self.tool_pose_step_modify, action="sub"))

    def back_task_start(self):
        """后台任务启动"""
        logger.warning("获取机械臂连接状态定时器，启动!")
        self.get_arm_connect_status_timer = QTimer()
        self.get_arm_connect_status_timer.timeout.connect(self.get_robot_arm_connect_status_timer)
        self.get_arm_connect_status_timer.start(100)
        
        logger.warning("获取机械臂命令模式定时器，启动!")
        self.update_connect_status_timer = QTimer()
        self.update_connect_status_timer.timeout.connect(self.get_current_cmd_model)
        self.update_connect_status_timer.start(1000)
        
        logger.warning("更新机械臂的关节角度/末端位姿数据线程，启动!")
        self.update_joint_angles_thread = UpdateJointAnglesTask(self.joints_angle_queue)
        self.thread_pool.start(self.update_joint_angles_thread)
        self.update_joint_angles_thread.singal_emitter.joint_angles_update_signal.connect(self.update_joint_degrees_text)
        self.update_joint_angles_thread.singal_emitter.arm_endfactor_positions_update_signal.connect(self.update_arm_pose_text)

    # 顶部工具栏
    @check_robot_arm_connection                    
    @Slot()
    def import_data(self):
        """导入动作"""
        file_name, _ = QFileDialog.getOpenFileName(self, "导入动作文件", "",
                                                   "JSON Files (*.json);;All Files (*)")
        try:
            if file_name:
                logger.info(f"开始导入 {file_name} 动作文件")
                with open(file_name, "r", encoding="utf-8") as json_file:
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
                        note = item.get("备注", "")

                        row_position = self.ActionTableWidget.rowCount()
                        self.ActionTableWidget.insertRow(row_position)
                        self.update_table_cell(row_position, 0, angle_1)
                        self.update_table_cell(row_position, 1, angle_2)
                        self.update_table_cell(row_position, 2, angle_3)
                        self.update_table_cell(row_position, 3, angle_4)
                        self.update_table_cell(row_position, 4, angle_5)
                        self.update_table_cell(row_position, 5, angle_6)
                        self.update_table_cell(row_position, 6, speed_percentage)

                        # 工具列
                        arm_tool_combobox = ComboBox()
                        arm_tool_combobox.addItems(["", "夹爪", "吸盘"])
                        arm_tool_combobox.setCurrentText(arm_tool_option)
                        self.update_table_cell_widget(row_position, 7, arm_tool_combobox)

                        # 开关列
                        arm_tool_control_combobox = ComboBox()
                        arm_tool_control_combobox.addItems(["", "关", "开"])
                        arm_tool_control_combobox.setCurrentText(arm_tool_control)
                        self.update_table_cell_widget(row_position, 8, arm_tool_control_combobox)

                        # 延时列
                        self.update_table_cell(row_position, 9, arm_action_delay_time)
                        
                        # 备注列
                        self.update_table_cell(row_position, 10, note)
                        
                    logger.info("完成导入动作文件!")
            else:
                logger.warning("取消导入动作文件!")
        except Exception as e:
            logger.exception(f"导入动作文件失败: {e}")
            self.message_box.error_message_box(message="导入动作文件失败!")
    
    @check_robot_arm_connection
    @Slot()                    
    def export_data(self):
        """导出动作"""
        file_name, _ = QFileDialog.getSaveFileName(self, "导出动作文件", "", "JSON Files (*.json);;All Files (*)",
                                                   )
        if file_name:
            logger.info("开始导出动作文件")
            logger.debug(f"导出的配置文件的路径 {file_name}")
            data = []
            for row in range(self.ActionTableWidget.rowCount()):
                angle_1 = self.ActionTableWidget.item(row, 0).text()
                angle_2 = self.ActionTableWidget.item(row, 1).text()
                angle_3 = self.ActionTableWidget.item(row, 2).text()
                angle_4 = self.ActionTableWidget.item(row, 3).text()
                angle_5 = self.ActionTableWidget.item(row, 4).text()
                angle_6 = self.ActionTableWidget.item(row, 5).text()
                speed_percentage = self.ActionTableWidget.item(row, 6).text()        # 速度列
                arm_tool_widget = self.ActionTableWidget.cellWidget(row, 7)          # 工具列
                arm_tool_control_widget = self.ActionTableWidget.cellWidget(row, 8)  # 开关列
                arm_action_delay_time = self.ActionTableWidget.item(row, 9).text()   # 延时列
                note = self.ActionTableWidget.item(row, 10).text()                   # 备注列

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
                    "备注": note
                })

            with open(file_name, "w", encoding="utf-8") as json_file:
                json.dump(data, json_file, indent=4, ensure_ascii=False)
                logger.info("导出配置文件成功!")
    
    @check_robot_arm_connection
    @Slot()
    def change_command_model(self, isChecked: bool):
        """切换命令模式"""
        # INT: 实时指令模式(True)
        # SEQ: 顺序执行模式(False)
        self.command_model = "SEQ" if isChecked else "INT"
        logger.warning(f"命令模式切换: {self.command_model} !")
        command_model_payload = {"command": "set_robot_mode", "data": [self.command_model]}
        command_model_payload_str = json.dumps(command_model_payload).replace(' ', "") + '\r\n'
        self.command_queue.put(command_model_payload_str.encode('utf-8'))
    
    def tale_action_thread(self):
        """顺序执行示教动作线程"""
        action_count = self.ActionTableWidget.rowCount()
        logger.debug("机械臂动作数量: {}".format(action_count))
        for robot_action_row in range(self.ActionTableWidget.rowCount()):
            if self.table_action_thread_flag:
                pub.subscribe(self._check_tale_action_thread_flag, 'tale_action_thread_flag')
                logger.warning(f"机械臂正在执行第 {robot_action_row + 1} 个动作")
                
                # 更新任务执行的进度条
                self.ProgressBar.setVal(100 * (robot_action_row + 1) / action_count)
                
                # 构造机械臂执行动作的数据
                arm_payload_data, tool_type_data, delay_time = self.get_arm_action_payload(robot_action_row)
                
                # 订阅机械臂的角度信息，判断是否到达目标位置
                logger.debug(f'运动状态: {self.move_status}')
                
                # 发送机械臂执行动作的命令
                json_command = {"command": "set_joint_angle_all_time", "data": arm_payload_data}
                str_command = json.dumps(json_command, use_decimal=True).replace(' ', "") + '\r\n'
                self.command_queue.put(str_command.encode())
            
                # 控制末端工具动作的命令
                if tool_type_data[0] == "吸盘" and tool_type_data[1] != "":
                    tool_status = 1 if tool_type_data[1] == "开" else 0
                    json_command = {"command":"set_end_tool", "data": [1, tool_status]}
                    str_command = json.dumps(json_command).replace(' ', "") + '\r\n'
                    self.command_queue.put(str_command.encode())
                
                # SEQ 顺序模式下，发送延时命令，INT 模式不发送延时命令
                if self.command_model == 'SEQ' and delay_time != 0:
                    set_delay_time = int(delay_time * 1000)
                    if set_delay_time <= 30000:
                        json_command = {"command": "set_time_delay", "data": [set_delay_time]}
                        str_command = json.dumps(json_command).replace(' ', "") + '\r\n'
                        self.command_queue.put(str_command.encode())
                    else:
                        self.message_box.warning_message_box("延时时间太长，系统动作无法执行!")
                        break
                
                # 根据动作是否到位，以及线程是否工作判断是否执行
                if self.command_model == "INT":
                    pub.subscribe(self._check_tale_action_thread_flag, 'tale_action_thread_flag')
                    delay_count = 0  # 动作超时计数器
                    while not self.move_status and self.table_action_thread_flag and self.thread_is_on:
                        time.sleep(0.1)
                        pub.subscribe(self._joints_move_status, 'joints/move_status')  # 机械臂动作执行状态标识
                        pub.subscribe(self._check_flag, 'thread_work_flag')  # 线程控制标识
                        pub.subscribe(self._check_tale_action_thread_flag, 'tale_action_thread_flag')  # 示教线程运动标识
                        
                        logger.warning("等待上一个动作完成")
                        delay_count += 1
                        logger.debug(f"等待次数: {delay_count}")
                        if delay_count >= 100:
                            logger.warning("等待时间过长，默认完成!")
                            self.move_status = True
                            
                        # 完成所有动作后，退出循环
                        if robot_action_row + 1 == action_count:
                            logger.debug("所有动作执行完成")
                            self.move_status = True
                
                self.move_status = False  # 单个动作执行完成后需要重置状态，否则无法进入 while 循环
                self.ProgressBar.setVal(0)  # 进度条清零
            else:
                logger.warning("急停, 线程退出!")
                self.ProgressBar.setVal(0)  # 重置进度条
                break
            
    def _check_flag(self, flag=True):
        """线程工作控制位"""
        self.thread_is_on = flag
    
    def _check_tale_action_thread_flag(self, flag=True):
        """示教线程工作控制位"""
        self.table_action_thread_flag = flag
    
    def _joints_move_status(self, move_status=True):
        """订阅机械臂的关节运动状态"""
        self.move_status = move_status
    
    @check_robot_arm_connection
    @Slot()
    def run_all_action(self):
        """顺序执行示教动作"""
        self.TeachArmRunLogWindow.appendPlainText('【顺序执行】开始')
        run_all_action_thread = Worker(self.tale_action_thread)
        self.thread_pool.start(run_all_action_thread)
        
    def get_arm_action_payload(self, row):
        """获取机械臂示执行示教动作的角度数据

        Args:
            row (QTableWidget): 用户在示教界面，点击选中的行

        Returns:
            arm_payload_data (list): 机械臂的关节角度数据
            tool_type_data (list): 末端工具的类型数据
            delay_time (float): 执行动作需要的时间
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
        arm_payload = [speed_percentage, angle_1, angle_2, angle_3, angle_4, angle_5, angle_6]
        tool_payload = [type_of_tool, tool_switch]
        return arm_payload, tool_payload, delay_time

    def robot_arm_step_action_thread(self, row):
        """机械臂单次执行示教动作线程"""
        arm_payload_data, tool_type_data, _ = self.get_arm_action_payload(row)
        
        json_command = {"command": "set_joint_angle_all_time", "data": arm_payload_data}
        str_command = json.dumps(json_command, use_decimal=True).replace(' ', "") + '\r\n'
        self.command_queue.put(str_command.encode())
        
        # 末端工具动作
        if tool_type_data[0] == "吸盘" and tool_type_data[1] != "":
            tool_status = 1 if tool_type_data[1] == "开" else 0
            json_command = {"command":"set_end_tool", "data": [1, tool_status]}
            str_command = json.dumps(json_command).replace(' ', "") + '\r\n'
            self.command_queue.put(str_command.encode())

    @check_robot_arm_connection
    @Slot()
    def run_action_step(self):
        """单次执行选定的动作"""
        # 获取到选定的动作
        selected_row = self.ActionTableWidget.currentRow()
        if selected_row >= 0:
            self.TeachArmRunLogWindow.appendPlainText("正在执行第 " + str(selected_row + 1) + " 个动作")
            # 启动机械臂动作执行线程
            run_action_step_thread = Worker(self.robot_arm_step_action_thread, selected_row)
            self.thread_pool.start(run_action_step_thread)
        else:
            self.message_box.warning_message_box("请选择需要执行的动作!")

    def arm_action_loop_thread(self, loop_times):
        """机械臂循环执行指定次数的示教动作线程"""
        # 获取循环动作循环执行的次数
        for loop_time in range(loop_times):
            logger.warning(f"机械臂正在执行第 {loop_time + 1} 次循环动作")
            if self.table_action_thread_flag:
                self.tale_action_thread()
                time.sleep(1)  # 循环组间的间隔时间
            else:
                logger.warning("急停, 循环执行任务退出!")
                break
    
    @check_robot_arm_connection
    @Slot()
    def run_action_loop(self):
        """循环执行动作"""
        if self.ActionLoopTimes.text().isdigit():
            loop_times = int(self.ActionLoopTimes.text().strip())
            loop_work_thread = Worker(self.arm_action_loop_thread, loop_times)
            self.thread_pool.start(loop_work_thread)
        else:
            self.message_box.warning_message_box(f"请输入所以动作循环次数[0-9]")
    
    @Slot()
    def show_context_menu(self, pos):
        """右键复制粘贴菜单"""
        self.context_menu.exec_(self.ActionTableWidget.mapToGlobal(pos))
    
    @check_robot_arm_connection
    @Slot()
    def add_item(self):
        """示教控制添加一行动作"""
        speed_percentage = self.JointSpeedEdit.text()  # 速度值，暂定百分比
        type_of_tool = self.ArmToolComboBox.currentText()  # 获取末端工具类型
        
        row_position = self.ActionTableWidget.rowCount()
        self.ActionTableWidget.insertRow(row_position)
        self.ActionTableWidget.setItem(row_position, 0, QTableWidgetItem(str(self.q1)))
        self.ActionTableWidget.setItem(row_position, 1, QTableWidgetItem(str(self.q2)))
        self.ActionTableWidget.setItem(row_position, 2, QTableWidgetItem(str(self.q3)))
        self.ActionTableWidget.setItem(row_position, 3, QTableWidgetItem(str(self.q4)))
        self.ActionTableWidget.setItem(row_position, 4, QTableWidgetItem(str(self.q5)))
        self.ActionTableWidget.setItem(row_position, 5, QTableWidgetItem(str(self.q6)))
        self.ActionTableWidget.setItem(row_position, 6, QTableWidgetItem(speed_percentage))
        

        # 工具列添加下拉选择框
        arm_tool_combobox = ComboBox()
        arm_tool_combobox.addItems(["", "夹爪", "吸盘"])
        arm_tool_combobox.setCurrentText(type_of_tool)
        self.ActionTableWidget.setCellWidget(row_position, 7, arm_tool_combobox)

        # 开关列添加下拉选择框
        arm_tool_control = ComboBox()
        arm_tool_control.addItems(["", "关", "开"])
        self.ActionTableWidget.setCellWidget(row_position, 8, arm_tool_control)
        
        # 获取延时长短
        self.ActionTableWidget.setItem(row_position, 9, QTableWidgetItem(str(self.JointDelayTimeEdit.text())))
        
        # 备注列
        self.ActionTableWidget.setItem(row_position, 10, QTableWidgetItem(""))

    @check_robot_arm_connection
    @Slot()
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
    @Slot()
    def update_row(self):
        """示教控制更新指定行的动作"""
        selected_rows = self.ActionTableWidget.selectionModel().selectedRows()
        if selected_rows:
            for row in selected_rows:
                for col in range(self.ActionTableWidget.columnCount()):
                    if col == 0:
                        self.update_table_cell(row.row(), col, self.q1)
                    elif col == 1:
                        self.update_table_cell(row.row(), col, self.q2)
                    elif col == 2:
                        self.update_table_cell(row.row(), col, self.q3)
                    elif col == 3:
                        self.update_table_cell(row.row(), col, self.q4)
                    elif col == 4:
                        self.update_table_cell(row.row(), col, self.q5)
                    elif col == 5:
                        self.update_table_cell(row.row(), col, self.q6)
                    elif col == 6:
                        self.update_table_cell(row.row(), col, self.JointSpeedEdit.text())
                    elif col == 7:
                        arm_tool_combobox = ComboBox()
                        arm_tool_combobox.addItems(["", "夹爪", "吸盘"])
                        arm_tool_combobox.setCurrentText(self.ArmToolComboBox.currentText())
                        self.update_table_cell_widget(row.row(), col, arm_tool_combobox)
                    elif col == 9:
                        self.update_table_cell(row.row(), col, self.JointDelayTimeEdit.text())
        else:
            self.message_box.warning_message_box(message="请选择需要更新的行! \n点击表格左侧行号即可选中行")
    
    @check_robot_arm_connection
    @Slot()
    def update_column(self):
        """更新选中的列"""
        selected_columns = self.ActionTableWidget.selectionModel().selectedColumns()
        if selected_columns:
            for col in selected_columns:
                column_number = col.column()
                for row in range(self.ActionTableWidget.rowCount()):
                    if column_number == 0:
                        self.update_table_cell(row, column_number, self.q1)
                    elif column_number == 1:
                        self.update_table_cell(row, column_number, self.q2)
                    elif column_number == 2:
                        self.update_table_cell(row, column_number, self.q3)
                    elif column_number == 3:
                        self.update_table_cell(row, column_number, self.q4)
                    elif column_number == 4:
                        self.update_table_cell(row, column_number, self.q5)
                    elif column_number == 5:
                        self.update_table_cell(row, column_number, self.q6)
                    elif column_number == 6:
                        self.update_table_cell(row, column_number, self.JointSpeedEdit.text())
                    elif column_number == 7:
                        arm_tool_combobox = ComboBox()
                        arm_tool_combobox.addItems(["", "夹爪", "吸盘"])
                        arm_tool_combobox.setCurrentText(self.ArmToolComboBox.currentText())
                        self.update_table_cell_widget(row, column_number, arm_tool_combobox)
                    elif column_number == 8:
                        arm_tool_control = ComboBox()
                        arm_tool_control.addItems(["", "关", "开"])
                        self.update_table_cell_widget(row, column_number, arm_tool_control)
                    elif column_number == 9:
                        self.update_table_cell(row, column_number, self.JointDelayTimeEdit.text())
        else:
            self.message_box.warning_message_box(message="请选择需要更新的列! \n点击表格上方列名即可选中列")
    
    # 表格的右键菜单功能
    @Slot()
    def show_context_menu(self, pos):
        """右键复制粘贴菜单"""
        self.context_menu.exec(self.ActionTableWidget.mapToGlobal(pos))
    
    @Slot()
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

    @Slot()
    def paste_row(self):
        """粘贴选择行"""
        if self.copied_row:
            row_position = self.ActionTableWidget.rowCount()
            self.ActionTableWidget.insertRow(row_position)
            for col, value in enumerate(self.copied_row):
                if col == 7:  # 工具列、开关列需要获取下拉框的选中值
                    # 工具列添加下拉选择框
                    arm_tool_combobox = ComboBox()
                    arm_tool_combobox.addItems(["", "夹爪", "吸盘"])
                    arm_tool_combobox.setCurrentText(value)
                    self.update_table_cell_widget(row_position, col, arm_tool_combobox)
                elif col == 8:
                    # 开关列添加下拉选择框
                    arm_tool_control = ComboBox()
                    arm_tool_control.addItems(["", "关", "开"])
                    arm_tool_control.setCurrentText(value)
                    self.update_table_cell_widget(row_position, col, arm_tool_control)
                else:
                    self.update_table_cell(row_position, col, value)
    
    @Slot()
    def update_cell(self):
        """更新选中的单元格"""
        # 获取选中的单元格
        selected_items = self.ActionTableWidget.selectedItems()
        if selected_items:
            selected_row = selected_items[0].row()
            sellected_col = selected_items[0].column()
            if sellected_col == 0:
                self.update_table_cell(selected_row, sellected_col, self.q1)
            elif sellected_col == 1:
                self.update_table_cell(selected_row, sellected_col, self.q2)
            elif sellected_col == 2:
                self.update_table_cell(selected_row, sellected_col, self.q3)
            elif sellected_col == 3:
                self.update_table_cell(selected_row, sellected_col, self.q4)
            elif sellected_col == 4:
                self.update_table_cell(selected_row, sellected_col, self.q5)
            elif sellected_col == 5:
                self.update_table_cell(selected_row, sellected_col, self.q6)
            elif sellected_col == 6:
                self.update_table_cell(selected_row, sellected_col, self.JointSpeedEdit.text())
            elif sellected_col == 7:
                arm_tool_combobox = ComboBox()
                arm_tool_combobox.addItems(["", "夹爪", "吸盘"])
                arm_tool_combobox.setCurrentText(self.ArmToolComboBox.currentText())
                self.update_table_cell_widget(selected_row, sellected_col, arm_tool_combobox)
            elif sellected_col == 8:
                arm_tool_control = ComboBox()
                arm_tool_control.addItems(["", "关", "开"])
                self.update_table_cell_widget(selected_row, sellected_col, arm_tool_control)
            elif sellected_col == 9:
                self.update_table_cell(selected_row, sellected_col, self.JointDelayTimeEdit.text())
        else:
            self.message_box.warning_message_box(message="请选择需要更新的单元格! \n点击表格即可选中单元格")
    
    @Slot()
    def insert_row(self):
        """在当前行下插入一行"""
        selected_row = self.ActionTableWidget.currentRow()
        if selected_row >= 0:
            row_position = selected_row + 1
            self.ActionTableWidget.insertRow(row_position)
            for col in range(self.ActionTableWidget.columnCount()):
                if col == 0:
                    self.update_table_cell(row_position, col, self.q1)
                elif col == 1:
                    self.update_table_cell(row_position, col, self.q2)
                elif col == 2:
                    self.update_table_cell(row_position, col, self.q3)
                elif col == 3:
                    self.update_table_cell(row_position, col, self.q4)
                elif col == 4:
                    self.update_table_cell(row_position, col, self.q5)
                elif col == 5:
                    self.update_table_cell(row_position, col, self.q6)
                elif col == 6:
                    self.update_table_cell(row_position, col, self.JointSpeedEdit.text())
                elif col == 7:  
                    # 工具列、开关列需要获取下拉框的选中值
                    # 工具列添加下拉选择框
                    arm_tool_combobox = ComboBox()
                    arm_tool_combobox.addItems(["", "夹爪", "吸盘"])
                    arm_tool_combobox.setCurrentText(self.ArmToolComboBox.currentText())
                    self.update_table_cell_widget(row_position, col, arm_tool_combobox)
                elif col == 8:
                    # 开关列添加下拉选择框
                    arm_tool_control = ComboBox()
                    arm_tool_control.addItems(["", "关", "开"])
                    self.update_table_cell_widget(row_position, col, arm_tool_control)
                elif col == 9:
                    self.update_table_cell(row_position, col, self.JointDelayTimeEdit.text())
    
    @check_robot_arm_connection
    @Slot()
    def modify_joint_angle(self, joint_number, min_degrade, max_degrade, increase=True):
        """机械臂关节角度增减操作"""
        old_degrade = getattr(self, f'q{joint_number}')  # 获取当前对象的属性
        step_degrade = Decimal(self.JointStepEdit.text().strip())
        speed_percentage = Decimal(self.JointSpeedEdit.text().strip())

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
                {"command": "set_joint_angle", "data": [joint_number, speed_percentage, degrade]}, use_decimal=True) + '\r\n'
            self.command_queue.put(command.encode())
            logger.debug(f"机械臂关节 {joint_number} 转动 {degrade} 度")
            
            #  录制操作激活时
            if self.RecordActivateSwitchButton.isChecked():
                self.add_item()
    
    @check_robot_arm_connection
    @Slot()
    def modify_joint_angle_step(self, increase=True):
        """修改机械臂关节步长"""
        old_degrade = int(self.JointStepEdit.text().strip())
        degrade = old_degrade + 5 if increase else old_degrade - 5
        self.JointStepEdit.setText(str(degrade))
        logger.debug(f"机械臂步长修改为: {degrade}")

    @check_robot_arm_connection
    @Slot()
    def modify_joint_speed_percentage(self, increase=True):
        """修改关节运动速度百分比"""
        speed_percentage_edit = self.JointSpeedEdit.text()
        if speed_percentage_edit is not None and speed_percentage_edit.isdigit():
            old_speed_percentage = int(speed_percentage_edit.strip())
            new_speed_percentage = old_speed_percentage + 5 if increase else old_speed_percentage - 5
            if 0 <= new_speed_percentage <= 100:
                self.JointSpeedEdit.setText(str(new_speed_percentage))
                logger.debug(f"机械臂速度修改为: {new_speed_percentage}")
            else:
                self.message_box.warning_message_box(message=f"关节速度范围 0 ~ 100")
        else:
            self.message_box.error_message_box(message="请输入整数字符!")

    @check_robot_arm_connection
    @Slot()
    def modify_joint_delay_time(self, increase=True):
        """修改机械臂延时时间"""
        delay_time_edit = self.JointDelayTimeEdit.text()
        if delay_time_edit is not None and delay_time_edit.isdigit():
            old_delay_time = int(delay_time_edit.strip())
            new_delay_time = old_delay_time + 1 if increase else old_delay_time - 1
            if 0 <= new_delay_time <= 100:
                self.JointDelayTimeEdit.setText(str(new_delay_time))
                logger.debug(f"机械臂延时时间修改为: {new_delay_time}s")
            else:
                self.message_box.warning_message_box(message=f"延时时间必须在 0-100s 之间")
        else:
            self.message_box.error_message_box(message="请输入整数字符!")
    
    @check_robot_arm_connection
    @Slot()
    def robot_arm_initialize(self):
        """机械臂复位
        :param mode:
        """
        command = json.dumps({"command": "set_joint_initialize", "data": [0]}).replace('', "") + '\r\n'
        self.command_queue.put(command.encode())
        self.JointDelayTimeEdit.setText("0")  # 复位时延时时间设置为 0
        self.table_action_thread_flag = True
        
        InfoBar.warning(
            title="⚠️警告",
            content="🦾机械臂复位中! \n🦾请注意手臂姿态",
            isClosable=False,
            orient=Qt.Horizontal,
            duration=3000,
            position=InfoBarPosition.TOP,
            parent=self    
        )
        
        logger.warning("机械臂复位中!请注意手臂姿态")
    
    @check_robot_arm_connection
    @Slot()
    def reset_to_zero(self):
        """机械臂回零"""
        command = json.dumps({"command": "set_joint_angle_all", "data": [100, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]}).replace(' ', "") + '\r\n'
        self.command_queue.put(command.encode())
        self.JointDelayTimeEdit.setText("0")  # 归零时延时时间设置为 0
        self.message_box.warning_message_box("机械臂回到初始角度中!\n请注意手臂姿态")
        logger.warning("机械臂回到初始位姿中!")
    
    @check_robot_arm_connection
    # 机械臂急停按钮回调函数
    @Slot()
    def stop_robot_arm_emergency(self):
        """机械臂急停"""
        # 发送急停命令
        emergency_stop_command = json.dumps({"command": "set_joint_emergency_stop", "data": [0]}).replace(' ', "") + '\r\n'
        with self.get_robot_arm_connector() as robot_arm_connector:
            robot_arm_connector.send(emergency_stop_command.encode())
        
        # 重置线程工作状态
        pub.sendMessage('tale_action_thread_flag', flag=False)  # 示教线程标志位设置为 False
        InfoBar.warning(
            title="警告",
            content="机械臂急停! \n请排除完问题后, 点击两次: 初始化 按钮",
            isClosable=False,
            orient=Qt.Horizontal,
            duration=3000,
            position=InfoBarPosition.TOP,
            parent=self
            )
    
    @check_robot_arm_connection
    @Slot()
    def tool_control(self, action=1):
        """吸盘工具开"""
        type_of_tool = self.ArmToolComboBox.currentText()
        if type_of_tool == "吸盘":
            command = json.dumps({"command":"set_end_tool", "data": [1, action]}) + '\r\n'
            
            if action:
                logger.warning("吸盘开启!")
            else:
                logger.warning("吸盘关闭!")
                
            self.command_queue.put(command.encode())
        else:
            self.message_box.warning_message_box("末端工具未选择吸盘!")
    
    @check_robot_arm_connection
    @Slot()
    def end_tool_coordinate_operate(self, axis: str, action: str = "add"):
        """末端工具坐标增减函数"""
        # 获取末端工具的坐标
        coordinates = {'x': self.X, 'y': self.Y, 'z': self.Z}
        old_coordinate = coordinates[axis.lower()]

        # 获取末端工具的姿态
        rx_pose = self.rx
        ry_pose = self.ry
        rz_pose = self.rz

        change_value = self._decimal_round(self.CoordinateStepEdit.text().strip(), accuracy='0.001')  # 步长值
        speed_percentage = round(int(self.JointSpeedEdit.text().strip()), 2)  # 速度值

        # 根据按钮加减增减数值
        if action == "add":
            new_coordinate = old_coordinate + change_value
        else:
            new_coordinate = old_coordinate - change_value

        logger.debug(f"末端工具, 目标坐标 {axis.upper()}: {new_coordinate}")

        # 通过逆解算出机械臂各个关节角度值
        coordinates[axis] = new_coordinate
        arm_ikine_solves = self.get_arm_ikine(coordinates['x'], coordinates['y'], coordinates['z'], rx_pose, ry_pose, rz_pose)
        self.construct_and_send_command(arm_ikine_solves, speed_percentage)

        #  录制操作激活时
        if self.RecordActivateSwitchButton.isChecked():
            self.add_item()

    @check_robot_arm_connection
    @Slot()
    def tool_coordinate_step_modify(self, action="add"):
        """末端工具坐标步长增减函数"""
        old_coordinate_step = self._decimal_round(self.CoordinateStepEdit.text().strip(), accuracy='0.001')
        if action == "add":
            new_coordinate_step = old_coordinate_step + Decimal('1')
        else:
            new_coordinate_step = old_coordinate_step - Decimal('1')
            
        logger.debug(f"末端工具坐标步长设置为: {new_coordinate_step}")
        self.CoordinateStepEdit.setText(str(new_coordinate_step))
    
    @check_robot_arm_connection
    @Slot()
    def tool_rx_operate(self, action="add"):
        """末端工具坐标 Rx 增减函数"""
        # 获取末端工具的坐标
        x_coordinate = self._decimal_round(self.XAxisEdit.text().strip(), accuracy='0.001')
        y_coordinate = self._decimal_round(self.YAxisEdit.text().strip(), accuracy='0.001')
        z_coordinate = self._decimal_round(self.ZAxisEdit.text().strip(), accuracy='0.001')
        
        # 获取末端工具的姿态
        old_rx_pose = self._decimal_round(self.RxAxisEdit.text().strip(), accuracy='0.001')
        ry_pose = self._decimal_round(self.RyAxisEdit.text().strip(), accuracy='0.001')
        rz_pose = self._decimal_round(self.RzAxisEdit.text().strip(), accuracy='0.001')
        
        change_value = self._decimal_round(self.ApStepEdit.text().strip(), accuracy='0.001')  # 步长值
        speed_percentage = round(int(self.JointSpeedEdit.text().strip()), 2)  # 速度值
        
        # 根据按钮加减增减数值
        if action == "add":
            new_rx_pose = old_rx_pose + change_value
            logger.debug(f"末端工具翻滚姿态 Rx: {new_rx_pose} 度")
        else:
            new_rx_pose = old_rx_pose - change_value
            logger.debug(f"末端工具翻滚姿态 Rx: {new_rx_pose} 度")
        
        
        # 根据增减后的位姿数值，逆解出机械臂关节的角度并发送命令
        arm_ikine_solves = self.get_arm_ikine(x_coordinate, y_coordinate, z_coordinate, new_rx_pose, ry_pose, rz_pose)
        self.construct_and_send_command(arm_ikine_solves, speed_percentage)
        
        #  录制操作激活时
        if self.RecordActivateSwitchButton.isChecked():
            self.add_item()
    
    @check_robot_arm_connection
    @Slot()           
    def tool_ry_operate(self, action="add"):
        """末端工具坐标 Ry 增减函数"""
        # 获取末端工具的坐标
        x_coordinate = self._decimal_round(self.XAxisEdit.text().strip(), accuracy='0.001')
        y_coordinate = self._decimal_round(self.YAxisEdit.text().strip(), accuracy='0.001')
        z_coordinate = self._decimal_round(self.ZAxisEdit.text().strip(), accuracy='0.001')
        
        # 获取末端工具的姿态
        rx_pose = self._decimal_round(self.RxAxisEdit.text().strip(), accuracy='0.001')
        old_ry_pose = self._decimal_round(self.RyAxisEdit.text().strip(), accuracy='0.001')
        rz_pose = self._decimal_round(self.RzAxisEdit.text().strip(), accuracy='0.001')
        
        change_value = self._decimal_round(self.ApStepEdit.text().strip(), accuracy='0.001')  # 步长值
        speed_percentage = round(int(self.JointSpeedEdit.text().strip()), 2)  # 速度值
        
        # 根据按钮加减增减数值
        if action == "add":
            new_ry_pose = old_ry_pose + change_value
            logger.debug(f"末端工具俯仰姿态 Ry: {new_ry_pose} 度")
        else:
            new_ry_pose = old_ry_pose - change_value
            logger.debug(f"末端工具俯仰姿态 Ry: {new_ry_pose} 度")
            
        # 根据增减后的位姿数值，逆解出机械臂关节的角度并发送命令
        arm_ikine_solves = self.get_arm_ikine(x_coordinate, y_coordinate, z_coordinate, rx_pose, new_ry_pose, rz_pose)
        self.construct_and_send_command(arm_ikine_solves, speed_percentage)
        
        #  录制操作激活时
        if self.RecordActivateSwitchButton.isChecked():
            self.add_item()
    
    @check_robot_arm_connection
    @Slot()    
    def tool_rz_operate(self, action="add"):
        """末端工具坐标 Rz 增减函数"""
        # 获取末端工具的坐标、姿态数值
        x_coordinate = self._decimal_round(self.XAxisEdit.text().strip(), accuracy='0.001')
        y_coordinate = self._decimal_round(self.YAxisEdit.text().strip(), accuracy='0.001')
        z_coordinate = self._decimal_round(self.ZAxisEdit.text().strip(), accuracy='0.001')
        
        # 获取末端工具的姿态
        rx_pose = self._decimal_round(self.RxAxisEdit.text().strip(), accuracy='0.001')
        ry_pose = self._decimal_round(self.RyAxisEdit.text().strip(), accuracy='0.001')
        old_rz_pose = self._decimal_round(self.RzAxisEdit.text().strip(), accuracy='0.001')
        
        change_value = self._decimal_round(self.ApStepEdit.text().strip(), accuracy='0.001')  # 步长值
        speed_percentage = round(int(self.JointSpeedEdit.text().strip()), 2)  # 速度值
        
        
        # 根据按钮加减增减数值
        if action == "add":
            new_rz_pose = old_rz_pose + change_value
            logger.debug(f"末端工具偏航姿态 Rz: {new_rz_pose} 度")
        else:
            new_rz_pose = old_rz_pose - change_value
            logger.debug(f"末端工具偏航姿态 Rz: {new_rz_pose} 度")
            
        # 根据增减后的位姿数值，逆解出机械臂关节的角度并发送命令
        arm_ikine_solves = self.get_arm_ikine(x_coordinate, y_coordinate, z_coordinate, rx_pose, ry_pose, new_rz_pose)
        self.construct_and_send_command(arm_ikine_solves, speed_percentage)
        
        #  录制操作激活时
        if self.RecordActivateSwitchButton.isChecked():
            self.add_item()
    
    @check_robot_arm_connection
    @Slot()
    def tool_pose_step_modify(self, action="add"):
        """末端工具姿态步长增减函数"""
        old_pose_step = self._decimal_round(self.ApStepEdit.text().strip(), accuracy='0.01')
        if action == "add":
            new_pose_step = old_pose_step + Decimal('1')
        elif action == "sub":
            new_pose_step = old_pose_step - Decimal('1')
        else:
            raise ValueError("action 参数只能为 add 或 sub")
        logger.debug(f"末端工具姿态步长设置为: {new_pose_step}")
        self.ApStepEdit.setText(str(new_pose_step))
    
    # 一些 qt 界面的常用的抽象操作
    def update_table_cell_widget(self, row, col, widget):
        """更新表格指定位置的小部件"""
        self.ActionTableWidget.setCellWidget(row, col, widget)
    
    # 一些 qt 界面的常用的抽象操作                
    def update_table_cell(self, row, col, value):
        """更新表格指定位置的项"""
        self.ActionTableWidget.setItem(row, col, QTableWidgetItem(str(value)))
    
    def initJointControlWidiget(self):
        """分段导航栏添加子页面控件"""
        self.addSubInterface(self.ArmAngleControlCard, 'ArmAngleControlCard', '关节角度控制')
        self.addSubInterface(self.ArmEndToolsCoordinateControlCard, 'ArmEndToolsCoordinateControlCard', '末端坐标/姿态控制')

        self.ArmActionControlStackWidget.currentChanged.connect(self.onCurrentIndexChanged)
        self.ArmActionControlStackWidget.setCurrentWidget(self.ArmAngleControlCard)
        self.RobotArmControlSegmentedWidget.setCurrentItem(self.ArmAngleControlCard.objectName())
        
    def addSubInterface(self, widget: CardWidget, objectName, text):
        """添加子页面控件到分段导航栏"""
        # 先将子页面添加到 StackWidget 堆栈控件中
        self.ArmActionControlStackWidget.addWidget(widget)
        self.RobotArmControlSegmentedWidget.addItem(
            routeKey=objectName,
            text=text,
            onClick=lambda: self.ArmActionControlStackWidget.setCurrentWidget(widget),
        )
    
    def onCurrentIndexChanged(self, index):
        """分段导航栏切换页面回调函数"""
        widget = self.ArmActionControlStackWidget.widget(index)
        self.RobotArmControlSegmentedWidget.setCurrentItem(widget.objectName())
        
    def initButtonIcon(self):
        """初始化按钮图标"""
        self.ActionImportButton.setIcon(FIF.DOWNLOAD)
        self.ActionOutputButton.setIcon(FIF.UP)
        self.ActionStepRunButton.setIcon(FIF.PLAY)
        self.ActionRunButton.setIcon(FIF.ALIGNMENT)
        self.ActionLoopRunButton.setIcon(FIF.ROTATE)
        self.ActionAddButton.setIcon(FIF.ADD_TO)
        self.ActionDeleteButton.setIcon(FIF.DELETE)
        self.ActionUpdateColButton.setIcon(FIF.SCROLL)
        self.ActionUpdateRowButton.setIcon(FIF.MENU)
        # 关节控制按钮图标
        self.JointOneAddButton.setIcon(FIF.ADD)
        self.JointOneSubButton.setIcon(FIF.REMOVE)
        self.JointTwoAddButton.setIcon(FIF.ADD)
        self.JointTwoSubButton.setIcon(FIF.REMOVE)
        self.JointThreeAddButton.setIcon(FIF.ADD)
        self.JointThreeSubButton.setIcon(FIF.REMOVE)
        self.JointFourAddButton.setIcon(FIF.ADD)
        self.JointFourSubButton.setIcon(FIF.REMOVE)
        self.JointFiveAddButton.setIcon(FIF.ADD)
        self.JointFiveSubButton.setIcon(FIF.REMOVE)
        self.JointSixAddButton.setIcon(FIF.ADD)
        self.JointSixSubButton.setIcon(FIF.REMOVE)
        self.JointStepAddButton.setIcon(FIF.ADD)
        self.JointStepSubButton.setIcon(FIF.REMOVE)
        self.JointSpeedUpButton.setIcon(FIF.ADD)
        self.JointSpeedDecButton.setIcon(FIF.REMOVE)
        self.JointDelayTimeAddButton.setIcon(FIF.ADD)
        self.JointDelayTimeSubButton.setIcon(FIF.REMOVE)
        # 坐标控制按钮图标
        self.XAxisAddButton.setIcon(FIF.ADD)
        self.XAxisSubButton.setIcon(FIF.REMOVE)
        self.YAxisAddButton.setIcon(FIF.ADD)
        self.YAxisSubButton.setIcon(FIF.REMOVE)
        self.ZAxisAddButton.setIcon(FIF.ADD)
        self.ZAxisSubButton.setIcon(FIF.REMOVE)
        self.CoordinateAddButton.setIcon(FIF.ADD)
        self.CoordinateStepSubButton.setIcon(FIF.REMOVE)
        # 姿态控制按钮图标
        self.RxAxisAddButton.setIcon(FIF.ADD)
        self.RxAxisSubButton.setIcon(FIF.REMOVE)
        self.RyAxisAddButton.setIcon(FIF.ADD)
        self.RyAxisSubButton.setIcon(FIF.REMOVE)
        self.RzAxisAddButton.setIcon(FIF.ADD)
        self.RzAxisSubButton.setIcon(FIF.REMOVE)
        self.ApStepAddButton.setIcon(FIF.ADD)
        self.ApStepSubButton.setIcon(FIF.REMOVE)
    
    def update_joint_degrees_text(self, angle_data_list: list):
        """更新界面上的角度值, 并返回实时角度值

        Args:
            rs_data_dict (_dict_): 与机械臂通讯获取到的机械臂角度值
        """
        self.q1, self.q2, self.q3, self.q4, self.q5, self.q6 = angle_data_list
        display_q1 = str(self.q1)
        display_q2 = str(self.q2)
        display_q3 = str(self.q3)
        display_q4 = str(self.q4)
        display_q5 = str(self.q5)
        display_q6 = str(self.q6)
        self.JointOneEdit.setText(display_q1)
        self.JointTwoEdit.setText(display_q2)
        self.JointThreeEdit.setText(display_q3)
        self.JointFourEdit.setText(display_q4)
        self.JointFiveEdit.setText(display_q5)
        self.JointSixEdit.setText(display_q6)
    
    def update_arm_pose_text(self, arm_pose_data: list):
        """更新界面上机械臂末端工具的坐标和姿态值"""
        self.X, self.Y, self.Z = arm_pose_data[:3]
        self.rx, self.ry, self.rz = arm_pose_data[3:]
        self.XAxisEdit.setText(str(self.X))
        self.YAxisEdit.setText(str(self.Y))
        self.ZAxisEdit.setText(str(self.Z))
        self.RxAxisEdit.setText(str(self.rx))
        self.RyAxisEdit.setText(str(self.ry))
        self.RzAxisEdit.setText(str(self.rz))

    def construct_and_send_command(self, joint_degrees, speed_percentage):
        """构造逆解后的发送命令"""
        if joint_degrees is not None:
            speed_degree_data = [speed_percentage]
            speed_degree_data.extend(joint_degrees)
            command = json.dumps({"command": "set_joint_angle_all_time", "data": speed_degree_data}, use_decimal=True).replace(' ', "") + '\r\n'
            logger.debug(f"逆解后的所有关节角度值: {list(map(lambda d: float(d), joint_degrees))}")
            # 发送命令
            self.command_queue.put(command.encode())
        else:
            logger.warning("关节运动范围超出超限!")
            self.message_box.error_message_box("关节运动范围超限!")
        
    def get_arm_ikine(self, x_coordinate, y_coordinate, z_coordinate, rx_pose, ry_pose, rz_pose) -> list:
        """计算机械臂的逆解"""
        # 对坐标的值缩小 3 位
        x_coordinate, y_coordinate, z_coordinate = map(self._decimal_exp, [x_coordinate, y_coordinate, z_coordinate])
        logger.debug(f"缩小后的末端工具坐标: {x_coordinate}, {y_coordinate}, {z_coordinate}")
        logger.debug(f"末端工具姿态: {rx_pose}, {ry_pose}, {rz_pose}")
        R_T = SE3([x_coordinate, y_coordinate, z_coordinate]) * rpy2tr([float(rx_pose), float(ry_pose), float(rz_pose)], unit='deg', order='zyx')
        sol = self.blinx_robot_arm.ikine_LM(R_T, joint_limits=True)
        if sol.success:
            joint_degrees = [self._decimal_round(degrees(d)) for d in sol.q]
        else:
            joint_degrees = None
        
        return joint_degrees
    
    @logger.catch
    def get_robot_arm_connector(self):
        """获取与机械臂的连接对象"""
        try:
            socket_info = shelve.open(str(settings.IP_PORT_INFO_FILE_PATH))
            host = socket_info['target_ip']
            port = int(socket_info['target_port'])
            robot_arm_client = ClientSocket(host, port)
            socket_info.close()
        except Exception as e:
            logger.exception(str(e))
            self.message_box.error_message_box(message="没有读取到 ip 和 port 信息，请前往机械臂配置 !")
        return robot_arm_client
    
    def get_current_cmd_model(self):
        """连接上机械臂后，获取当前的命令模式并更新"""
        pub.subscribe(self._get_robot_arm_connect_status, 'robot_arm_connect_status')
        if self.robot_arm_is_connected:
            get_cmd_model_payload = json.dumps({"command": "get_robot_mode"}).replace(' ', "") + '\r\n'
            
            with self.get_robot_arm_connector() as conn:
                conn.send(get_cmd_model_payload.encode())
                try:
                    cmd_model_str = conn.recv(1024).decode()
                    cmd_model = json.loads(cmd_model_str)['data']
                    logger.debug(f"机械臂当前的命令模式为: {cmd_model}")
                    
                    if cmd_model == "SEQ":
                        logger.warning(f"机械臂当前为 SEQ 顺序模式!")
                        self.ActionModelSwitchButton.setChecked(True)
                        self.command_model = "SEQ"
                    else:
                        logger.warning(f"机械臂当前为 INT 实时模式!")
                        self.ActionModelSwitchButton.setChecked(False)
                        self.command_model = "INT"
                        
                    logger.warning("更新机械臂命令模式定时器停止!")
                    self.update_connect_status_timer.stop()
                    
                except Exception as e:
                    logger.exception(str(e))
                    self.message_box.error_message_box("获取机械臂命令模式失败!")
                
    def get_robot_arm_connect_status_timer(self):
        """获取机械臂连接状态的定时器"""
        pub.subscribe(self._get_robot_arm_connect_status, 'robot_arm_connect_status')
    
    def _get_robot_arm_connect_status(self, status: bool):
        self.robot_arm_is_connected = status
    
    def _decimal_round(self, joints_angle, accuracy="0.001") -> Decimal:
        """用精确的方式四舍五入"""
        if not isinstance(joints_angle, str):
            joints_angle_str = str(joints_angle)
        else:
            joints_angle_str = joints_angle
            
        joints_angle_decimal = Decimal(joints_angle_str).quantize(Decimal(accuracy), rounding = "ROUND_HALF_UP")
        return joints_angle_decimal
    
    def _decimal_exp(self, value: Decimal) -> float:
        """用精确的方式四舍五入, 保留末端坐标和姿态的三位小数"""
        coordinate_value = value / Decimal('1000')
        coordinate_value_float = coordinate_value.quantize(Decimal("0.001"), rounding="ROUND_HALF_UP")
        return float(coordinate_value_float)
    
    def init_input_validator(self):
        """设置输入框的过滤规则"""
        # 只允许输入阿拉伯数字
        only_digidts_regex = QRegularExpression(r'^[0-9]{1,3}$')
        only_digidts_validator = QRegularExpressionValidator(only_digidts_regex, self)
        self.ActionLoopTimes.setValidator(only_digidts_validator)
        self.JointStepEdit.setValidator(only_digidts_validator)
        self.JointSpeedEdit.setValidator(only_digidts_validator)
        self.JointDelayTimeEdit.setValidator(only_digidts_validator)
        
        # 只允许输入浮点数
        only_float_regex = QRegularExpression(r'^-?\d{1,3}(\.\d{1,3})?$')
        only_float_validator = QRegularExpressionValidator(only_float_regex, self)
        
        # 关节控制正则过滤
        self.JointOneEdit.setValidator(only_float_validator)
        self.JointTwoEdit.setValidator(only_float_validator)
        self.JointThreeEdit.setValidator(only_float_validator)
        self.JointFourEdit.setValidator(only_float_validator)
        self.JointFiveEdit.setValidator(only_float_validator)
        self.JointSixEdit.setValidator(only_float_validator)
        
        # 坐标控制正则过滤
        self.XAxisEdit.setValidator(only_float_validator)
        self.YAxisEdit.setValidator(only_float_validator)
        self.ZAxisEdit.setValidator(only_float_validator)
        self.CoordinateStepEdit.setValidator(only_float_validator)
        
        # 末端工具位置与姿态正则过滤
        self.RxAxisEdit.setValidator(only_float_validator)
        self.RyAxisEdit.setValidator(only_float_validator)
        self.RzAxisEdit.setValidator(only_float_validator)
        self.ApStepEdit.setValidator(only_digidts_validator)
    
    
class ConnectPage(QFrame, connect_page_frame):
    """连接配置页面"""
    def __init__(self, page_name: str, thread_pool: QThreadPool, command_queue: Queue, joints_angle_queue: Queue):
        super().__init__()
        self.setupUi(self)
        self.setObjectName(page_name.replace(' ', '-'))
        self.reload_ip_port_history()  # 加载上一次的配置
        
        # 开启 QT 线程池
        self.thread_pool = thread_pool
        self.command_queue = command_queue
        self.joints_angle_queue = joints_angle_queue
        
        self.init_task_thread()
        self.init_input_validator()
        
        # 机械臂的连接状态
        self.robot_arm_is_connected = False
        
        self.message_box = BlinxMessageBox(self)
        self.robot_arm_connecting_tip = None
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
        self.RobotArmDisconnectButton.clicked.connect(self.disconnect_to_robot_arm)
        self.RobotArmDisconnectButton.setEnabled(False)

    def init_input_validator(self):
        """对用户输入过滤"""
        # 限制 IP 输入
        ip_regex = QRegularExpression(r'^((\d|[1-9]\d|1\d\d|2[0-4]\d|25[0-5])\.){3}(\d|[1-9]\d|1\d\d|2[0-4]\d|25[0-5])(?::(?:[0-9]|[1-9][0-9]{1,3}|[1-5][0-9]{4}|6[0-4][0-9]{3}|65[0-4][0-9]{2}|655[0-2][0-9]|6553[0-5]))?$')
        ip_validator = QRegularExpressionValidator(ip_regex, self)
        self.TargetIpEdit.setValidator(ip_validator)
        
        # 限制端口号输入
        sport_regex = QRegularExpression(r'^(102[4-9]|10[3-9]\d|1[1-9]\d{2}|[2-9]\d{3}|[1-5]\d{4}|6[0-4]\d{3}|65[0-4]\d{2}|655[0-2]\d|6553[0-5])$')
        sport_validator = QRegularExpressionValidator(sport_regex, self)
        self.TargetPortEdit.setValidator(sport_validator)

        # 限制 Wifi SSID 输入
        ssid_regex = QRegularExpression(r'^[a-zA-Z0-9_\-]{1,32}$')
        ssid_validator = QRegularExpressionValidator(ssid_regex, self)
        self.WiFiSsidEdit.setValidator(ssid_validator)
        
        # 限制 wifi 密码输入
        password_regex = QRegularExpression(r'^[a-zA-Z0-9_\-]{8,63}$')
        password_validator = QRegularExpressionValidator(password_regex, self)
        self.WiFiPasswordLineEdit.setValidator(password_validator)
        
    def init_task_thread(self):
        """初始化后台线程任务"""
        self.angle_degree_thread = AgnleDegreeWatchTask(self.joints_angle_queue)
        self.command_sender_thread = CommandSenderTask(self.command_queue)
        self.command_recver_thread = CommandReceiverTask()
    
    # 机械臂连接配置回调函数
    def reload_ip_port_history(self):
        """获取历史IP和Port填写记录"""
        try:
            if settings.IP_PORT_INFO_FILE_PATH.parent.exists() is False:
                settings.IP_PORT_INFO_FILE_PATH.parent.mkdir(parents=True)
            else:
                socket_info = shelve.open(str(settings.IP_PORT_INFO_FILE_PATH))
                self.TargetIpEdit.setText(socket_info["target_ip"])
                self.TargetPortEdit.setText(str(socket_info["target_port"]))
                socket_info.close()
        except KeyError:
            logger.warning("IP 和 Port 未找到对应记录, 请填写配置信息!")
            self.TargetIpEdit.setText("")
            self.TargetPortEdit.setText("")
    
    @Slot()
    def submit_ip_port_info(self):
        """配置机械臂的通讯IP和端口"""
        ip = self.TargetIpEdit.text().strip()
        port = self.TargetPortEdit.text().strip()
        
        # 保存 IP 和 Port 信息
        if all([ip, port]):
            socket_info = shelve.open(str(settings.IP_PORT_INFO_FILE_PATH))
            socket_info["target_ip"] = ip
            socket_info["target_port"] = int(port)
            self.message_box.success_message_box(message="配置添加成功!")
            socket_info.close()
        else:
            self.message_box.warning_message_box(message="IP 或 Port 号为空，请重新填写!")
    
    @Slot()
    def reset_ip_port_info(self):
        """重置 IP 和 Port 输入框内容"""
        self.TargetIpEdit.clear()
        self.TargetPortEdit.clear()
    
    # 机械臂 WiFi AP 模式配置回调函数
    def reload_ap_passwd_history(self):
        """获取历史 WiFi 名称和 Passwd 记录"""            
        try:
            if settings.WIFI_INFO_FILE_PATH.parent.exists() is False:
                settings.WIFI_INFO_FILE_PATH.parent.mkdir(parents=True)
            else:
                wifi_info = shelve.open(str(settings.WIFI_INFO_FILE_PATH))
                self.WiFiSsidEdit.setText(wifi_info["SSID"])
                self.WiFiPasswordLineEdit.setText(wifi_info["passwd"])
                wifi_info.close()
        except KeyError:
            logger.warning("WiFi 配置未找到历史记录,请填写配置信息!")
            self.WiFiSsidEdit.setText("")
            self.WiFiPasswordLineEdit.setText("")
    
    @Slot()
    def submit_ap_passwd_info(self):
        """配置机械臂的通讯 WiFi 名称和 passwd"""
        ip = self.WiFiSsidEdit.text().strip()
        port = self.WiFiPasswordLineEdit.text().strip()
        
        # 保存 IP 和 Port 信息
        if all([ip, port]):
            wifi_info = shelve.open(str(settings.WIFI_INFO_FILE_PATH))
            wifi_info["SSID"] = ip
            wifi_info["passwd"] = port
            wifi_info.close()
            self.message_box.success_message_box(message="WiFi 配置添加成功!")
        else:
            self.message_box.warning_message_box(message="WiFi名称 或密码为空，请重新填写!")
    
    @Slot()
    def reset_ap_passwd_info(self):
        """重置 WiFi 名称和 passwd 输入框内容"""
        self.WiFiSsidEdit.clear()
        self.WiFiPasswordLineEdit.clear()

    # todo: 机械臂串口连接配置回调函数
    @Slot()
    def get_sb_info(self):
        """获取系统当前的串口信息并更新下拉框"""
        ports = list_ports.comports()
        self.SerialNumComboBox.addItems([f"{port.device}" for port in ports])
    
    @logger.catch
    @Slot()
    def connect_to_robot_arm(self):
        """连接机械臂"""
        try:
            remote_address = self.get_robot_arm_connect_info()
                
            if remote_address:
                InfoBar.success(
                    title='连接成功',
                    content=f"机械臂连接成功 !\nIP: {remote_address[0]}\nPort: {remote_address[1]}",
                    orient=Qt.Horizontal,
                    isClosable=True,
                    position=InfoBarPosition.BOTTOM_RIGHT,
                    duration=3000,
                    parent=self
                )
                
                self._update_arm_connect_status(connected=True)
                self.start_sender_recv_threads()
    

        except Exception as e:
            # 连接失败后，将连接机械臂按钮启用
            self.RobotArmLinkButton.setEnabled(True)
            # 清空队列
            self.command_queue.queue.clear()
            # 弹出错误提示框
            logger.exception(f"机械臂连接失败: {e}")
            InfoBar.error(
                title='连接失败',
                content="机械臂连接失败 !",
                orient=Qt.Horizontal,
                isClosable=False,
                duration=3000,
                parent=self
            )

    def get_robot_arm_connect_info(self):
        """连接机械臂线程"""
        self.RobotArmLinkButton.setEnabled(False)
        # 检查网络连接状态
        robot_arm_client = self.get_robot_arm_connector()
        with robot_arm_client as rac:
            remote_address = rac.getpeername()
            logger.info("机械臂连接成功!")
        return remote_address

    def _update_arm_connect_status(self, connected: bool =True):
        """更新机械臂的连接状态, 以及相关按钮的状态"""
        # 发布机械臂连接状态
        pub.sendMessage("robot_arm_connect_status", status=True)
        self.robot_arm_is_connected = connected
        
        # 更新机械臂连接按钮状态
        self.RobotArmLinkButton.setText("机械臂已连接")
        # 连接成功后，将连接机械臂按钮禁用，避免用户操作重复发起连接
        self.RobotArmLinkButton.setEnabled(not connected)
        self.RobotArmDisconnectButton.setEnabled(connected)
    
    @Slot()
    def disconnect_to_robot_arm(self):
        """断开与机械臂的连接"""
        # 清空命令、角度队列
        self.command_queue.queue.clear()
        self.joints_angle_queue.queue.clear()
        
        # 关闭线程池
        pub.sendMessage("thread_work_flag", flag=False)
        pub.sendMessage("robot_arm_connect_status", status=False)
        
        InfoBar.warning(
            title='连接断开',
            content="机械臂连接断开 !",
            orient=Qt.Horizontal,
            isClosable=False,   # disable close button
            position=InfoBarPosition.TOP_RIGHT,
            duration=2000,
            parent=self
        )
        
        self.RobotArmLinkButton.setEnabled(True)
        self.RobotArmLinkButton.setText("连接机械臂")
        self.RobotArmDisconnectButton.setEnabled(False)
        
        # 创建新的线程对象
        self.init_task_thread()
    
    def start_sender_recv_threads(self):
        """启动命令发送与命令接收线程"""
        # 启用实时获取机械臂角度线程
        self.joints_angle_queue.queue.clear()  # 清空队列
        self.thread_pool.start(self.angle_degree_thread)
        logger.info("后台获取机械臂角度启动!")
                
        # 启用轮询队列中所有命令的线程
        self.command_queue.queue.clear()  # 清空队列
        self.thread_pool.start(self.command_sender_thread)
        logger.info("命令发送线程启动!")
                
        # 启动命令接收线程
        self.thread_pool.start(self.command_recver_thread)
        logger.info("命令接收线程启动!")
        
    
    @logger.catch
    def get_robot_arm_connector(self):
        """获取与机械臂的连接对象"""
        try:
            socket_info = shelve.open(str(settings.IP_PORT_INFO_FILE_PATH))
            host = socket_info['target_ip']
            port = int(socket_info['target_port'])
            robot_arm_client = ClientSocket(host, port)
            socket_info.close()
        except Exception as e:
            logger.exception(str(e))
            self.message_box.error_message_box(message="没有读取到 ip 和 port 信息，请前往机械臂配置 !")
        return robot_arm_client
            
    
class BlinxRobotArmControlWindow(MSFluentWindow):
    """上位机主窗口"""    
    def __init__(self):
        super().__init__()
        self.command_queue = Queue()  # 控件发送的命令队列
        self.joints_angle_queue = Queue()  # 查询到关节角度信息的队列
        self.threadpool = QThreadPool()
        self.threadpool.globalInstance()
        self.commandInterface = CommandPage('命令控制')
        self.teachInterface = TeachPage('示教控制', self.threadpool, self.command_queue, self.joints_angle_queue)
        self.connectionInterface = ConnectPage('连接设置', self.threadpool, self.command_queue, self.joints_angle_queue)
        
        self.initNavigation()
        self.initWindow()
        
    def initWindow(self):
        """初始化窗口"""
        self.resize(1330, 750)
        self.setWindowTitle("比邻星六轴机械臂上位机 v4.3.1")
        self.setWindowIcon(QIcon(str(settings.WINDOWS_ICON_PATH)))
        setThemeColor('#00AAFF')
        
        # 根据屏幕大小居中显示
        desktop = QApplication.screens()[0].availableGeometry()
        w, h = desktop.width(), desktop.height()
        self.move(w//2 - self.width()//2, h//2 - self.height()//2)
    
    def initNavigation(self):
        """初始化导航栏"""
        self.addSubInterface(self.teachInterface, FIF.APPLICATION, '示教控制')
        self.addSubInterface(self.commandInterface, FIF.COMMAND_PROMPT, '命令控制')
        self.addSubInterface(self.connectionInterface, FIF.IOT, '连接设置')
        
        self.navigationInterface.addItem(
            routeKey='Help',
            icon=FIF.HELP,
            text='帮助',
            onClick=self.showMessageBox,
            selectable=False,
            position=NavigationItemPosition.BOTTOM
        )
        
        # 设置默认打开的页面
        self.navigationInterface.setCurrentItem(self.teachInterface.objectName())
    
    def showMessageBox(self):
        """弹出帮助信息框"""
        w = MessageBox(
            '📖帮助',
            '🎊欢迎使用比邻星六轴机械臂上位机 v4.3.1🎊\n\n👇使用文档请访问官网获取👇',
            self
        )
        w.yesButton.setText('直达官网🚀')
        w.cancelButton.setText('取消❌')
        if w.exec():
            QDesktopServices.openUrl(QUrl("http://www.blinx.cn/"))
    
    def closeEvent(self, e):
        pub.sendMessage("thread_work_flag", flag=False)
        pub.sendMessage("update_joint_angles_thread_flag", flag=False)
        logger.warning("程序退出")
        return super().closeEvent(e)    
    
    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = BlinxRobotArmControlWindow()
    w.show()
    app.exec()
    