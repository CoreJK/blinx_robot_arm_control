# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'BLinx_Robot_Arm_ui.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1476, 682)
        self.HomePage = QTabWidget(Form)
        self.HomePage.setObjectName(u"HomePage")
        self.HomePage.setGeometry(QRect(8, 59, 971, 591))
        self.HomePage.setTabPosition(QTabWidget.West)
        self.HomePage.setTabShape(QTabWidget.Rounded)
        self.HomePage.setIconSize(QSize(16, 16))
        self.HomePage.setElideMode(Qt.ElideNone)
        self.HomePage.setTabsClosable(False)
        self.HomePage.setTabBarAutoHide(False)
        self.CommandPage = QWidget()
        self.CommandPage.setObjectName(u"CommandPage")
        self.CommandEditWindow = QTextEdit(self.CommandPage)
        self.CommandEditWindow.setObjectName(u"CommandEditWindow")
        self.CommandEditWindow.setGeometry(QRect(20, 507, 771, 51))
        self.CommandSendButton = QPushButton(self.CommandPage)
        self.CommandSendButton.setObjectName(u"CommandSendButton")
        self.CommandSendButton.setGeometry(QRect(800, 507, 121, 51))
        self.SendLabel = QLabel(self.CommandPage)
        self.SendLabel.setObjectName(u"SendLabel")
        self.SendLabel.setGeometry(QRect(20, 11, 54, 12))
        self.ResponseLabel = QLabel(self.CommandPage)
        self.ResponseLabel.setObjectName(u"ResponseLabel")
        self.ResponseLabel.setGeometry(QRect(20, 178, 54, 12))
        self.CommandArmRunLogLabel = QLabel(self.CommandPage)
        self.CommandArmRunLogLabel.setObjectName(u"CommandArmRunLogLabel")
        self.CommandArmRunLogLabel.setGeometry(QRect(20, 340, 91, 16))
        self.CommandArmRunLogWindow = QTextBrowser(self.CommandPage)
        self.CommandArmRunLogWindow.setObjectName(u"CommandArmRunLogWindow")
        self.CommandArmRunLogWindow.setGeometry(QRect(19, 366, 901, 131))
        self.CommandResWindow = QTextBrowser(self.CommandPage)
        self.CommandResWindow.setObjectName(u"CommandResWindow")
        self.CommandResWindow.setGeometry(QRect(18, 195, 901, 141))
        self.CommandSendWindow = QTextBrowser(self.CommandPage)
        self.CommandSendWindow.setObjectName(u"CommandSendWindow")
        self.CommandSendWindow.setGeometry(QRect(20, 31, 901, 141))
        self.HomePage.addTab(self.CommandPage, "")
        self.HelpTeachPage = QWidget()
        self.HelpTeachPage.setObjectName(u"HelpTeachPage")
        self.ActionTableWidget = QTableWidget(self.HelpTeachPage)
        if (self.ActionTableWidget.columnCount() < 11):
            self.ActionTableWidget.setColumnCount(11)
        __qtablewidgetitem = QTableWidgetItem()
        self.ActionTableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.ActionTableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.ActionTableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.ActionTableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.ActionTableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.ActionTableWidget.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.ActionTableWidget.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.ActionTableWidget.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.ActionTableWidget.setHorizontalHeaderItem(8, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.ActionTableWidget.setHorizontalHeaderItem(9, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.ActionTableWidget.setHorizontalHeaderItem(10, __qtablewidgetitem10)
        self.ActionTableWidget.setObjectName(u"ActionTableWidget")
        self.ActionTableWidget.setGeometry(QRect(20, 40, 901, 361))
        self.TeachArmRunLogLabel = QLabel(self.HelpTeachPage)
        self.TeachArmRunLogLabel.setObjectName(u"TeachArmRunLogLabel")
        self.TeachArmRunLogLabel.setGeometry(QRect(24, 444, 91, 16))
        self.ActionDeleteButton = QPushButton(self.HelpTeachPage)
        self.ActionDeleteButton.setObjectName(u"ActionDeleteButton")
        self.ActionDeleteButton.setGeometry(QRect(20, 410, 91, 23))
        self.ActionPastButton = QPushButton(self.HelpTeachPage)
        self.ActionPastButton.setObjectName(u"ActionPastButton")
        self.ActionPastButton.setGeometry(QRect(821, 410, 91, 23))
        self.ActionCopyButton = QPushButton(self.HelpTeachPage)
        self.ActionCopyButton.setObjectName(u"ActionCopyButton")
        self.ActionCopyButton.setGeometry(QRect(710, 410, 91, 23))
        self.ActionAddButton = QPushButton(self.HelpTeachPage)
        self.ActionAddButton.setObjectName(u"ActionAddButton")
        self.ActionAddButton.setGeometry(QRect(490, 410, 91, 23))
        self.ActionRunButton = QPushButton(self.HelpTeachPage)
        self.ActionRunButton.setObjectName(u"ActionRunButton")
        self.ActionRunButton.setGeometry(QRect(480, 10, 101, 23))
        self.ActionStepRunButton = QPushButton(self.HelpTeachPage)
        self.ActionStepRunButton.setObjectName(u"ActionStepRunButton")
        self.ActionStepRunButton.setGeometry(QRect(600, 10, 91, 23))
        self.ActionUpdateButton = QPushButton(self.HelpTeachPage)
        self.ActionUpdateButton.setObjectName(u"ActionUpdateButton")
        self.ActionUpdateButton.setGeometry(QRect(600, 410, 91, 23))
        self.ActionLoopRunButton = QPushButton(self.HelpTeachPage)
        self.ActionLoopRunButton.setObjectName(u"ActionLoopRunButton")
        self.ActionLoopRunButton.setGeometry(QRect(714, 10, 91, 23))
        self.ActionLoopTimes = QLineEdit(self.HelpTeachPage)
        self.ActionLoopTimes.setObjectName(u"ActionLoopTimes")
        self.ActionLoopTimes.setGeometry(QRect(820, 10, 91, 20))
        self.ActionImportButton = QPushButton(self.HelpTeachPage)
        self.ActionImportButton.setObjectName(u"ActionImportButton")
        self.ActionImportButton.setGeometry(QRect(20, 10, 91, 23))
        self.ActionOutputButton = QPushButton(self.HelpTeachPage)
        self.ActionOutputButton.setObjectName(u"ActionOutputButton")
        self.ActionOutputButton.setGeometry(QRect(130, 9, 91, 23))
        self.TeachArmRunLogWindow = QTextBrowser(self.HelpTeachPage)
        self.TeachArmRunLogWindow.setObjectName(u"TeachArmRunLogWindow")
        self.TeachArmRunLogWindow.setGeometry(QRect(20, 460, 891, 101))
        self.HomePage.addTab(self.HelpTeachPage, "")
        self.SettingPage = QWidget()
        self.SettingPage.setObjectName(u"SettingPage")
        self.IpPortInfoGroup = QGroupBox(self.SettingPage)
        self.IpPortInfoGroup.setObjectName(u"IpPortInfoGroup")
        self.IpPortInfoGroup.setGeometry(QRect(20, 20, 901, 151))
        self.IpPortInfoSubmitButton = QPushButton(self.IpPortInfoGroup)
        self.IpPortInfoSubmitButton.setObjectName(u"IpPortInfoSubmitButton")
        self.IpPortInfoSubmitButton.setGeometry(QRect(490, 90, 75, 23))
        self.TargetPortLabel = QLabel(self.IpPortInfoGroup)
        self.TargetPortLabel.setObjectName(u"TargetPortLabel")
        self.TargetPortLabel.setGeometry(QRect(370, 64, 54, 12))
        self.TargetPortEdit = QLineEdit(self.IpPortInfoGroup)
        self.TargetPortEdit.setObjectName(u"TargetPortEdit")
        self.TargetPortEdit.setGeometry(QRect(433, 60, 131, 20))
        self.TargetIpEdit = QLineEdit(self.IpPortInfoGroup)
        self.TargetIpEdit.setObjectName(u"TargetIpEdit")
        self.TargetIpEdit.setGeometry(QRect(433, 30, 131, 20))
        self.IpPortInfoRestButton = QPushButton(self.IpPortInfoGroup)
        self.IpPortInfoRestButton.setObjectName(u"IpPortInfoRestButton")
        self.IpPortInfoRestButton.setGeometry(QRect(401, 90, 75, 23))
        self.TargetIpLabel = QLabel(self.IpPortInfoGroup)
        self.TargetIpLabel.setObjectName(u"TargetIpLabel")
        self.TargetIpLabel.setGeometry(QRect(370, 35, 54, 12))
        self.WiFiInfoGroup = QGroupBox(self.SettingPage)
        self.WiFiInfoGroup.setObjectName(u"WiFiInfoGroup")
        self.WiFiInfoGroup.setGeometry(QRect(20, 190, 901, 151))
        self.WiFiInfoSubmit = QPushButton(self.WiFiInfoGroup)
        self.WiFiInfoSubmit.setObjectName(u"WiFiInfoSubmit")
        self.WiFiInfoSubmit.setGeometry(QRect(490, 90, 75, 23))
        self.WiFiPasswdLabel = QLabel(self.WiFiInfoGroup)
        self.WiFiPasswdLabel.setObjectName(u"WiFiPasswdLabel")
        self.WiFiPasswdLabel.setGeometry(QRect(370, 63, 61, 16))
        self.WiFiPasswdEdit = QLineEdit(self.WiFiInfoGroup)
        self.WiFiPasswdEdit.setObjectName(u"WiFiPasswdEdit")
        self.WiFiPasswdEdit.setGeometry(QRect(440, 60, 131, 20))
        self.WiFiSsidEdit = QLineEdit(self.WiFiInfoGroup)
        self.WiFiSsidEdit.setObjectName(u"WiFiSsidEdit")
        self.WiFiSsidEdit.setGeometry(QRect(440, 30, 131, 20))
        self.WiFiInfoReset = QPushButton(self.WiFiInfoGroup)
        self.WiFiInfoReset.setObjectName(u"WiFiInfoReset")
        self.WiFiInfoReset.setGeometry(QRect(401, 90, 75, 23))
        self.WiFiSsidLabel = QLabel(self.WiFiInfoGroup)
        self.WiFiSsidLabel.setObjectName(u"WiFiSsidLabel")
        self.WiFiSsidLabel.setGeometry(QRect(370, 35, 61, 16))
        self.SbInfoGroup = QGroupBox(self.SettingPage)
        self.SbInfoGroup.setObjectName(u"SbInfoGroup")
        self.SbInfoGroup.setGeometry(QRect(20, 360, 901, 151))
        self.SbInfoSubmitButton = QPushButton(self.SbInfoGroup)
        self.SbInfoSubmitButton.setObjectName(u"SbInfoSubmitButton")
        self.SbInfoSubmitButton.setGeometry(QRect(490, 90, 75, 23))
        self.BaudRatesLabel = QLabel(self.SbInfoGroup)
        self.BaudRatesLabel.setObjectName(u"BaudRatesLabel")
        self.BaudRatesLabel.setGeometry(QRect(380, 64, 54, 12))
        self.SbInfoFreshButton = QPushButton(self.SbInfoGroup)
        self.SbInfoFreshButton.setObjectName(u"SbInfoFreshButton")
        self.SbInfoFreshButton.setGeometry(QRect(401, 90, 75, 23))
        self.SerialNumLabel = QLabel(self.SbInfoGroup)
        self.SerialNumLabel.setObjectName(u"SerialNumLabel")
        self.SerialNumLabel.setGeometry(QRect(380, 35, 54, 12))
        self.SerialNumComboBox = QComboBox(self.SbInfoGroup)
        self.SerialNumComboBox.setObjectName(u"SerialNumComboBox")
        self.SerialNumComboBox.setGeometry(QRect(440, 30, 131, 22))
        self.BaudRatesComboBox = QComboBox(self.SbInfoGroup)
        self.BaudRatesComboBox.addItem("")
        self.BaudRatesComboBox.addItem("")
        self.BaudRatesComboBox.setObjectName(u"BaudRatesComboBox")
        self.BaudRatesComboBox.setGeometry(QRect(440, 60, 131, 22))
        self.RobotArmLinkButton = QPushButton(self.SettingPage)
        self.RobotArmLinkButton.setObjectName(u"RobotArmLinkButton")
        self.RobotArmLinkButton.setGeometry(QRect(420, 520, 161, 31))
        self.HomePage.addTab(self.SettingPage, "")
        self.SystemInfoPage = QWidget()
        self.SystemInfoPage.setObjectName(u"SystemInfoPage")
        self.groupBox = QGroupBox(self.SystemInfoPage)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(10, 13, 911, 151))
        self.RobotArmInfoGroup = QGroupBox(self.SystemInfoPage)
        self.RobotArmInfoGroup.setObjectName(u"RobotArmInfoGroup")
        self.RobotArmInfoGroup.setGeometry(QRect(10, 195, 911, 151))
        self.SoftInfoGroup = QGroupBox(self.SystemInfoPage)
        self.SoftInfoGroup.setObjectName(u"SoftInfoGroup")
        self.SoftInfoGroup.setGeometry(QRect(10, 370, 911, 151))
        self.HomePage.addTab(self.SystemInfoPage, "")
        self.RobotArmToolsGrop = QGroupBox(Form)
        self.RobotArmToolsGrop.setObjectName(u"RobotArmToolsGrop")
        self.RobotArmToolsGrop.setGeometry(QRect(990, 430, 241, 121))
        self.ArmClawCloseButton = QPushButton(self.RobotArmToolsGrop)
        self.ArmClawCloseButton.setObjectName(u"ArmClawCloseButton")
        self.ArmClawCloseButton.setGeometry(QRect(150, 70, 51, 31))
        self.ArmControlLabel = QLabel(self.RobotArmToolsGrop)
        self.ArmControlLabel.setObjectName(u"ArmControlLabel")
        self.ArmControlLabel.setGeometry(QRect(30, 80, 31, 16))
        self.ArmClawOpenButton = QPushButton(self.RobotArmToolsGrop)
        self.ArmClawOpenButton.setObjectName(u"ArmClawOpenButton")
        self.ArmClawOpenButton.setGeometry(QRect(90, 70, 51, 31))
        self.ArmToolLabel = QLabel(self.RobotArmToolsGrop)
        self.ArmToolLabel.setObjectName(u"ArmToolLabel")
        self.ArmToolLabel.setGeometry(QRect(30, 43, 31, 16))
        self.ArmToolComboBox = QComboBox(self.RobotArmToolsGrop)
        self.ArmToolComboBox.addItem("")
        self.ArmToolComboBox.addItem("")
        self.ArmToolComboBox.addItem("")
        self.ArmToolComboBox.setObjectName(u"ArmToolComboBox")
        self.ArmToolComboBox.setGeometry(QRect(90, 40, 111, 21))
        self.RobotArmPositionControlGroup = QGroupBox(Form)
        self.RobotArmPositionControlGroup.setObjectName(u"RobotArmPositionControlGroup")
        self.RobotArmPositionControlGroup.setGeometry(QRect(1240, 60, 221, 181))
        self.ZAxisAddButton = QPushButton(self.RobotArmPositionControlGroup)
        self.ZAxisAddButton.setObjectName(u"ZAxisAddButton")
        self.ZAxisAddButton.setGeometry(QRect(160, 130, 51, 31))
        self.XAxisEdit = QLineEdit(self.RobotArmPositionControlGroup)
        self.XAxisEdit.setObjectName(u"XAxisEdit")
        self.XAxisEdit.setGeometry(QRect(100, 50, 51, 31))
        self.YAxisAddButton = QPushButton(self.RobotArmPositionControlGroup)
        self.YAxisAddButton.setObjectName(u"YAxisAddButton")
        self.YAxisAddButton.setGeometry(QRect(160, 90, 51, 31))
        self.Zlable = QLabel(self.RobotArmPositionControlGroup)
        self.Zlable.setObjectName(u"Zlable")
        self.Zlable.setGeometry(QRect(14, 140, 20, 20))
        self.YLable = QLabel(self.RobotArmPositionControlGroup)
        self.YLable.setObjectName(u"YLable")
        self.YLable.setGeometry(QRect(13, 100, 21, 20))
        self.XAxisSubButton = QPushButton(self.RobotArmPositionControlGroup)
        self.XAxisSubButton.setObjectName(u"XAxisSubButton")
        self.XAxisSubButton.setGeometry(QRect(40, 50, 51, 31))
        self.YAxisEdit = QLineEdit(self.RobotArmPositionControlGroup)
        self.YAxisEdit.setObjectName(u"YAxisEdit")
        self.YAxisEdit.setGeometry(QRect(100, 90, 51, 31))
        self.YAxisSubButton = QPushButton(self.RobotArmPositionControlGroup)
        self.YAxisSubButton.setObjectName(u"YAxisSubButton")
        self.YAxisSubButton.setGeometry(QRect(40, 90, 51, 31))
        self.ZAxisEdit = QLineEdit(self.RobotArmPositionControlGroup)
        self.ZAxisEdit.setObjectName(u"ZAxisEdit")
        self.ZAxisEdit.setGeometry(QRect(100, 130, 51, 31))
        self.XLable = QLabel(self.RobotArmPositionControlGroup)
        self.XLable.setObjectName(u"XLable")
        self.XLable.setGeometry(QRect(13, 60, 21, 20))
        self.ZAxisSubButton = QPushButton(self.RobotArmPositionControlGroup)
        self.ZAxisSubButton.setObjectName(u"ZAxisSubButton")
        self.ZAxisSubButton.setGeometry(QRect(40, 130, 51, 31))
        self.XAxisAddButton = QPushButton(self.RobotArmPositionControlGroup)
        self.XAxisAddButton.setObjectName(u"XAxisAddButton")
        self.XAxisAddButton.setGeometry(QRect(160, 50, 51, 31))
        self.RobotArmControlGroup = QGroupBox(Form)
        self.RobotArmControlGroup.setObjectName(u"RobotArmControlGroup")
        self.RobotArmControlGroup.setGeometry(QRect(990, 60, 241, 361))
        self.AngleOneSubButton = QPushButton(self.RobotArmControlGroup)
        self.AngleOneSubButton.setObjectName(u"AngleOneSubButton")
        self.AngleOneSubButton.setGeometry(QRect(61, 40, 51, 31))
        self.AngleOneSubButton.setAutoFillBackground(False)
        self.AngleOneLabel = QLabel(self.RobotArmControlGroup)
        self.AngleOneLabel.setObjectName(u"AngleOneLabel")
        self.AngleOneLabel.setGeometry(QRect(17, 46, 41, 20))
        self.AngleFourAddButton = QPushButton(self.RobotArmControlGroup)
        self.AngleFourAddButton.setObjectName(u"AngleFourAddButton")
        self.AngleFourAddButton.setGeometry(QRect(181, 160, 51, 31))
        self.AngleTwoSubButton = QPushButton(self.RobotArmControlGroup)
        self.AngleTwoSubButton.setObjectName(u"AngleTwoSubButton")
        self.AngleTwoSubButton.setGeometry(QRect(61, 80, 51, 31))
        self.AngleFourSubButton = QPushButton(self.RobotArmControlGroup)
        self.AngleFourSubButton.setObjectName(u"AngleFourSubButton")
        self.AngleFourSubButton.setGeometry(QRect(61, 160, 51, 31))
        self.AngleSixSubButton = QPushButton(self.RobotArmControlGroup)
        self.AngleSixSubButton.setObjectName(u"AngleSixSubButton")
        self.AngleSixSubButton.setGeometry(QRect(61, 240, 51, 31))
        self.AngleSixLabel = QLabel(self.RobotArmControlGroup)
        self.AngleSixLabel.setObjectName(u"AngleSixLabel")
        self.AngleSixLabel.setGeometry(QRect(17, 246, 41, 20))
        self.AngleSixAddButton = QPushButton(self.RobotArmControlGroup)
        self.AngleSixAddButton.setObjectName(u"AngleSixAddButton")
        self.AngleSixAddButton.setGeometry(QRect(181, 240, 51, 31))
        self.ArmSpeedLabel = QLabel(self.RobotArmControlGroup)
        self.ArmSpeedLabel.setObjectName(u"ArmSpeedLabel")
        self.ArmSpeedLabel.setGeometry(QRect(18, 324, 41, 20))
        self.ArmSpeedEdit = QLineEdit(self.RobotArmControlGroup)
        self.ArmSpeedEdit.setObjectName(u"ArmSpeedEdit")
        self.ArmSpeedEdit.setGeometry(QRect(121, 320, 51, 31))
        self.AngleOneAddButton = QPushButton(self.RobotArmControlGroup)
        self.AngleOneAddButton.setObjectName(u"AngleOneAddButton")
        self.AngleOneAddButton.setGeometry(QRect(181, 40, 51, 31))
        self.AngleStepAddButton = QPushButton(self.RobotArmControlGroup)
        self.AngleStepAddButton.setObjectName(u"AngleStepAddButton")
        self.AngleStepAddButton.setGeometry(QRect(181, 280, 51, 31))
        self.AngleFiveEdit = QLineEdit(self.RobotArmControlGroup)
        self.AngleFiveEdit.setObjectName(u"AngleFiveEdit")
        self.AngleFiveEdit.setGeometry(QRect(121, 200, 51, 31))
        self.AngleThreeLabel = QLabel(self.RobotArmControlGroup)
        self.AngleThreeLabel.setObjectName(u"AngleThreeLabel")
        self.AngleThreeLabel.setGeometry(QRect(18, 125, 41, 20))
        self.AngleTwoEdit = QLineEdit(self.RobotArmControlGroup)
        self.AngleTwoEdit.setObjectName(u"AngleTwoEdit")
        self.AngleTwoEdit.setGeometry(QRect(121, 80, 51, 31))
        self.AngleSixEdit = QLineEdit(self.RobotArmControlGroup)
        self.AngleSixEdit.setObjectName(u"AngleSixEdit")
        self.AngleSixEdit.setGeometry(QRect(121, 240, 51, 31))
        self.ArmSpeedUpButton = QPushButton(self.RobotArmControlGroup)
        self.ArmSpeedUpButton.setObjectName(u"ArmSpeedUpButton")
        self.ArmSpeedUpButton.setGeometry(QRect(181, 320, 51, 31))
        self.AngleThreeEdit = QLineEdit(self.RobotArmControlGroup)
        self.AngleThreeEdit.setObjectName(u"AngleThreeEdit")
        self.AngleThreeEdit.setGeometry(QRect(121, 120, 51, 31))
        self.AngleFiveSubButton = QPushButton(self.RobotArmControlGroup)
        self.AngleFiveSubButton.setObjectName(u"AngleFiveSubButton")
        self.AngleFiveSubButton.setGeometry(QRect(61, 200, 51, 31))
        self.AngleFourEdit = QLineEdit(self.RobotArmControlGroup)
        self.AngleFourEdit.setObjectName(u"AngleFourEdit")
        self.AngleFourEdit.setGeometry(QRect(121, 160, 51, 31))
        self.AngleOneEdit = QLineEdit(self.RobotArmControlGroup)
        self.AngleOneEdit.setObjectName(u"AngleOneEdit")
        self.AngleOneEdit.setGeometry(QRect(121, 40, 51, 31))
        self.AngleStepSubButton = QPushButton(self.RobotArmControlGroup)
        self.AngleStepSubButton.setObjectName(u"AngleStepSubButton")
        self.AngleStepSubButton.setGeometry(QRect(61, 280, 51, 31))
        self.ArmSpeedDecButton = QPushButton(self.RobotArmControlGroup)
        self.ArmSpeedDecButton.setObjectName(u"ArmSpeedDecButton")
        self.ArmSpeedDecButton.setGeometry(QRect(61, 320, 51, 31))
        self.AngleFourLabel = QLabel(self.RobotArmControlGroup)
        self.AngleFourLabel.setObjectName(u"AngleFourLabel")
        self.AngleFourLabel.setGeometry(QRect(18, 166, 41, 20))
        self.AngleFiveLabel = QLabel(self.RobotArmControlGroup)
        self.AngleFiveLabel.setObjectName(u"AngleFiveLabel")
        self.AngleFiveLabel.setGeometry(QRect(18, 206, 41, 20))
        self.AngleStepLabel = QLabel(self.RobotArmControlGroup)
        self.AngleStepLabel.setObjectName(u"AngleStepLabel")
        self.AngleStepLabel.setGeometry(QRect(18, 287, 41, 20))
        self.AngleThreeSubButton = QPushButton(self.RobotArmControlGroup)
        self.AngleThreeSubButton.setObjectName(u"AngleThreeSubButton")
        self.AngleThreeSubButton.setGeometry(QRect(61, 120, 51, 31))
        self.AngleFiveAddButton = QPushButton(self.RobotArmControlGroup)
        self.AngleFiveAddButton.setObjectName(u"AngleFiveAddButton")
        self.AngleFiveAddButton.setGeometry(QRect(181, 200, 51, 31))
        self.AngleTwoAddButton = QPushButton(self.RobotArmControlGroup)
        self.AngleTwoAddButton.setObjectName(u"AngleTwoAddButton")
        self.AngleTwoAddButton.setGeometry(QRect(181, 80, 51, 31))
        self.AngleTwoLabel = QLabel(self.RobotArmControlGroup)
        self.AngleTwoLabel.setObjectName(u"AngleTwoLabel")
        self.AngleTwoLabel.setGeometry(QRect(18, 85, 41, 20))
        self.AngleThreeAddButton = QPushButton(self.RobotArmControlGroup)
        self.AngleThreeAddButton.setObjectName(u"AngleThreeAddButton")
        self.AngleThreeAddButton.setGeometry(QRect(181, 120, 51, 31))
        self.AngleStepEdit = QLineEdit(self.RobotArmControlGroup)
        self.AngleStepEdit.setObjectName(u"AngleStepEdit")
        self.AngleStepEdit.setGeometry(QRect(121, 280, 51, 31))
        self.RobotArmAttituControlGroup = QGroupBox(Form)
        self.RobotArmAttituControlGroup.setObjectName(u"RobotArmAttituControlGroup")
        self.RobotArmAttituControlGroup.setGeometry(QRect(1240, 240, 221, 181))
        self.RzAxisAddButton = QPushButton(self.RobotArmAttituControlGroup)
        self.RzAxisAddButton.setObjectName(u"RzAxisAddButton")
        self.RzAxisAddButton.setGeometry(QRect(160, 130, 51, 31))
        self.RzAxisEdit = QLineEdit(self.RobotArmAttituControlGroup)
        self.RzAxisEdit.setObjectName(u"RzAxisEdit")
        self.RzAxisEdit.setGeometry(QRect(100, 130, 51, 31))
        self.RxAxisEdit = QLineEdit(self.RobotArmAttituControlGroup)
        self.RxAxisEdit.setObjectName(u"RxAxisEdit")
        self.RxAxisEdit.setGeometry(QRect(100, 50, 51, 31))
        self.RzLabel = QLabel(self.RobotArmAttituControlGroup)
        self.RzLabel.setObjectName(u"RzLabel")
        self.RzLabel.setGeometry(QRect(13, 140, 21, 20))
        self.RzAxisSubButton = QPushButton(self.RobotArmAttituControlGroup)
        self.RzAxisSubButton.setObjectName(u"RzAxisSubButton")
        self.RzAxisSubButton.setGeometry(QRect(40, 130, 51, 31))
        self.RyAxisAddButton = QPushButton(self.RobotArmAttituControlGroup)
        self.RyAxisAddButton.setObjectName(u"RyAxisAddButton")
        self.RyAxisAddButton.setGeometry(QRect(160, 90, 51, 31))
        self.RyLabel = QLabel(self.RobotArmAttituControlGroup)
        self.RyLabel.setObjectName(u"RyLabel")
        self.RyLabel.setGeometry(QRect(13, 100, 21, 20))
        self.RxLabel = QLabel(self.RobotArmAttituControlGroup)
        self.RxLabel.setObjectName(u"RxLabel")
        self.RxLabel.setGeometry(QRect(13, 60, 21, 20))
        self.RxAxisSubButton = QPushButton(self.RobotArmAttituControlGroup)
        self.RxAxisSubButton.setObjectName(u"RxAxisSubButton")
        self.RxAxisSubButton.setGeometry(QRect(40, 50, 51, 31))
        self.RxAxisAddButton = QPushButton(self.RobotArmAttituControlGroup)
        self.RxAxisAddButton.setObjectName(u"RxAxisAddButton")
        self.RxAxisAddButton.setGeometry(QRect(160, 50, 51, 31))
        self.RyAxisEdit = QLineEdit(self.RobotArmAttituControlGroup)
        self.RyAxisEdit.setObjectName(u"RyAxisEdit")
        self.RyAxisEdit.setGeometry(QRect(100, 90, 51, 31))
        self.RyAxisSubButton = QPushButton(self.RobotArmAttituControlGroup)
        self.RyAxisSubButton.setObjectName(u"RyAxisSubButton")
        self.RyAxisSubButton.setGeometry(QRect(40, 90, 51, 31))
        self.RobotArmResetButton = QPushButton(Form)
        self.RobotArmResetButton.setObjectName(u"RobotArmResetButton")
        self.RobotArmResetButton.setGeometry(QRect(1250, 460, 101, 81))
        self.RobotArmStopButton = QPushButton(Form)
        self.RobotArmStopButton.setObjectName(u"RobotArmStopButton")
        self.RobotArmStopButton.setGeometry(QRect(1360, 460, 101, 81))
        self.graphicsView = QGraphicsView(Form)
        self.graphicsView.setObjectName(u"graphicsView")
        self.graphicsView.setGeometry(QRect(990, 566, 341, 81))

        self.retranslateUi(Form)

        self.HomePage.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.CommandEditWindow.setPlaceholderText(QCoreApplication.translate("Form", u"\u8bf7\u8f93\u5165\u7b26\u5408 json \u683c\u5f0f\u7684\u63a7\u5236\u547d\u4ee4", None))
        self.CommandSendButton.setText(QCoreApplication.translate("Form", u"\u53d1\u9001", None))
        self.SendLabel.setText(QCoreApplication.translate("Form", u"\u547d\u4ee4\u53d1\u9001", None))
        self.ResponseLabel.setText(QCoreApplication.translate("Form", u"\u547d\u4ee4\u54cd\u5e94", None))
        self.CommandArmRunLogLabel.setText(QCoreApplication.translate("Form", u"\u673a\u68b0\u81c2\u8fd0\u884c\u65e5\u5fd7", None))
        self.CommandResWindow.setPlaceholderText(QCoreApplication.translate("Form", u"\u54cd\u5e94", None))
        self.CommandSendWindow.setPlaceholderText(QCoreApplication.translate("Form", u"\u53d1\u9001", None))
        self.HomePage.setTabText(self.HomePage.indexOf(self.CommandPage), QCoreApplication.translate("Form", u"\u547d\u4ee4\u63a7\u5236", None))
        ___qtablewidgetitem = self.ActionTableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Form", u"J1/X", None));
        ___qtablewidgetitem1 = self.ActionTableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Form", u"J2/Y", None));
        ___qtablewidgetitem2 = self.ActionTableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Form", u"J3/Z", None));
        ___qtablewidgetitem3 = self.ActionTableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Form", u"J4/RX", None));
        ___qtablewidgetitem4 = self.ActionTableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Form", u"J5/RY", None));
        ___qtablewidgetitem5 = self.ActionTableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("Form", u"J6/RZ", None));
        ___qtablewidgetitem6 = self.ActionTableWidget.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("Form", u"\u901f\u5ea6", None));
        ___qtablewidgetitem7 = self.ActionTableWidget.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("Form", u"\u5de5\u5177", None));
        ___qtablewidgetitem8 = self.ActionTableWidget.horizontalHeaderItem(8)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("Form", u"\u5f00\u5173", None));
        ___qtablewidgetitem9 = self.ActionTableWidget.horizontalHeaderItem(9)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("Form", u"\u5ef6\u65f6", None));
        ___qtablewidgetitem10 = self.ActionTableWidget.horizontalHeaderItem(10)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("Form", u"\u5907\u6ce8", None));
        self.TeachArmRunLogLabel.setText(QCoreApplication.translate("Form", u"\u673a\u68b0\u81c2\u8fd0\u884c\u65e5\u5fd7", None))
        self.ActionDeleteButton.setText(QCoreApplication.translate("Form", u"\u5220\u9664\u52a8\u4f5c", None))
        self.ActionPastButton.setText(QCoreApplication.translate("Form", u"\u7c98\u8d34\u52a8\u4f5c", None))
        self.ActionCopyButton.setText(QCoreApplication.translate("Form", u"\u590d\u5236\u52a8\u4f5c", None))
        self.ActionAddButton.setText(QCoreApplication.translate("Form", u"\u6dfb\u52a0\u52a8\u4f5c", None))
        self.ActionRunButton.setText(QCoreApplication.translate("Form", u"\u987a\u5e8f\u6267\u884c", None))
        self.ActionStepRunButton.setText(QCoreApplication.translate("Form", u"\u5355\u6b21\u6267\u884c", None))
        self.ActionUpdateButton.setText(QCoreApplication.translate("Form", u"\u66f4\u65b0\u52a8\u4f5c", None))
        self.ActionLoopRunButton.setText(QCoreApplication.translate("Form", u"\u5faa\u73af\u6267\u884c", None))
        self.ActionLoopTimes.setPlaceholderText(QCoreApplication.translate("Form", u"1~100", None))
        self.ActionImportButton.setText(QCoreApplication.translate("Form", u"\u5bfc\u5165\u52a8\u4f5c", None))
        self.ActionOutputButton.setText(QCoreApplication.translate("Form", u"\u5bfc\u51fa\u52a8\u4f5c", None))
        self.HomePage.setTabText(self.HomePage.indexOf(self.HelpTeachPage), QCoreApplication.translate("Form", u"\u793a\u6559\u63a7\u5236", None))
        self.IpPortInfoGroup.setTitle(QCoreApplication.translate("Form", u"\u673a\u68b0\u81c2\u8fde\u63a5\u914d\u7f6e", None))
        self.IpPortInfoSubmitButton.setText(QCoreApplication.translate("Form", u"\u786e\u5b9a", None))
        self.TargetPortLabel.setText(QCoreApplication.translate("Form", u"\u7aef\u53e3\u53f7", None))
        self.TargetPortEdit.setText("")
        self.IpPortInfoRestButton.setText(QCoreApplication.translate("Form", u"\u91cd\u7f6e", None))
        self.TargetIpLabel.setText(QCoreApplication.translate("Form", u"\u76ee\u6807 IP", None))
        self.WiFiInfoGroup.setTitle(QCoreApplication.translate("Form", u"\u673a\u68b0\u81c2 WIFI  AP \u6a21\u5f0f\u914d\u7f6e", None))
        self.WiFiInfoSubmit.setText(QCoreApplication.translate("Form", u"\u786e\u5b9a", None))
        self.WiFiPasswdLabel.setText(QCoreApplication.translate("Form", u"WIFI \u5bc6\u7801", None))
        self.WiFiPasswdEdit.setText("")
        self.WiFiInfoReset.setText(QCoreApplication.translate("Form", u"\u91cd\u7f6e", None))
        self.WiFiSsidLabel.setText(QCoreApplication.translate("Form", u"WIFI SSID", None))
        self.SbInfoGroup.setTitle(QCoreApplication.translate("Form", u"\u673a\u68b0\u81c2\u4e32\u53e3\u8fde\u63a5\u914d\u7f6e", None))
        self.SbInfoSubmitButton.setText(QCoreApplication.translate("Form", u"\u786e\u5b9a", None))
        self.BaudRatesLabel.setText(QCoreApplication.translate("Form", u"\u6ce2\u7279\u7387", None))
        self.SbInfoFreshButton.setText(QCoreApplication.translate("Form", u"\u5237\u65b0", None))
        self.SerialNumLabel.setText(QCoreApplication.translate("Form", u"\u4e32\u53e3\u53f7", None))
        self.BaudRatesComboBox.setItemText(0, QCoreApplication.translate("Form", u"115200", None))
        self.BaudRatesComboBox.setItemText(1, QCoreApplication.translate("Form", u"8000", None))

        self.RobotArmLinkButton.setText(QCoreApplication.translate("Form", u"\u8fde\u63a5\u673a\u68b0\u81c2", None))
        self.HomePage.setTabText(self.HomePage.indexOf(self.SettingPage), QCoreApplication.translate("Form", u"\u8fde\u63a5\u914d\u7f6e", None))
        self.groupBox.setTitle(QCoreApplication.translate("Form", u"\u672c\u673a\u4fe1\u606f", None))
        self.RobotArmInfoGroup.setTitle(QCoreApplication.translate("Form", u"\u673a\u68b0\u81c2\u4fe1\u606f", None))
        self.SoftInfoGroup.setTitle(QCoreApplication.translate("Form", u"\u8f6f\u4ef6\u4fe1\u606f", None))
        self.HomePage.setTabText(self.HomePage.indexOf(self.SystemInfoPage), QCoreApplication.translate("Form", u"\u7cfb\u7edf\u4fe1\u606f", None))
        self.RobotArmToolsGrop.setTitle(QCoreApplication.translate("Form", u"\u672b\u7aef\u5de5\u5177\u63a7\u5236", None))
        self.ArmClawCloseButton.setText(QCoreApplication.translate("Form", u"\u5173", None))
        self.ArmControlLabel.setText(QCoreApplication.translate("Form", u"\u63a7\u5236", None))
        self.ArmClawOpenButton.setText(QCoreApplication.translate("Form", u"\u5f00", None))
        self.ArmToolLabel.setText(QCoreApplication.translate("Form", u"\u5de5\u5177", None))
        self.ArmToolComboBox.setItemText(0, "")
        self.ArmToolComboBox.setItemText(1, QCoreApplication.translate("Form", u"\u5939\u722a", None))
        self.ArmToolComboBox.setItemText(2, QCoreApplication.translate("Form", u"\u5438\u76d8", None))

        self.RobotArmPositionControlGroup.setTitle(QCoreApplication.translate("Form", u"\u4f4d\u7f6e\u63a7\u5236", None))
        self.ZAxisAddButton.setText(QCoreApplication.translate("Form", u"+", None))
        self.XAxisEdit.setText(QCoreApplication.translate("Form", u"0", None))
        self.YAxisAddButton.setText(QCoreApplication.translate("Form", u"+", None))
        self.Zlable.setText(QCoreApplication.translate("Form", u"Z", None))
        self.YLable.setText(QCoreApplication.translate("Form", u"Y", None))
        self.XAxisSubButton.setText(QCoreApplication.translate("Form", u"-", None))
        self.YAxisEdit.setText(QCoreApplication.translate("Form", u"0", None))
        self.YAxisSubButton.setText(QCoreApplication.translate("Form", u"-", None))
        self.ZAxisEdit.setText(QCoreApplication.translate("Form", u"0", None))
        self.XLable.setText(QCoreApplication.translate("Form", u"X", None))
        self.ZAxisSubButton.setText(QCoreApplication.translate("Form", u"-", None))
        self.XAxisAddButton.setText(QCoreApplication.translate("Form", u"+", None))
        self.RobotArmControlGroup.setTitle(QCoreApplication.translate("Form", u"\u673a\u68b0\u81c2\u5173\u8282\u63a7\u5236", None))
        self.AngleOneSubButton.setText(QCoreApplication.translate("Form", u"-", None))
        self.AngleOneLabel.setText(QCoreApplication.translate("Form", u"\u5173\u82821", None))
        self.AngleFourAddButton.setText(QCoreApplication.translate("Form", u"+", None))
        self.AngleTwoSubButton.setText(QCoreApplication.translate("Form", u"-", None))
        self.AngleFourSubButton.setText(QCoreApplication.translate("Form", u"-", None))
        self.AngleSixSubButton.setText(QCoreApplication.translate("Form", u"-", None))
        self.AngleSixLabel.setText(QCoreApplication.translate("Form", u"\u5173\u82826", None))
        self.AngleSixAddButton.setText(QCoreApplication.translate("Form", u"+", None))
        self.ArmSpeedLabel.setText(QCoreApplication.translate("Form", u"\u901f\u5ea6", None))
        self.ArmSpeedEdit.setText(QCoreApplication.translate("Form", u"0", None))
        self.AngleOneAddButton.setText(QCoreApplication.translate("Form", u"+", None))
        self.AngleStepAddButton.setText(QCoreApplication.translate("Form", u"+", None))
        self.AngleFiveEdit.setText(QCoreApplication.translate("Form", u"0", None))
        self.AngleThreeLabel.setText(QCoreApplication.translate("Form", u"\u5173\u82823", None))
        self.AngleTwoEdit.setText(QCoreApplication.translate("Form", u"0", None))
        self.AngleSixEdit.setText(QCoreApplication.translate("Form", u"0", None))
        self.ArmSpeedUpButton.setText(QCoreApplication.translate("Form", u"+", None))
        self.AngleThreeEdit.setText(QCoreApplication.translate("Form", u"0", None))
        self.AngleFiveSubButton.setText(QCoreApplication.translate("Form", u"-", None))
        self.AngleFourEdit.setText(QCoreApplication.translate("Form", u"0", None))
        self.AngleOneEdit.setText(QCoreApplication.translate("Form", u"0", None))
        self.AngleStepSubButton.setText(QCoreApplication.translate("Form", u"-", None))
        self.ArmSpeedDecButton.setText(QCoreApplication.translate("Form", u"-", None))
        self.AngleFourLabel.setText(QCoreApplication.translate("Form", u"\u5173\u82824", None))
        self.AngleFiveLabel.setText(QCoreApplication.translate("Form", u"\u5173\u82825", None))
        self.AngleStepLabel.setText(QCoreApplication.translate("Form", u"\u6b65\u957f", None))
        self.AngleThreeSubButton.setText(QCoreApplication.translate("Form", u"-", None))
        self.AngleFiveAddButton.setText(QCoreApplication.translate("Form", u"+", None))
        self.AngleTwoAddButton.setText(QCoreApplication.translate("Form", u"+", None))
        self.AngleTwoLabel.setText(QCoreApplication.translate("Form", u"\u5173\u82822", None))
        self.AngleThreeAddButton.setText(QCoreApplication.translate("Form", u"+", None))
        self.AngleStepEdit.setText(QCoreApplication.translate("Form", u"0", None))
        self.RobotArmAttituControlGroup.setTitle(QCoreApplication.translate("Form", u"\u59ff\u6001\u63a7\u5236", None))
        self.RzAxisAddButton.setText(QCoreApplication.translate("Form", u"+", None))
        self.RzAxisEdit.setText(QCoreApplication.translate("Form", u"0", None))
        self.RxAxisEdit.setText(QCoreApplication.translate("Form", u"0", None))
        self.RzLabel.setText(QCoreApplication.translate("Form", u"RZ", None))
        self.RzAxisSubButton.setText(QCoreApplication.translate("Form", u"-", None))
        self.RyAxisAddButton.setText(QCoreApplication.translate("Form", u"+", None))
        self.RyLabel.setText(QCoreApplication.translate("Form", u"RY", None))
        self.RxLabel.setText(QCoreApplication.translate("Form", u"RX", None))
        self.RxAxisSubButton.setText(QCoreApplication.translate("Form", u"-", None))
        self.RxAxisAddButton.setText(QCoreApplication.translate("Form", u"+", None))
        self.RyAxisEdit.setText(QCoreApplication.translate("Form", u"0", None))
        self.RyAxisSubButton.setText(QCoreApplication.translate("Form", u"-", None))
        self.RobotArmResetButton.setText(QCoreApplication.translate("Form", u"\u590d\u4f4d", None))
        self.RobotArmStopButton.setText(QCoreApplication.translate("Form", u"\u6025\u505c", None))
    # retranslateUi

