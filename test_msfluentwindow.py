# -*- coding:utf-8 -*-
import sys
import json
import shelve
import sys
import time
from functools import partial
from queue import PriorityQueue
from retrying import retry

import common.settings as settings
from common.blinx_robot_module import Mirobot
from common.check_tools import check_robot_arm_connection
from common.socket_client import ClientSocket, Worker

# UI 相关模块
from PySide6.QtCore import Qt, QThreadPool, Slot
from PySide6.QtWidgets import (QApplication, QFrame, QMenu, QTableWidgetItem, QFileDialog)
from qfluentwidgets import (MSFluentWindow, CardWidget, ComboBox)
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
logger.add(settings.LOG_FILE_PATH, level="INFO")

# 三方通讯模块
from serial.tools import list_ports


class CommandPage(QFrame, command_page_frame):
    """命令控制页面"""
    def __init__(self, page_name: str, parent=None):
        super().__init__(parent=parent)
        self.setupUi(self)
        self.setObjectName(page_name.replace(' ', '-'))
        self.initButtonIcon()
        
    def initButtonIcon(self):
        """初始化按钮图标"""
        self.PushButton.setIcon(FIF.SEND)
        self.PushButton.setText('发送')


class TeachPage(QFrame, teach_page_frame):
    """示教控制页面"""
    def __init__(self, page_name: str, command_queue: PriorityQueue, command_response_queue: PriorityQueue, parent=None):
        super().__init__(parent=parent)
        self.setupUi(self)
        self.setObjectName(page_name.replace(' ', '-'))
        self.initButtonIcon()
        self.initJointControlWidiget()
        
        # 开启 QT 线程池
        self.threadpool = QThreadPool()
        self.threadpool.start(self.get_joint_angle_thread)
        
        self.command_queue = command_queue  # 控制命令队列
        self.command_response_queue = command_response_queue  # 控制命令响应队列
        self.blinx_robot_arm = Mirobot(settings.ROBOT_MODEL_CONFIG_FILE_PATH)
        self.message_box = BlinxMessageBox(self)
        
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
        
        # 示教控制页面
        self.tool_type = ["夹爪", "吸盘"]
        self.ArmToolOptions = self.ArmToolComboBox.addItems(self.tool_type)
        self.ArmToolComboBox.setCurrentText("吸盘")
        
        # 示教控制操作按钮槽函数绑定
        self.ActionImportButton.clicked.connect(self.import_data)
        self.ActionOutputButton.clicked.connect(self.export_data)
        # self.ActionStepRunButton.clicked.connect(self.run_action_step)
        # self.ActionRunButton.clicked.connect(self.run_all_action)
        # self.ActionLoopRunButton.clicked.connect(self.run_action_loop)
        self.ActionDeleteButton.clicked.connect(self.remove_item)
        self.ActionAddButton.clicked.connect(self.add_item)
        self.ActionUpdateRowButton.clicked.connect(self.update_row)
        self.ActionUpdateColButton.clicked.connect(self.update_column)  # 当前组件中无法选择列更新

        

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


        # # 实例化机械臂关节控制回调函数绑定
        
        self.JointOneAddButton.clicked.connect(partial(self.modify_joint_angle, 1, -140, 140, increase=True))
        self.JointOneSubButton.clicked.connect(partial(self.modify_joint_angle, 1, -140, 140, increase=False))
        self.JointTwoAddButton.clicked.connect(partial(self.modify_joint_angle, 2, -70, 70, increase=True))
        self.JointTwoSubButton.clicked.connect(partial(self.modify_joint_angle, 2, -70, 70, increase=False))
        self.JointThreeAddButton.clicked.connect(partial(self.modify_joint_angle, 3, -60, 45, increase=True))
        self.JointThreeSubButton.clicked.connect(partial(self.modify_joint_angle, 3, -60, 45, increase=False))
        self.JointFourAddButton.clicked.connect(partial(self.modify_joint_angle, 4, -150, 150, increase=True))
        self.JointFourSubButton.clicked.connect(partial(self.modify_joint_angle, 4, -150, 150, increase=False))
        self.JointFiveAddButton.clicked.connect(partial(self.modify_joint_angle, 5, -180, 10, increase=True))
        self.JointFiveSubButton.clicked.connect(partial(self.modify_joint_angle, 5, -180, 10, increase=False))
        self.JointSixAddButton.clicked.connect(partial(self.modify_joint_angle, 6, -180, 180, increase=True))
        self.JointSixSubButton.clicked.connect(partial(self.modify_joint_angle, 6, -180, 180, increase=False))
        self.JointStepAddButton.clicked.connect(partial(self.modify_joint_angle_step, increase=True))
        self.JointStepSubButton.clicked.connect(partial(self.modify_joint_angle_step, increase=False))
        self.JointSpeedUpButton.clicked.connect(partial(self.modify_joint_speed_percentage, increase=True))
        self.JointSpeedDecButton.clicked.connect(partial(self.modify_joint_speed_percentage, increase=False))
        self.JointDelayTimeAddButton.clicked.connect(partial(self.modify_joint_delay_time, increase=True))
        self.JointDelayTimeSubButton.clicked.connect(partial(self.modify_joint_delay_time, increase=False))

        
        # # 复位和急停按钮绑定
        self.RobotArmResetButton.clicked.connect(self.reset_robot_arm)
        self.RobotArmZeroButton.clicked.connect(self.reset_to_zero)
        # self.RobotArmStopButton.setEnabled(False) # 禁用急停按钮
        self.RobotArmStopButton.clicked.connect(self.stop_robot_arm)
        
        # # 末端工具控制组回调函数绑定
        # self.ArmClawOpenButton.clicked.connect(self.tool_open)
        # self.ArmClawCloseButton.clicked.connect(self.tool_close)
        
        # # 末端工具坐标增减回调函数绑定 
        # self.XAxisAddButton.clicked.connect(partial(self.tool_x_operate, action="add"))
        # self.XAxisSubButton.clicked.connect(partial(self.tool_x_operate, action="sub"))
        # self.YAxisAddButton.clicked.connect(partial(self.tool_y_operate, action="add"))
        # self.YAxisSubButton.clicked.connect(partial(self.tool_y_operate, action="sub"))
        # self.ZAxisAddButton.clicked.connect(partial(self.tool_z_operate, action="add"))
        # self.ZAxisSubButton.clicked.connect(partial(self.tool_z_operate, action="sub"))
        # self.CoordinateAddButton.clicked.connect(self.tool_coordinate_step_add)
        # self.CoordinateStepSubButton.clicked.connect(self.tool_coordinate_step_sub)
        
        # # 末端工具姿态增减回调函数绑定
        # self.RxAxisAddButton.clicked.connect(partial(self.tool_rx_operate, action="add"))
        # self.RxAxisSubButton.clicked.connect(partial(self.tool_rx_operate, action="sub"))
        # self.RyAxisAddButton.clicked.connect(partial(self.tool_ry_operate, action="add"))
        # self.RyAxisSubButton.clicked.connect(partial(self.tool_ry_operate, action="sub"))
        # self.RzAxisAddButton.clicked.connect(partial(self.tool_rz_operate, action="add"))
        # self.RzAxisSubButton.clicked.connect(partial(self.tool_rz_operate, action="sub"))
        # self.ApStepAddButton.clicked.connect(self.tool_pose_step_add)
        # self.ApStepSubButton.clicked.connect(self.tool_pose_step_sub)

    # 顶部工具栏
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
                    logger.info("完成导入动作文件!")
            else:
                logger.warning("取消导入动作文件!")
        except Exception as e:
            logger.error(f"导入动作文件失败: {e}")
            self.message_box.error_message_box(message="导入动作文件失败!")
            
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

            with open(file_name, "w", encoding="utf-8") as json_file:
                json.dump(data, json_file, indent=4, ensure_ascii=False)
                logger.info("导出配置文件成功!")
    
    @Slot()
    def add_item(self):
        """示教控制添加一行动作"""
        speed_percentage = self.JointSpeedEdit.text()  # 速度值，暂定百分比
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

    @Slot()
    def update_row(self):
        """示教控制更新指定行的动作"""
        selected_rows = self.ActionTableWidget.selectionModel().selectedRows()
        if selected_rows:
            for row in selected_rows:
                for col in range(self.ActionTableWidget.columnCount()):
                    if col == 0:
                        self.update_table_cell(row.row(), col, round(self.q1, 2))
                    elif col == 1:
                        self.update_table_cell(row.row(), col, round(self.q2, 2))
                    elif col == 2:
                        self.update_table_cell(row.row(), col, round(self.q3, 2))
                    elif col == 3:
                        self.update_table_cell(row.row(), col, round(self.q4, 2))
                    elif col == 4:
                        self.update_table_cell(row.row(), col, round(self.q5, 2))
                    elif col == 5:
                        self.update_table_cell(row.row(), col, round(self.q6, 2))
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
    
    @Slot()
    def update_column(self):
        """更新选中的列"""
        selected_columns = self.ActionTableWidget.selectionModel().selectedColumns()
        if selected_columns:
            for col in selected_columns:
                column_number = col.column()
                for row in range(self.ActionTableWidget.rowCount()):
                    if column_number == 0:
                        self.update_table_cell(row, column_number, round(self.q1, 2))
                    elif column_number == 1:
                        self.update_table_cell(row, column_number, round(self.q2, 2))
                    elif column_number == 2:
                        self.update_table_cell(row, column_number, round(self.q3, 2))
                    elif column_number == 3:
                        self.update_table_cell(row, column_number, round(self.q4, 2))
                    elif column_number == 4:
                        self.update_table_cell(row, column_number, round(self.q5, 2))
                    elif column_number == 5:
                        self.update_table_cell(row, column_number, round(self.q6, 2))
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
                self.update_table_cell(selected_row, sellected_col, round(self.q1, 2))
            elif sellected_col == 1:
                self.update_table_cell(selected_row, sellected_col, round(self.q2, 2))
            elif sellected_col == 2:
                self.update_table_cell(selected_row, sellected_col, round(self.q3, 2))
            elif sellected_col == 3:
                self.update_table_cell(selected_row, sellected_col, round(self.q4, 2))
            elif sellected_col == 4:
                self.update_table_cell(selected_row, sellected_col, round(self.q5, 2))
            elif sellected_col == 5:
                self.update_table_cell(selected_row, sellected_col, round(self.q6, 2))
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
                    self.update_table_cell(row_position, col, round(self.q1, 2))
                elif col == 1:
                    self.update_table_cell(row_position, col, round(self.q2, 2))
                elif col == 2:
                    self.update_table_cell(row_position, col, round(self.q3, 2))
                elif col == 3:
                    self.update_table_cell(row_position, col, round(self.q4, 2))
                elif col == 4:
                    self.update_table_cell(row_position, col, round(self.q5, 2))
                elif col == 5:
                    self.update_table_cell(row_position, col, round(self.q6, 2))
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
    
    @Slot()
    def modify_joint_angle(self, joint_number, min_degrade, max_degrade, increase=True):
        """机械臂关节角度增减操作"""
        old_degrade = getattr(self, f'q{joint_number}')  # 获取当前对象的属性
        step_degrade = float(self.JointStepEdit.text().strip())
        speed_percentage = float(self.JointSpeedEdit.text().strip())

        if increase:
            degrade = old_degrade + step_degrade
        else:
            degrade = old_degrade - step_degrade

        joint_name_mapping = {1: 'One', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five', 6: 'Six'}
        getattr(self, f'Joint{joint_name_mapping[joint_number]}Edit').setText(str(degrade))  # 更新关节角度值

        if degrade < min_degrade or degrade > max_degrade:
            self.message_box.error_message_box(message=f"关节角度超出范围: {min_degrade} ~ {max_degrade}")
        else:
            # 使用线性回归方程限制关节角度
            degrade = np.clip(degrade, min_degrade, max_degrade)

            # 构造发送命令
            command = json.dumps(
                {"command": "set_joint_angle_speed_percentage", "data": [2, degrade, speed_percentage]}) + '\r\n'
            self.command_queue.put((1.5, command.encode()))
            
            #  录制操作激活时
            if self.RecordActivateButton.isChecked():
                self.add_item()
    
    @Slot()
    def modify_joint_angle_step(self, increase=True):
        """修改机械臂关节步长"""
        old_degrade = int(self.JointStepEdit.text().strip())
        degrade = old_degrade + 5 if increase else old_degrade - 5
        if 0 < degrade <= 20:
            self.JointStepEdit.setText(str(degrade))
        else:
            message = "步长不能超过 20" if increase else "步长不能为负!"
            self.message_box.warning_message_box(message=message)
    
    @Slot()
    def modify_joint_speed_percentage(self, increase=True):
        """修改关节运动速度百分比"""
        speed_percentage_edit = self.JointSpeedEdit.text()
        if speed_percentage_edit is not None and speed_percentage_edit.isdigit():
            old_speed_percentage = int(speed_percentage_edit.strip())
            new_speed_percentage = old_speed_percentage + 5 if increase else old_speed_percentage - 5
            if 0 <= new_speed_percentage <= 100:
                self.JointSpeedEdit.setText(str(new_speed_percentage))
            else:
                self.message_box.warning_message_box(message=f"关节速度范围 0 ~ 100")
        else:
            self.message_box.error_message_box(message="请输入整数字符!")

    @Slot()
    def modify_joint_delay_time(self, increase=True):
        """修改机械臂延时时间"""
        delay_time_edit = self.JointDelayTimeEdit.text()
        if delay_time_edit is not None and delay_time_edit.isdigit():
            old_delay_time = int(delay_time_edit.strip())
            new_delay_time = old_delay_time + 1 if increase else old_delay_time - 1
            if 0 <= new_delay_time <= 100:
                self.JointDelayTimeEdit.setText(str(new_delay_time))
            else:
                self.message_box.warning_message_box(message=f"延时时间必须在 0-100s 之间")
        else:
            self.message_box.error_message_box(message="请输入整数字符!")
              
    @Slot()
    def reset_robot_arm(self):
        """机械臂复位
        :param mode:
        """
        command = json.dumps({"command": "set_joint_Auto_zero"}).replace('', "") + '\r\n'
        self.command_queue.put((1, command.encode()))
        self.message_box.warning_message_box("机械臂复位中!\n请注意手臂姿态")
        logger.warning("机械臂复位中!请注意手臂姿态")
        
    @Slot()
    def reset_to_zero(self):
        """机械臂复位到零点"""
        command = json.dumps({"command": "set_joint_angle_all_time", "data": [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0, 35]}).replace(' ', "") + '\r\n'
        self.command_queue.put((1, command.encode()))
        self.message_box.warning_message_box("机械臂回到初始角度中!\n请注意手臂姿态")
        logger.warning("机械臂回到初始角度中!")
        
    # 机械臂急停按钮回调函数
    @Slot()
    def stop_robot_arm(self):
        """机械臂急停"""
        # 线程标志设置为停止
        self.loop_flag = True
        # 清空队列中的命令
        self.command_queue.queue.clear()
        # 恢复连接机械臂按钮
        # self.RobotArmLinkButton.setText("连接机械臂")
        # self.RobotArmLinkButton.setEnabled(True)
        # 禁用急停按钮
        self.RobotArmStopButton.setEnabled(False)
        
        self.message_box.error_message_box("机械臂急停!")
        self.loop_flag = False  # 恢复线程池的初始标志位
        self.robot_arm_is_connected = False # 机械臂连接标志位设置为 False
    
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
        self.addSubInterface(self.ArmEndToolsCoordinateControlCard, 'ArmEndToolsCoordinateControlCard', '工具坐标控制')
        self.addSubInterface(self.ArmEndToolsPositionControlCard, 'ArmEndToolsPositionControlCard', '工具姿态控制')

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
        self.ActionRunButton.setIcon(FIF.PLAY)
        self.ActionStepRunButton.setIcon(FIF.ALIGNMENT)
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
        self.ApStepAddButton.setIcon(FIF.ADD)
        self.ApStepSubButton.setIcon(FIF.REMOVE)
    
    def get_joint_angle_thread(self):
        """后台更新各个关节角度"""
        # 从 command_response_queue 中获取机械臂的关节角度信息
        logger.info("获取机械臂的关节角度信息线程启动!")
        while True:
            if not self.command_response_queue.empty():
                angle_data_list = self.command_response_queue.get()
                self.q1, self.q2, self.q3, self.q4, self.q5, self.q6 = angle_data_list[1]
                self.update_joint_degrees_text()
                
                # 更新机械臂末端工具的坐标和姿态值
                arm_joint_radians = np.radians(angle_data_list[1])
                translation_vector = self.blinx_robot_arm.fkine(arm_joint_radians)
                self.X, self.Y, self.Z = translation_vector.t  # 末端坐标
                self.rz, self.ry, self.rx = translation_vector.rpy(unit='deg')  # 末端姿态
                self.update_arm_pose_text()
                
            time.sleep(0.1)
            
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
        self.JointOneEdit.setText(display_q1)
        self.JointTwoEdit.setText(display_q2)
        self.JointThreeEdit.setText(display_q3)
        self.JointFourEdit.setText(display_q4)
        self.JointFiveEdit.setText(display_q5)
        self.JointSixEdit.setText(display_q6)
        logger.debug(f"显示的角度值: {[display_q1, display_q2, display_q3, display_q4, display_q5, display_q6]}")
    
    def update_arm_pose_text(self):
        """更新界面上机械臂末端工具的坐标和姿态值"""
        self.XAxisEdit.setText(str(round(self.X, 3)))
        self.YAxisEdit.setText(str(round(self.Y, 3)))
        self.ZAxisEdit.setText(str(round(self.Z, 3)))
        self.RxAxisEdit.setText(str(round(self.rx, 3)))
        self.RyAxisEdit.setText(str(round(self.ry, 3)))
        self.RzAxisEdit.setText(str(round(self.rz, 3)))
        
        
class ConnectPage(QFrame, connect_page_frame):
    """连接配置页面"""
    def __init__(self, page_name: str, command_queue: PriorityQueue, command_response_queue: PriorityQueue, parent=None):
        super().__init__(parent=parent)
        self.setupUi(self)
        self.setObjectName(page_name.replace(' ', '-'))
        self.reload_ip_port_history()  # 加载上一次的配置
        
        # 开启 QT 线程池
        self.threadpool = QThreadPool()
        self.command_queue = command_queue
        self.command_response_queue = command_response_queue
        
        # 机械臂的查询循环控制位
        self.loop_flag = False
        self.robot_arm_is_connected = False
        
        self.message_box = BlinxMessageBox(self)
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
        
        # self.initialize_values()
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
                # self.RobotArmStopButton.setEnabled(True)
                
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
    
    @retry(stop_max_attempt_number=3, wait_fixed=1000)
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
            logger.error(str(e))
            self.message_box.error_message_box(message="没有读取到 ip 和 port 信息，请前往机械臂配置 !")
        return robot_arm_client
    
    @logger.catch
    def get_angle_value(self):
        """实时获取关节的角度值"""        
        while not self.loop_flag:
            command = json.dumps({"command": "get_joint_angle_all"}).replace(' ',"") + '\r\n'
            self.command_queue.put((3, command.encode()))
            time.sleep(1)

    
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
                            self.command_response_queue.put((1, angle_data_list))
                            
                    except Exception as e:
                        logger.warning(f"命令处理异常: {e}")
                        continue
            time.sleep(0.1)
                         
                       
class BlinxRobotArmControlWindow(MSFluentWindow):
    """上位机主窗口"""    
    def __init__(self):
        super().__init__()
        self.command_queue = PriorityQueue()  # 控件发送的命令队列
        self.response_queue = PriorityQueue()  # 接收响应的命令队列
        self.commandInterface = CommandPage('命令控制', self)
        self.teachInterface = TeachPage('示教控制', self.command_queue, self.response_queue, self)
        self.connectionInterface = ConnectPage('连接设置', self.command_queue, self.response_queue, self)
        
        self.initNavigation()
        self.initWindow()
        
        
    def initWindow(self):
        """初始化窗口"""
        self.resize(1394, 750)
        self.setWindowTitle("比邻星六轴机械臂上位机")
        
        # 根据屏幕大小居中显示
        desktop = QApplication.screens()[0].availableGeometry()
        w, h = desktop.width(), desktop.height()
        self.move(w//2 - self.width()//2, h//2 - self.height()//2)
    
    def initNavigation(self):
        """初始化导航栏"""
        self.addSubInterface(self.commandInterface, FIF.COMMAND_PROMPT, '命令控制')
        self.addSubInterface(self.teachInterface, FIF.APPLICATION, '示教控制')
        self.addSubInterface(self.connectionInterface, FIF.IOT, '连接设置')
        
        # 设置默认打开的页面
        self.navigationInterface.setCurrentItem(self.commandInterface.objectName())
    
    def closeEvent(self, event):
        """用户触发窗口关闭事件，所有线程标志位为退出"""
        self.loop_flag = True
        logger.info("比邻星六轴机械臂上位机窗口关闭！")
        event.accept()
    
    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = BlinxRobotArmControlWindow()
    w.show()
    app.exec()
    