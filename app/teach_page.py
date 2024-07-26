# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'teach_page.ui'
##
## Created by: Qt User Interface Compiler version 6.6.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QHeaderView,
    QSizePolicy, QSpacerItem, QStackedWidget, QTableWidget,
    QTableWidgetItem, QVBoxLayout, QWidget)

from qfluentwidgets import (BodyLabel, CardWidget, ComboBox, HorizontalSeparator,
    LineEdit, Pivot, ProgressBar, PushButton,
    SegmentedWidget, StrongBodyLabel, SwitchButton, ToolButton,
    TransparentToolButton, VerticalSeparator)

class teach_page_frame(object):
    def setupUi(self, Frame):
        if not Frame.objectName():
            Frame.setObjectName(u"Frame")
        Frame.resize(1318, 718)
        self.horizontalLayout_19 = QHBoxLayout(Frame)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.horizontalLayout_18 = QHBoxLayout()
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.ActionImportButton = PushButton(Frame)
        self.ActionImportButton.setObjectName(u"ActionImportButton")
        self.ActionImportButton.setMinimumSize(QSize(80, 0))

        self.horizontalLayout.addWidget(self.ActionImportButton)

        self.horizontalSpacer_31 = QSpacerItem(5, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_31)

        self.ActionOutputButton = PushButton(Frame)
        self.ActionOutputButton.setObjectName(u"ActionOutputButton")
        self.ActionOutputButton.setMinimumSize(QSize(0, 0))

        self.horizontalLayout.addWidget(self.ActionOutputButton)

        self.horizontalSpacer = QSpacerItem(300, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.ActionStepRunButton = PushButton(Frame)
        self.ActionStepRunButton.setObjectName(u"ActionStepRunButton")
        self.ActionStepRunButton.setMinimumSize(QSize(0, 0))

        self.horizontalLayout.addWidget(self.ActionStepRunButton)

        self.horizontalSpacer_3 = QSpacerItem(5, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_3)

        self.ActionRunButton = PushButton(Frame)
        self.ActionRunButton.setObjectName(u"ActionRunButton")
        self.ActionRunButton.setMinimumSize(QSize(0, 0))

        self.horizontalLayout.addWidget(self.ActionRunButton)

        self.horizontalSpacer_4 = QSpacerItem(5, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_4)

        self.ActionLoopRunButton = PushButton(Frame)
        self.ActionLoopRunButton.setObjectName(u"ActionLoopRunButton")
        self.ActionLoopRunButton.setMinimumSize(QSize(0, 0))

        self.horizontalLayout.addWidget(self.ActionLoopRunButton)

        self.ActionLoopTimes = LineEdit(Frame)
        self.ActionLoopTimes.setObjectName(u"ActionLoopTimes")
        self.ActionLoopTimes.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.ActionLoopTimes)


        self.verticalLayout_7.addLayout(self.horizontalLayout)

        self.HorizontalSeparator = HorizontalSeparator(Frame)
        self.HorizontalSeparator.setObjectName(u"HorizontalSeparator")

        self.verticalLayout_7.addWidget(self.HorizontalSeparator)

        self.ActionTableWidget = QTableWidget(Frame)
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

        self.verticalLayout_7.addWidget(self.ActionTableWidget)

        self.ProgressBar = ProgressBar(Frame)
        self.ProgressBar.setObjectName(u"ProgressBar")

        self.verticalLayout_7.addWidget(self.ProgressBar)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.ActionDeleteButton = PushButton(Frame)
        self.ActionDeleteButton.setObjectName(u"ActionDeleteButton")
        self.ActionDeleteButton.setMinimumSize(QSize(80, 0))

        self.horizontalLayout_2.addWidget(self.ActionDeleteButton)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_5)

        self.ActionAddButton = PushButton(Frame)
        self.ActionAddButton.setObjectName(u"ActionAddButton")

        self.horizontalLayout_2.addWidget(self.ActionAddButton)

        self.horizontalSpacer_6 = QSpacerItem(5, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_6)

        self.ActionUpdateRowButton = PushButton(Frame)
        self.ActionUpdateRowButton.setObjectName(u"ActionUpdateRowButton")

        self.horizontalLayout_2.addWidget(self.ActionUpdateRowButton)


        self.verticalLayout_7.addLayout(self.horizontalLayout_2)


        self.horizontalLayout_18.addLayout(self.verticalLayout_7)

        self.VerticalSeparator = VerticalSeparator(Frame)
        self.VerticalSeparator.setObjectName(u"VerticalSeparator")

        self.horizontalLayout_18.addWidget(self.VerticalSeparator)

        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.ActionModeIcon = TransparentToolButton(Frame)
        self.ActionModeIcon.setObjectName(u"ActionModeIcon")

        self.horizontalLayout_5.addWidget(self.ActionModeIcon)

        self.ActionModelLabel = BodyLabel(Frame)
        self.ActionModelLabel.setObjectName(u"ActionModelLabel")

        self.horizontalLayout_5.addWidget(self.ActionModelLabel)

        self.CommandModeComboBox = ComboBox(Frame)
        self.CommandModeComboBox.setObjectName(u"CommandModeComboBox")

        self.horizontalLayout_5.addWidget(self.CommandModeComboBox)

        self.horizontalSpacer_7 = QSpacerItem(10, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_7)


        self.verticalLayout_5.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.ActionRecordIcon = TransparentToolButton(Frame)
        self.ActionRecordIcon.setObjectName(u"ActionRecordIcon")

        self.horizontalLayout_8.addWidget(self.ActionRecordIcon)

        self.ActionRecordLabel = BodyLabel(Frame)
        self.ActionRecordLabel.setObjectName(u"ActionRecordLabel")

        self.horizontalLayout_8.addWidget(self.ActionRecordLabel)

        self.RecordActivateSwitchButton = SwitchButton(Frame)
        self.RecordActivateSwitchButton.setObjectName(u"RecordActivateSwitchButton")

        self.horizontalLayout_8.addWidget(self.RecordActivateSwitchButton)

        self.horizontalSpacer_24 = QSpacerItem(10, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_24)


        self.verticalLayout_5.addLayout(self.horizontalLayout_8)


        self.horizontalLayout_9.addLayout(self.verticalLayout_5)

        self.RobotArmStopButton = PushButton(Frame)
        self.RobotArmStopButton.setObjectName(u"RobotArmStopButton")
        self.RobotArmStopButton.setMinimumSize(QSize(150, 80))
        self.RobotArmStopButton.setMaximumSize(QSize(90, 90))

        self.horizontalLayout_9.addWidget(self.RobotArmStopButton)


        self.verticalLayout_9.addLayout(self.horizontalLayout_9)

        self.RobotArmControlSegmentedWidget = SegmentedWidget(Frame)
        self.RobotArmControlSegmentedWidget.setObjectName(u"RobotArmControlSegmentedWidget")
        self.RobotArmControlSegmentedWidget.setMinimumSize(QSize(188, 31))

        self.verticalLayout_9.addWidget(self.RobotArmControlSegmentedWidget)

        self.ArmActionControlStackWidget = QStackedWidget(Frame)
        self.ArmActionControlStackWidget.setObjectName(u"ArmActionControlStackWidget")
        self.ArmAngleControlPage = QWidget()
        self.ArmAngleControlPage.setObjectName(u"ArmAngleControlPage")
        self.verticalLayout_6 = QVBoxLayout(self.ArmAngleControlPage)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.ArmAngleControlCard = CardWidget(self.ArmAngleControlPage)
        self.ArmAngleControlCard.setObjectName(u"ArmAngleControlCard")
        self.horizontalLayout_22 = QHBoxLayout(self.ArmAngleControlCard)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.JointOneLaylout = QHBoxLayout()
        self.JointOneLaylout.setObjectName(u"JointOneLaylout")
        self.horizontalSpacer_40 = QSpacerItem(10, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.JointOneLaylout.addItem(self.horizontalSpacer_40)

        self.JointOneLabel = StrongBodyLabel(self.ArmAngleControlCard)
        self.JointOneLabel.setObjectName(u"JointOneLabel")

        self.JointOneLaylout.addWidget(self.JointOneLabel)

        self.horizontalSpacer_2 = QSpacerItem(22, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.JointOneLaylout.addItem(self.horizontalSpacer_2)

        self.JointOneSubButton = ToolButton(self.ArmAngleControlCard)
        self.JointOneSubButton.setObjectName(u"JointOneSubButton")

        self.JointOneLaylout.addWidget(self.JointOneSubButton)

        self.JointOneEdit = LineEdit(self.ArmAngleControlCard)
        self.JointOneEdit.setObjectName(u"JointOneEdit")
        self.JointOneEdit.setAlignment(Qt.AlignCenter)
        self.JointOneEdit.setReadOnly(True)

        self.JointOneLaylout.addWidget(self.JointOneEdit)

        self.JointOneAddButton = ToolButton(self.ArmAngleControlCard)
        self.JointOneAddButton.setObjectName(u"JointOneAddButton")

        self.JointOneLaylout.addWidget(self.JointOneAddButton)

        self.horizontalSpacer_49 = QSpacerItem(10, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.JointOneLaylout.addItem(self.horizontalSpacer_49)


        self.verticalLayout_2.addLayout(self.JointOneLaylout)

        self.JointTwolout = QHBoxLayout()
        self.JointTwolout.setObjectName(u"JointTwolout")
        self.horizontalSpacer_41 = QSpacerItem(10, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.JointTwolout.addItem(self.horizontalSpacer_41)

        self.JointTwoLabel = StrongBodyLabel(self.ArmAngleControlCard)
        self.JointTwoLabel.setObjectName(u"JointTwoLabel")

        self.JointTwolout.addWidget(self.JointTwoLabel)

        self.horizontalSpacer_9 = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.JointTwolout.addItem(self.horizontalSpacer_9)

        self.JointTwoSubButton = ToolButton(self.ArmAngleControlCard)
        self.JointTwoSubButton.setObjectName(u"JointTwoSubButton")

        self.JointTwolout.addWidget(self.JointTwoSubButton)

        self.JointTwoEdit = LineEdit(self.ArmAngleControlCard)
        self.JointTwoEdit.setObjectName(u"JointTwoEdit")
        self.JointTwoEdit.setAlignment(Qt.AlignCenter)
        self.JointTwoEdit.setReadOnly(True)

        self.JointTwolout.addWidget(self.JointTwoEdit)

        self.JointTwoAddButton = ToolButton(self.ArmAngleControlCard)
        self.JointTwoAddButton.setObjectName(u"JointTwoAddButton")

        self.JointTwolout.addWidget(self.JointTwoAddButton)

        self.horizontalSpacer_50 = QSpacerItem(10, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.JointTwolout.addItem(self.horizontalSpacer_50)


        self.verticalLayout_2.addLayout(self.JointTwolout)

        self.JointThreeLaylout = QHBoxLayout()
        self.JointThreeLaylout.setObjectName(u"JointThreeLaylout")
        self.horizontalSpacer_42 = QSpacerItem(10, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.JointThreeLaylout.addItem(self.horizontalSpacer_42)

        self.JointThreeLabel = StrongBodyLabel(self.ArmAngleControlCard)
        self.JointThreeLabel.setObjectName(u"JointThreeLabel")

        self.JointThreeLaylout.addWidget(self.JointThreeLabel)

        self.horizontalSpacer_10 = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.JointThreeLaylout.addItem(self.horizontalSpacer_10)

        self.JointThreeSubButton = ToolButton(self.ArmAngleControlCard)
        self.JointThreeSubButton.setObjectName(u"JointThreeSubButton")

        self.JointThreeLaylout.addWidget(self.JointThreeSubButton)

        self.JointThreeEdit = LineEdit(self.ArmAngleControlCard)
        self.JointThreeEdit.setObjectName(u"JointThreeEdit")
        self.JointThreeEdit.setAlignment(Qt.AlignCenter)
        self.JointThreeEdit.setReadOnly(True)

        self.JointThreeLaylout.addWidget(self.JointThreeEdit)

        self.JointThreeAddButton = ToolButton(self.ArmAngleControlCard)
        self.JointThreeAddButton.setObjectName(u"JointThreeAddButton")

        self.JointThreeLaylout.addWidget(self.JointThreeAddButton)

        self.horizontalSpacer_51 = QSpacerItem(10, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.JointThreeLaylout.addItem(self.horizontalSpacer_51)


        self.verticalLayout_2.addLayout(self.JointThreeLaylout)

        self.JointFourLaylout = QHBoxLayout()
        self.JointFourLaylout.setObjectName(u"JointFourLaylout")
        self.horizontalSpacer_43 = QSpacerItem(10, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.JointFourLaylout.addItem(self.horizontalSpacer_43)

        self.JointFourLabel = StrongBodyLabel(self.ArmAngleControlCard)
        self.JointFourLabel.setObjectName(u"JointFourLabel")

        self.JointFourLaylout.addWidget(self.JointFourLabel)

        self.horizontalSpacer_11 = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.JointFourLaylout.addItem(self.horizontalSpacer_11)

        self.JointFourSubButton = ToolButton(self.ArmAngleControlCard)
        self.JointFourSubButton.setObjectName(u"JointFourSubButton")

        self.JointFourLaylout.addWidget(self.JointFourSubButton)

        self.JointFourEdit = LineEdit(self.ArmAngleControlCard)
        self.JointFourEdit.setObjectName(u"JointFourEdit")
        self.JointFourEdit.setAlignment(Qt.AlignCenter)
        self.JointFourEdit.setReadOnly(True)

        self.JointFourLaylout.addWidget(self.JointFourEdit)

        self.JointFourAddButton = ToolButton(self.ArmAngleControlCard)
        self.JointFourAddButton.setObjectName(u"JointFourAddButton")

        self.JointFourLaylout.addWidget(self.JointFourAddButton)

        self.horizontalSpacer_52 = QSpacerItem(10, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.JointFourLaylout.addItem(self.horizontalSpacer_52)


        self.verticalLayout_2.addLayout(self.JointFourLaylout)

        self.JointFiveLaylout = QHBoxLayout()
        self.JointFiveLaylout.setObjectName(u"JointFiveLaylout")
        self.horizontalSpacer_44 = QSpacerItem(10, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.JointFiveLaylout.addItem(self.horizontalSpacer_44)

        self.JointFiveLabel = StrongBodyLabel(self.ArmAngleControlCard)
        self.JointFiveLabel.setObjectName(u"JointFiveLabel")

        self.JointFiveLaylout.addWidget(self.JointFiveLabel)

        self.horizontalSpacer_12 = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.JointFiveLaylout.addItem(self.horizontalSpacer_12)

        self.JointFiveSubButton = ToolButton(self.ArmAngleControlCard)
        self.JointFiveSubButton.setObjectName(u"JointFiveSubButton")

        self.JointFiveLaylout.addWidget(self.JointFiveSubButton)

        self.JointFiveEdit = LineEdit(self.ArmAngleControlCard)
        self.JointFiveEdit.setObjectName(u"JointFiveEdit")
        self.JointFiveEdit.setAlignment(Qt.AlignCenter)
        self.JointFiveEdit.setReadOnly(True)

        self.JointFiveLaylout.addWidget(self.JointFiveEdit)

        self.JointFiveAddButton = ToolButton(self.ArmAngleControlCard)
        self.JointFiveAddButton.setObjectName(u"JointFiveAddButton")

        self.JointFiveLaylout.addWidget(self.JointFiveAddButton)

        self.horizontalSpacer_53 = QSpacerItem(10, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.JointFiveLaylout.addItem(self.horizontalSpacer_53)


        self.verticalLayout_2.addLayout(self.JointFiveLaylout)

        self.JointSixLaylout = QHBoxLayout()
        self.JointSixLaylout.setObjectName(u"JointSixLaylout")
        self.horizontalSpacer_45 = QSpacerItem(10, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.JointSixLaylout.addItem(self.horizontalSpacer_45)

        self.JointSixLabel = StrongBodyLabel(self.ArmAngleControlCard)
        self.JointSixLabel.setObjectName(u"JointSixLabel")

        self.JointSixLaylout.addWidget(self.JointSixLabel)

        self.horizontalSpacer_13 = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.JointSixLaylout.addItem(self.horizontalSpacer_13)

        self.JointSixSubButton = ToolButton(self.ArmAngleControlCard)
        self.JointSixSubButton.setObjectName(u"JointSixSubButton")

        self.JointSixLaylout.addWidget(self.JointSixSubButton)

        self.JointSixEdit = LineEdit(self.ArmAngleControlCard)
        self.JointSixEdit.setObjectName(u"JointSixEdit")
        self.JointSixEdit.setAlignment(Qt.AlignCenter)
        self.JointSixEdit.setReadOnly(True)

        self.JointSixLaylout.addWidget(self.JointSixEdit)

        self.JointSixAddButton = ToolButton(self.ArmAngleControlCard)
        self.JointSixAddButton.setObjectName(u"JointSixAddButton")

        self.JointSixLaylout.addWidget(self.JointSixAddButton)

        self.horizontalSpacer_54 = QSpacerItem(10, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.JointSixLaylout.addItem(self.horizontalSpacer_54)


        self.verticalLayout_2.addLayout(self.JointSixLaylout)

        self.JointAngleStepLaylout = QHBoxLayout()
        self.JointAngleStepLaylout.setObjectName(u"JointAngleStepLaylout")
        self.horizontalSpacer_46 = QSpacerItem(14, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.JointAngleStepLaylout.addItem(self.horizontalSpacer_46)

        self.JointStepLabel = StrongBodyLabel(self.ArmAngleControlCard)
        self.JointStepLabel.setObjectName(u"JointStepLabel")

        self.JointAngleStepLaylout.addWidget(self.JointStepLabel)

        self.horizontalSpacer_14 = QSpacerItem(24, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.JointAngleStepLaylout.addItem(self.horizontalSpacer_14)

        self.JointStepSubButton = ToolButton(self.ArmAngleControlCard)
        self.JointStepSubButton.setObjectName(u"JointStepSubButton")

        self.JointAngleStepLaylout.addWidget(self.JointStepSubButton)

        self.JointStepEdit = LineEdit(self.ArmAngleControlCard)
        self.JointStepEdit.setObjectName(u"JointStepEdit")
        self.JointStepEdit.setAlignment(Qt.AlignCenter)

        self.JointAngleStepLaylout.addWidget(self.JointStepEdit)

        self.JointStepAddButton = ToolButton(self.ArmAngleControlCard)
        self.JointStepAddButton.setObjectName(u"JointStepAddButton")

        self.JointAngleStepLaylout.addWidget(self.JointStepAddButton)

        self.horizontalSpacer_55 = QSpacerItem(10, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.JointAngleStepLaylout.addItem(self.horizontalSpacer_55)


        self.verticalLayout_2.addLayout(self.JointAngleStepLaylout)

        self.JointSpeedLaylout = QHBoxLayout()
        self.JointSpeedLaylout.setObjectName(u"JointSpeedLaylout")
        self.horizontalSpacer_47 = QSpacerItem(14, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.JointSpeedLaylout.addItem(self.horizontalSpacer_47)

        self.JointSpeedLabel = StrongBodyLabel(self.ArmAngleControlCard)
        self.JointSpeedLabel.setObjectName(u"JointSpeedLabel")

        self.JointSpeedLaylout.addWidget(self.JointSpeedLabel)

        self.horizontalSpacer_15 = QSpacerItem(24, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.JointSpeedLaylout.addItem(self.horizontalSpacer_15)

        self.JointSpeedDecButton = ToolButton(self.ArmAngleControlCard)
        self.JointSpeedDecButton.setObjectName(u"JointSpeedDecButton")

        self.JointSpeedLaylout.addWidget(self.JointSpeedDecButton)

        self.JointSpeedEdit = LineEdit(self.ArmAngleControlCard)
        self.JointSpeedEdit.setObjectName(u"JointSpeedEdit")
        self.JointSpeedEdit.setAlignment(Qt.AlignCenter)

        self.JointSpeedLaylout.addWidget(self.JointSpeedEdit)

        self.JointSpeedUpButton = ToolButton(self.ArmAngleControlCard)
        self.JointSpeedUpButton.setObjectName(u"JointSpeedUpButton")

        self.JointSpeedLaylout.addWidget(self.JointSpeedUpButton)

        self.horizontalSpacer_56 = QSpacerItem(10, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.JointSpeedLaylout.addItem(self.horizontalSpacer_56)


        self.verticalLayout_2.addLayout(self.JointSpeedLaylout)

        self.JointDelayTimeLaylout = QHBoxLayout()
        self.JointDelayTimeLaylout.setObjectName(u"JointDelayTimeLaylout")
        self.horizontalSpacer_48 = QSpacerItem(14, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.JointDelayTimeLaylout.addItem(self.horizontalSpacer_48)

        self.JointDelayTimeLabel = StrongBodyLabel(self.ArmAngleControlCard)
        self.JointDelayTimeLabel.setObjectName(u"JointDelayTimeLabel")

        self.JointDelayTimeLaylout.addWidget(self.JointDelayTimeLabel)

        self.horizontalSpacer_18 = QSpacerItem(24, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.JointDelayTimeLaylout.addItem(self.horizontalSpacer_18)

        self.JointDelayTimeSubButton = ToolButton(self.ArmAngleControlCard)
        self.JointDelayTimeSubButton.setObjectName(u"JointDelayTimeSubButton")

        self.JointDelayTimeLaylout.addWidget(self.JointDelayTimeSubButton)

        self.JointDelayTimeEdit = LineEdit(self.ArmAngleControlCard)
        self.JointDelayTimeEdit.setObjectName(u"JointDelayTimeEdit")
        self.JointDelayTimeEdit.setAlignment(Qt.AlignCenter)

        self.JointDelayTimeLaylout.addWidget(self.JointDelayTimeEdit)

        self.JointDelayTimeAddButton = ToolButton(self.ArmAngleControlCard)
        self.JointDelayTimeAddButton.setObjectName(u"JointDelayTimeAddButton")

        self.JointDelayTimeLaylout.addWidget(self.JointDelayTimeAddButton)

        self.horizontalSpacer_57 = QSpacerItem(10, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.JointDelayTimeLaylout.addItem(self.horizontalSpacer_57)


        self.verticalLayout_2.addLayout(self.JointDelayTimeLaylout)


        self.horizontalLayout_22.addLayout(self.verticalLayout_2)


        self.verticalLayout_6.addWidget(self.ArmAngleControlCard)

        self.ArmActionControlStackWidget.addWidget(self.ArmAngleControlPage)
        self.ArmEndToolsCoordinateControlPage = QWidget()
        self.ArmEndToolsCoordinateControlPage.setObjectName(u"ArmEndToolsCoordinateControlPage")
        self.horizontalLayout_6 = QHBoxLayout(self.ArmEndToolsCoordinateControlPage)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.ArmEndToolsCoordinateControlCard = CardWidget(self.ArmEndToolsCoordinateControlPage)
        self.ArmEndToolsCoordinateControlCard.setObjectName(u"ArmEndToolsCoordinateControlCard")
        self.horizontalLayout_7 = QHBoxLayout(self.ArmEndToolsCoordinateControlCard)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalSpacer_32 = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_32)

        self.XLable = StrongBodyLabel(self.ArmEndToolsCoordinateControlCard)
        self.XLable.setObjectName(u"XLable")

        self.horizontalLayout_10.addWidget(self.XLable)

        self.horizontalSpacer_19 = QSpacerItem(22, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_19)

        self.XAxisSubButton = ToolButton(self.ArmEndToolsCoordinateControlCard)
        self.XAxisSubButton.setObjectName(u"XAxisSubButton")

        self.horizontalLayout_10.addWidget(self.XAxisSubButton)

        self.XAxisEdit = LineEdit(self.ArmEndToolsCoordinateControlCard)
        self.XAxisEdit.setObjectName(u"XAxisEdit")
        self.XAxisEdit.setAlignment(Qt.AlignCenter)
        self.XAxisEdit.setReadOnly(True)

        self.horizontalLayout_10.addWidget(self.XAxisEdit)

        self.XAxisAddButton = ToolButton(self.ArmEndToolsCoordinateControlCard)
        self.XAxisAddButton.setObjectName(u"XAxisAddButton")

        self.horizontalLayout_10.addWidget(self.XAxisAddButton)

        self.horizontalSpacer_36 = QSpacerItem(10, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_36)


        self.verticalLayout_3.addLayout(self.horizontalLayout_10)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalSpacer_33 = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_11.addItem(self.horizontalSpacer_33)

        self.YLable = StrongBodyLabel(self.ArmEndToolsCoordinateControlCard)
        self.YLable.setObjectName(u"YLable")

        self.horizontalLayout_11.addWidget(self.YLable)

        self.horizontalSpacer_20 = QSpacerItem(23, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_11.addItem(self.horizontalSpacer_20)

        self.YAxisSubButton = ToolButton(self.ArmEndToolsCoordinateControlCard)
        self.YAxisSubButton.setObjectName(u"YAxisSubButton")

        self.horizontalLayout_11.addWidget(self.YAxisSubButton)

        self.YAxisEdit = LineEdit(self.ArmEndToolsCoordinateControlCard)
        self.YAxisEdit.setObjectName(u"YAxisEdit")
        self.YAxisEdit.setAlignment(Qt.AlignCenter)
        self.YAxisEdit.setReadOnly(True)

        self.horizontalLayout_11.addWidget(self.YAxisEdit)

        self.YAxisAddButton = ToolButton(self.ArmEndToolsCoordinateControlCard)
        self.YAxisAddButton.setObjectName(u"YAxisAddButton")

        self.horizontalLayout_11.addWidget(self.YAxisAddButton)

        self.horizontalSpacer_37 = QSpacerItem(10, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_11.addItem(self.horizontalSpacer_37)


        self.verticalLayout_3.addLayout(self.horizontalLayout_11)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalSpacer_34 = QSpacerItem(21, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_34)

        self.Zlable = StrongBodyLabel(self.ArmEndToolsCoordinateControlCard)
        self.Zlable.setObjectName(u"Zlable")

        self.horizontalLayout_13.addWidget(self.Zlable)

        self.horizontalSpacer_21 = QSpacerItem(22, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_21)

        self.ZAxisSubButton = ToolButton(self.ArmEndToolsCoordinateControlCard)
        self.ZAxisSubButton.setObjectName(u"ZAxisSubButton")

        self.horizontalLayout_13.addWidget(self.ZAxisSubButton)

        self.ZAxisEdit = LineEdit(self.ArmEndToolsCoordinateControlCard)
        self.ZAxisEdit.setObjectName(u"ZAxisEdit")
        self.ZAxisEdit.setAlignment(Qt.AlignCenter)
        self.ZAxisEdit.setReadOnly(True)

        self.horizontalLayout_13.addWidget(self.ZAxisEdit)

        self.ZAxisAddButton = ToolButton(self.ArmEndToolsCoordinateControlCard)
        self.ZAxisAddButton.setObjectName(u"ZAxisAddButton")

        self.horizontalLayout_13.addWidget(self.ZAxisAddButton)

        self.horizontalSpacer_38 = QSpacerItem(10, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_38)


        self.verticalLayout_3.addLayout(self.horizontalLayout_13)

        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalSpacer_35 = QSpacerItem(10, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_14.addItem(self.horizontalSpacer_35)

        self.CoordinateStepLable = StrongBodyLabel(self.ArmEndToolsCoordinateControlCard)
        self.CoordinateStepLable.setObjectName(u"CoordinateStepLable")

        self.horizontalLayout_14.addWidget(self.CoordinateStepLable)

        self.horizontalSpacer_22 = QSpacerItem(10, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_14.addItem(self.horizontalSpacer_22)

        self.CoordinateStepSubButton = ToolButton(self.ArmEndToolsCoordinateControlCard)
        self.CoordinateStepSubButton.setObjectName(u"CoordinateStepSubButton")

        self.horizontalLayout_14.addWidget(self.CoordinateStepSubButton)

        self.CoordinateStepEdit = LineEdit(self.ArmEndToolsCoordinateControlCard)
        self.CoordinateStepEdit.setObjectName(u"CoordinateStepEdit")
        self.CoordinateStepEdit.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_14.addWidget(self.CoordinateStepEdit)

        self.CoordinateAddButton = ToolButton(self.ArmEndToolsCoordinateControlCard)
        self.CoordinateAddButton.setObjectName(u"CoordinateAddButton")

        self.horizontalLayout_14.addWidget(self.CoordinateAddButton)

        self.horizontalSpacer_39 = QSpacerItem(10, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_14.addItem(self.horizontalSpacer_39)


        self.verticalLayout_3.addLayout(self.horizontalLayout_14)

        self.HorizontalSeparator_2 = HorizontalSeparator(self.ArmEndToolsCoordinateControlCard)
        self.HorizontalSeparator_2.setObjectName(u"HorizontalSeparator_2")

        self.verticalLayout_3.addWidget(self.HorizontalSeparator_2)

        self.horizontalLayout_24 = QHBoxLayout()
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.horizontalSpacer_23 = QSpacerItem(18, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_24.addItem(self.horizontalSpacer_23)

        self.RxLabel = StrongBodyLabel(self.ArmEndToolsCoordinateControlCard)
        self.RxLabel.setObjectName(u"RxLabel")

        self.horizontalLayout_24.addWidget(self.RxLabel)

        self.horizontalSpacer_79 = QSpacerItem(17, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_24.addItem(self.horizontalSpacer_79)

        self.RxAxisSubButton = ToolButton(self.ArmEndToolsCoordinateControlCard)
        self.RxAxisSubButton.setObjectName(u"RxAxisSubButton")

        self.horizontalLayout_24.addWidget(self.RxAxisSubButton)

        self.RxAxisEdit = LineEdit(self.ArmEndToolsCoordinateControlCard)
        self.RxAxisEdit.setObjectName(u"RxAxisEdit")
        self.RxAxisEdit.setAlignment(Qt.AlignCenter)
        self.RxAxisEdit.setReadOnly(True)

        self.horizontalLayout_24.addWidget(self.RxAxisEdit)

        self.RxAxisAddButton = ToolButton(self.ArmEndToolsCoordinateControlCard)
        self.RxAxisAddButton.setObjectName(u"RxAxisAddButton")

        self.horizontalLayout_24.addWidget(self.RxAxisAddButton)

        self.horizontalSpacer_80 = QSpacerItem(10, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_24.addItem(self.horizontalSpacer_80)


        self.verticalLayout_3.addLayout(self.horizontalLayout_24)

        self.horizontalLayout_25 = QHBoxLayout()
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.horizontalSpacer_81 = QSpacerItem(18, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_25.addItem(self.horizontalSpacer_81)

        self.RyLabel = StrongBodyLabel(self.ArmEndToolsCoordinateControlCard)
        self.RyLabel.setObjectName(u"RyLabel")

        self.horizontalLayout_25.addWidget(self.RyLabel)

        self.horizontalSpacer_82 = QSpacerItem(17, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_25.addItem(self.horizontalSpacer_82)

        self.RyAxisSubButton = ToolButton(self.ArmEndToolsCoordinateControlCard)
        self.RyAxisSubButton.setObjectName(u"RyAxisSubButton")

        self.horizontalLayout_25.addWidget(self.RyAxisSubButton)

        self.RyAxisEdit = LineEdit(self.ArmEndToolsCoordinateControlCard)
        self.RyAxisEdit.setObjectName(u"RyAxisEdit")
        self.RyAxisEdit.setAlignment(Qt.AlignCenter)
        self.RyAxisEdit.setReadOnly(True)

        self.horizontalLayout_25.addWidget(self.RyAxisEdit)

        self.RyAxisAddButton = ToolButton(self.ArmEndToolsCoordinateControlCard)
        self.RyAxisAddButton.setObjectName(u"RyAxisAddButton")

        self.horizontalLayout_25.addWidget(self.RyAxisAddButton)

        self.horizontalSpacer_83 = QSpacerItem(10, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_25.addItem(self.horizontalSpacer_83)


        self.verticalLayout_3.addLayout(self.horizontalLayout_25)

        self.horizontalLayout_26 = QHBoxLayout()
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.horizontalSpacer_84 = QSpacerItem(18, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_26.addItem(self.horizontalSpacer_84)

        self.RzLabel = StrongBodyLabel(self.ArmEndToolsCoordinateControlCard)
        self.RzLabel.setObjectName(u"RzLabel")

        self.horizontalLayout_26.addWidget(self.RzLabel)

        self.horizontalSpacer_85 = QSpacerItem(17, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_26.addItem(self.horizontalSpacer_85)

        self.RzAxisSubButton = ToolButton(self.ArmEndToolsCoordinateControlCard)
        self.RzAxisSubButton.setObjectName(u"RzAxisSubButton")

        self.horizontalLayout_26.addWidget(self.RzAxisSubButton)

        self.RzAxisEdit = LineEdit(self.ArmEndToolsCoordinateControlCard)
        self.RzAxisEdit.setObjectName(u"RzAxisEdit")
        self.RzAxisEdit.setAlignment(Qt.AlignCenter)
        self.RzAxisEdit.setReadOnly(True)

        self.horizontalLayout_26.addWidget(self.RzAxisEdit)

        self.RzAxisAddButton = ToolButton(self.ArmEndToolsCoordinateControlCard)
        self.RzAxisAddButton.setObjectName(u"RzAxisAddButton")

        self.horizontalLayout_26.addWidget(self.RzAxisAddButton)

        self.horizontalSpacer_86 = QSpacerItem(10, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_26.addItem(self.horizontalSpacer_86)


        self.verticalLayout_3.addLayout(self.horizontalLayout_26)

        self.horizontalLayout_27 = QHBoxLayout()
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.horizontalSpacer_87 = QSpacerItem(10, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_27.addItem(self.horizontalSpacer_87)

        self.ApStepLabel = StrongBodyLabel(self.ArmEndToolsCoordinateControlCard)
        self.ApStepLabel.setObjectName(u"ApStepLabel")

        self.horizontalLayout_27.addWidget(self.ApStepLabel)

        self.horizontalSpacer_88 = QSpacerItem(10, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_27.addItem(self.horizontalSpacer_88)

        self.ApStepSubButton = ToolButton(self.ArmEndToolsCoordinateControlCard)
        self.ApStepSubButton.setObjectName(u"ApStepSubButton")

        self.horizontalLayout_27.addWidget(self.ApStepSubButton)

        self.ApStepEdit = LineEdit(self.ArmEndToolsCoordinateControlCard)
        self.ApStepEdit.setObjectName(u"ApStepEdit")
        self.ApStepEdit.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_27.addWidget(self.ApStepEdit)

        self.ApStepAddButton = ToolButton(self.ArmEndToolsCoordinateControlCard)
        self.ApStepAddButton.setObjectName(u"ApStepAddButton")

        self.horizontalLayout_27.addWidget(self.ApStepAddButton)

        self.horizontalSpacer_89 = QSpacerItem(10, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_27.addItem(self.horizontalSpacer_89)


        self.verticalLayout_3.addLayout(self.horizontalLayout_27)


        self.horizontalLayout_7.addLayout(self.verticalLayout_3)


        self.horizontalLayout_6.addWidget(self.ArmEndToolsCoordinateControlCard)

        self.ArmActionControlStackWidget.addWidget(self.ArmEndToolsCoordinateControlPage)
        self.ArmEndToolsPositionControlPage = QWidget()
        self.ArmEndToolsPositionControlPage.setObjectName(u"ArmEndToolsPositionControlPage")
        self.verticalLayout = QVBoxLayout(self.ArmEndToolsPositionControlPage)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.ArmActionControlStackWidget.addWidget(self.ArmEndToolsPositionControlPage)

        self.verticalLayout_9.addWidget(self.ArmActionControlStackWidget)

        self.horizontalLayout_17 = QHBoxLayout()
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.SwitchButtonOneIcon = TransparentToolButton(Frame)
        self.SwitchButtonOneIcon.setObjectName(u"SwitchButtonOneIcon")

        self.horizontalLayout_4.addWidget(self.SwitchButtonOneIcon)

        self.SwitchButtonOneLable = BodyLabel(Frame)
        self.SwitchButtonOneLable.setObjectName(u"SwitchButtonOneLable")
        font = QFont()
        font.setFamilies([u"Arial"])
        font.setPointSize(11)
        font.setBold(False)
        self.SwitchButtonOneLable.setFont(font)

        self.horizontalLayout_4.addWidget(self.SwitchButtonOneLable)

        self.SwitchButtonOne = SwitchButton(Frame)
        self.SwitchButtonOne.setObjectName(u"SwitchButtonOne")

        self.horizontalLayout_4.addWidget(self.SwitchButtonOne)


        self.verticalLayout_4.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.SwitchButtonTwoIcon = TransparentToolButton(Frame)
        self.SwitchButtonTwoIcon.setObjectName(u"SwitchButtonTwoIcon")

        self.horizontalLayout_15.addWidget(self.SwitchButtonTwoIcon)

        self.SwitchButtonTwoLable = BodyLabel(Frame)
        self.SwitchButtonTwoLable.setObjectName(u"SwitchButtonTwoLable")

        self.horizontalLayout_15.addWidget(self.SwitchButtonTwoLable)

        self.SwitchButtonTwo = SwitchButton(Frame)
        self.SwitchButtonTwo.setObjectName(u"SwitchButtonTwo")

        self.horizontalLayout_15.addWidget(self.SwitchButtonTwo)


        self.verticalLayout_4.addLayout(self.horizontalLayout_15)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.SwitchButtonThreeIcon = TransparentToolButton(Frame)
        self.SwitchButtonThreeIcon.setObjectName(u"SwitchButtonThreeIcon")

        self.horizontalLayout_12.addWidget(self.SwitchButtonThreeIcon)

        self.SwitchButtonThreeLable = BodyLabel(Frame)
        self.SwitchButtonThreeLable.setObjectName(u"SwitchButtonThreeLable")

        self.horizontalLayout_12.addWidget(self.SwitchButtonThreeLable)

        self.SwitchButtonThree = SwitchButton(Frame)
        self.SwitchButtonThree.setObjectName(u"SwitchButtonThree")

        self.horizontalLayout_12.addWidget(self.SwitchButtonThree)


        self.verticalLayout_4.addLayout(self.horizontalLayout_12)

        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.SwitchButtonFourIcon = TransparentToolButton(Frame)
        self.SwitchButtonFourIcon.setObjectName(u"SwitchButtonFourIcon")

        self.horizontalLayout_16.addWidget(self.SwitchButtonFourIcon)

        self.SwitchButtonFourLable = BodyLabel(Frame)
        self.SwitchButtonFourLable.setObjectName(u"SwitchButtonFourLable")

        self.horizontalLayout_16.addWidget(self.SwitchButtonFourLable)

        self.SwitchButtonFour = SwitchButton(Frame)
        self.SwitchButtonFour.setObjectName(u"SwitchButtonFour")

        self.horizontalLayout_16.addWidget(self.SwitchButtonFour)


        self.verticalLayout_4.addLayout(self.horizontalLayout_16)


        self.horizontalLayout_17.addLayout(self.verticalLayout_4)

        self.VerticalSeparator_2 = VerticalSeparator(Frame)
        self.VerticalSeparator_2.setObjectName(u"VerticalSeparator_2")

        self.horizontalLayout_17.addWidget(self.VerticalSeparator_2)

        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.horizontalLayout_tools = QHBoxLayout()
        self.horizontalLayout_tools.setSpacing(6)
        self.horizontalLayout_tools.setObjectName(u"horizontalLayout_tools")
        self.ToolIcon = TransparentToolButton(Frame)
        self.ToolIcon.setObjectName(u"ToolIcon")

        self.horizontalLayout_tools.addWidget(self.ToolIcon)

        self.ArmToolLabel = BodyLabel(Frame)
        self.ArmToolLabel.setObjectName(u"ArmToolLabel")

        self.horizontalLayout_tools.addWidget(self.ArmToolLabel)

        self.ArmToolComboBox = ComboBox(Frame)
        self.ArmToolComboBox.setObjectName(u"ArmToolComboBox")

        self.horizontalLayout_tools.addWidget(self.ArmToolComboBox)

        self.horizontalLayout_tools.setStretch(2, 8)

        self.verticalLayout_8.addLayout(self.horizontalLayout_tools)

        self.horizontalLayout_tool_control = QHBoxLayout()
        self.horizontalLayout_tool_control.setObjectName(u"horizontalLayout_tool_control")
        self.ToolsControlIcon = TransparentToolButton(Frame)
        self.ToolsControlIcon.setObjectName(u"ToolsControlIcon")

        self.horizontalLayout_tool_control.addWidget(self.ToolsControlIcon)

        self.BodyLabel = BodyLabel(Frame)
        self.BodyLabel.setObjectName(u"BodyLabel")

        self.horizontalLayout_tool_control.addWidget(self.BodyLabel)

        self.ArmToolSwitchButton = SwitchButton(Frame)
        self.ArmToolSwitchButton.setObjectName(u"ArmToolSwitchButton")

        self.horizontalLayout_tool_control.addWidget(self.ArmToolSwitchButton)


        self.verticalLayout_8.addLayout(self.horizontalLayout_tool_control)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.RobotArmZeroButton = PushButton(Frame)
        self.RobotArmZeroButton.setObjectName(u"RobotArmZeroButton")
        self.RobotArmZeroButton.setMinimumSize(QSize(80, 80))

        self.horizontalLayout_3.addWidget(self.RobotArmZeroButton)

        self.RobotArmResetButton = PushButton(Frame)
        self.RobotArmResetButton.setObjectName(u"RobotArmResetButton")
        self.RobotArmResetButton.setMinimumSize(QSize(80, 80))

        self.horizontalLayout_3.addWidget(self.RobotArmResetButton)


        self.verticalLayout_8.addLayout(self.horizontalLayout_3)


        self.horizontalLayout_17.addLayout(self.verticalLayout_8)


        self.verticalLayout_9.addLayout(self.horizontalLayout_17)


        self.horizontalLayout_18.addLayout(self.verticalLayout_9)


        self.horizontalLayout_19.addLayout(self.horizontalLayout_18)


        self.retranslateUi(Frame)

        self.ArmActionControlStackWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Frame)
    # setupUi

    def retranslateUi(self, Frame):
        Frame.setWindowTitle(QCoreApplication.translate("Frame", u"Frame", None))
        Frame.setProperty("lightCustomQss", "")
        self.ActionImportButton.setText(QCoreApplication.translate("Frame", u"\u5bfc\u5165\u52a8\u4f5c", None))
        self.ActionImportButton.setProperty("lightCustomQss", QCoreApplication.translate("Frame", u"PushButton {\n"
"    background: rgb(33, 150, 243);\n"
"    color:white;\n"
"}\n"
"\n"
"PushButton:hover {\n"
"    background: rgb(33, 150, 243);\n"
"    color:white;\n"
"}", None))
        self.ActionOutputButton.setText(QCoreApplication.translate("Frame", u"\u5bfc\u51fa\u52a8\u4f5c", None))
        self.ActionOutputButton.setProperty("lightCustomQss", QCoreApplication.translate("Frame", u"PushButton {\n"
"    background: rgb(33, 150, 243);\n"
"    color:white;\n"
"}\n"
"\n"
"PushButton:hover {\n"
"    background: rgb(33, 150, 243);\n"
"    color:white;\n"
"}", None))
        self.ActionStepRunButton.setText(QCoreApplication.translate("Frame", u"\u5355\u6b65\u6267\u884c", None))
        self.ActionStepRunButton.setProperty("lightCustomQss", QCoreApplication.translate("Frame", u"PushButton {\n"
"    background: rgb(33, 150, 243);\n"
"    color:white;\n"
"}\n"
"\n"
"PushButton:hover {\n"
"    background: rgb(33, 150, 243);\n"
"    color:white;\n"
"}", None))
        self.ActionRunButton.setText(QCoreApplication.translate("Frame", u"\u987a\u5e8f\u6267\u884c", None))
        self.ActionRunButton.setProperty("lightCustomQss", QCoreApplication.translate("Frame", u"PushButton {\n"
"    background: rgb(33, 150, 243);\n"
"    color:white;\n"
"}\n"
"\n"
"PushButton:hover {\n"
"    background: rgb(33, 150, 243);\n"
"    color:white;\n"
"}", None))
        self.ActionLoopRunButton.setText(QCoreApplication.translate("Frame", u"\u5faa\u73af\u6267\u884c", None))
        self.ActionLoopRunButton.setProperty("lightCustomQss", QCoreApplication.translate("Frame", u"PushButton {\n"
"    background: rgb(33, 150, 243);\n"
"    color:white;\n"
"}\n"
"\n"
"PushButton:hover {\n"
"    background: rgb(33, 150, 243);\n"
"    color:white;\n"
"}", None))
        self.ActionLoopTimes.setText("")
        self.ActionLoopTimes.setPlaceholderText(QCoreApplication.translate("Frame", u"1~100", None))
        ___qtablewidgetitem = self.ActionTableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Frame", u"J1", None));
        ___qtablewidgetitem1 = self.ActionTableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Frame", u"J2", None));
        ___qtablewidgetitem2 = self.ActionTableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Frame", u"J3", None));
        ___qtablewidgetitem3 = self.ActionTableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Frame", u"J4", None));
        ___qtablewidgetitem4 = self.ActionTableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Frame", u"J5", None));
        ___qtablewidgetitem5 = self.ActionTableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("Frame", u"J6", None));
        ___qtablewidgetitem6 = self.ActionTableWidget.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("Frame", u"\u901f\u5ea6", None));
        ___qtablewidgetitem7 = self.ActionTableWidget.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("Frame", u"\u5de5\u5177", None));
        ___qtablewidgetitem8 = self.ActionTableWidget.horizontalHeaderItem(8)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("Frame", u"\u5f00\u5173", None));
        ___qtablewidgetitem9 = self.ActionTableWidget.horizontalHeaderItem(9)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("Frame", u"\u5ef6\u65f6", None));
        ___qtablewidgetitem10 = self.ActionTableWidget.horizontalHeaderItem(10)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("Frame", u"\u5907\u6ce8", None));
        self.ActionDeleteButton.setText(QCoreApplication.translate("Frame", u"\u5220\u9664\u52a8\u4f5c", None))
        self.ActionDeleteButton.setProperty("lightCustomQss", QCoreApplication.translate("Frame", u"PushButton {\n"
"    background: rgb(225, 41, 41);\n"
"    color: white;\n"
"}\n"
"PushButton:hover {\n"
"    background: rgb(225, 41, 41);\n"
"    color: white;\n"
"}", None))
        self.ActionAddButton.setText(QCoreApplication.translate("Frame", u"\u6dfb\u52a0\u52a8\u4f5c", None))
        self.ActionAddButton.setProperty("lightCustomQss", QCoreApplication.translate("Frame", u"PushButton {\n"
"    background: rgb(33, 150, 243);\n"
"    color:white;\n"
"}\n"
"\n"
"PushButton:hover {\n"
"    background: rgb(33, 150, 243);\n"
"    color:white;\n"
"}", None))
        self.ActionUpdateRowButton.setText(QCoreApplication.translate("Frame", u"\u66f4\u65b0\u52a8\u4f5c", None))
        self.ActionUpdateRowButton.setProperty("lightCustomQss", QCoreApplication.translate("Frame", u"PushButton {\n"
"    background: rgb(33, 150, 243);\n"
"    color:white;\n"
"}\n"
"\n"
"PushButton:hover {\n"
"    background: rgb(33, 150, 243);\n"
"    color:white;\n"
"}", None))
        self.ActionModelLabel.setText(QCoreApplication.translate("Frame", u"\u6307\u4ee4\u6267\u884c\u6a21\u5f0f", None))
        self.ActionRecordLabel.setText(QCoreApplication.translate("Frame", u"\u5173\u8282\u52a8\u4f5c\u5f55\u5236", None))
        self.RecordActivateSwitchButton.setOnText(QCoreApplication.translate("Frame", u"\u5f00\u542f", None))
        self.RecordActivateSwitchButton.setOffText(QCoreApplication.translate("Frame", u"\u5173\u95ed", None))
        self.RobotArmStopButton.setText(QCoreApplication.translate("Frame", u"\u6025\u505c", None))
        self.RobotArmStopButton.setProperty("lightCustomQss", QCoreApplication.translate("Frame", u"PushButton {\n"
"    background: rgb(225, 41, 41);\n"
"    color: white;\n"
"}\n"
"PushButton:hover {\n"
"    background: rgba(225, 41, 41, 0.5);\n"
"    color: white;\n"
"}\n"
"PushButton:pressed {\n"
"    background: rgb(200, 20, 20);\n"
"    color: white;\n"
"}\n"
"PushButton:disabled {\n"
"    background: rgba(225, 41, 41, 0.5);\n"
"    color: white;\n"
"}", None))
        self.JointOneLabel.setText(QCoreApplication.translate("Frame", u"\u5173\u82821", None))
        self.JointOneSubButton.setProperty("lightCustomQss", QCoreApplication.translate("Frame", u"ToolButton {\n"
"    background: rgb(33, 150, 243);\n"
"}\n"
"\n"
"ToolButton:hover {\n"
"    background: rgb(33, 150, 243);\n"
"}", None))
        self.JointOneAddButton.setProperty("lightCustomQss", QCoreApplication.translate("Frame", u"ToolButton {\n"
"    background: rgb(33, 150, 243);\n"
"}\n"
"\n"
"ToolButton:hover {\n"
"    background: rgb(33, 150, 243);\n"
"}", None))
        self.JointTwoLabel.setText(QCoreApplication.translate("Frame", u"\u5173\u82822", None))
        self.JointTwoSubButton.setProperty("lightCustomQss", QCoreApplication.translate("Frame", u"ToolButton {\n"
"    background: rgb(33, 150, 243);\n"
"}\n"
"\n"
"ToolButton:hover {\n"
"    background: rgb(33, 150, 243);\n"
"}", None))
        self.JointTwoAddButton.setProperty("lightCustomQss", QCoreApplication.translate("Frame", u"ToolButton {\n"
"    background: rgb(33, 150, 243);\n"
"}\n"
"\n"
"ToolButton:hover {\n"
"    background: rgb(33, 150, 243);\n"
"}", None))
        self.JointThreeLabel.setText(QCoreApplication.translate("Frame", u"\u5173\u82823", None))
        self.JointThreeSubButton.setProperty("lightCustomQss", QCoreApplication.translate("Frame", u"ToolButton {\n"
"    background: rgb(33, 150, 243);\n"
"}\n"
"\n"
"ToolButton:hover {\n"
"    background: rgb(33, 150, 243);\n"
"}", None))
        self.JointThreeAddButton.setProperty("lightCustomQss", QCoreApplication.translate("Frame", u"ToolButton {\n"
"    background: rgb(33, 150, 243);\n"
"}\n"
"\n"
"ToolButton:hover {\n"
"    background: rgb(33, 150, 243);\n"
"}", None))
        self.JointFourLabel.setText(QCoreApplication.translate("Frame", u"\u5173\u82824", None))
        self.JointFourSubButton.setProperty("lightCustomQss", QCoreApplication.translate("Frame", u"ToolButton {\n"
"    background: rgb(33, 150, 243);\n"
"}\n"
"\n"
"ToolButton:hover {\n"
"    background: rgb(33, 150, 243);\n"
"}", None))
        self.JointFourAddButton.setProperty("lightCustomQss", QCoreApplication.translate("Frame", u"ToolButton {\n"
"    background: rgb(33, 150, 243);\n"
"}\n"
"\n"
"ToolButton:hover {\n"
"    background: rgb(33, 150, 243);\n"
"}", None))
        self.JointFiveLabel.setText(QCoreApplication.translate("Frame", u"\u5173\u82825", None))
        self.JointFiveSubButton.setProperty("lightCustomQss", QCoreApplication.translate("Frame", u"ToolButton {\n"
"    background: rgb(33, 150, 243);\n"
"}\n"
"\n"
"ToolButton:hover {\n"
"    background: rgb(33, 150, 243);\n"
"}", None))
        self.JointFiveAddButton.setProperty("lightCustomQss", QCoreApplication.translate("Frame", u"ToolButton {\n"
"    background: rgb(33, 150, 243);\n"
"}\n"
"\n"
"ToolButton:hover {\n"
"    background: rgb(33, 150, 243);\n"
"}", None))
        self.JointSixLabel.setText(QCoreApplication.translate("Frame", u"\u5173\u82826", None))
        self.JointSixSubButton.setProperty("lightCustomQss", QCoreApplication.translate("Frame", u"ToolButton {\n"
"    background: rgb(33, 150, 243);\n"
"}\n"
"\n"
"ToolButton:hover {\n"
"    background: rgb(33, 150, 243);\n"
"}", None))
        self.JointSixAddButton.setProperty("lightCustomQss", QCoreApplication.translate("Frame", u"ToolButton {\n"
"    background: rgb(33, 150, 243);\n"
"}\n"
"\n"
"ToolButton:hover {\n"
"    background: rgb(33, 150, 243);\n"
"}", None))
        self.JointStepLabel.setText(QCoreApplication.translate("Frame", u"\u6b65\u957f", None))
        self.JointStepSubButton.setProperty("lightCustomQss", QCoreApplication.translate("Frame", u"ToolButton {\n"
"    background: rgb(33, 150, 243);\n"
"}\n"
"\n"
"ToolButton:hover {\n"
"    background: rgb(33, 150, 243);\n"
"}", None))
        self.JointStepEdit.setText(QCoreApplication.translate("Frame", u"5", None))
        self.JointStepAddButton.setProperty("lightCustomQss", QCoreApplication.translate("Frame", u"ToolButton {\n"
"    background: rgb(33, 150, 243);\n"
"}\n"
"\n"
"ToolButton:hover {\n"
"    background: rgb(33, 150, 243);\n"
"}", None))
        self.JointSpeedLabel.setText(QCoreApplication.translate("Frame", u"\u901f\u5ea6", None))
        self.JointSpeedDecButton.setProperty("lightCustomQss", QCoreApplication.translate("Frame", u"ToolButton {\n"
"    background: rgb(33, 150, 243);\n"
"}\n"
"\n"
"ToolButton:hover {\n"
"    background: rgb(33, 150, 243);\n"
"}", None))
        self.JointSpeedEdit.setText(QCoreApplication.translate("Frame", u"50", None))
        self.JointSpeedUpButton.setProperty("lightCustomQss", QCoreApplication.translate("Frame", u"ToolButton {\n"
"    background: rgb(33, 150, 243);\n"
"}\n"
"\n"
"ToolButton:hover {\n"
"    background: rgb(33, 150, 243);\n"
"}", None))
        self.JointDelayTimeLabel.setText(QCoreApplication.translate("Frame", u"\u5ef6\u65f6", None))
        self.JointDelayTimeSubButton.setProperty("lightCustomQss", QCoreApplication.translate("Frame", u"ToolButton {\n"
"    background: rgb(33, 150, 243);\n"
"}\n"
"\n"
"ToolButton:hover {\n"
"    background: rgb(33, 150, 243);\n"
"}", None))
        self.JointDelayTimeEdit.setText(QCoreApplication.translate("Frame", u"1", None))
        self.JointDelayTimeAddButton.setProperty("lightCustomQss", QCoreApplication.translate("Frame", u"ToolButton {\n"
"    background: rgb(33, 150, 243);\n"
"}\n"
"\n"
"ToolButton:hover {\n"
"    background: rgb(33, 150, 243);\n"
"}", None))
        self.XLable.setText(QCoreApplication.translate("Frame", u"X", None))
        self.XLable.setProperty("lightCustomQss", QCoreApplication.translate("Frame", u"PushButton {     background: rgb(0, 170, 255); }  PushButton:hover {     background: rgb(0, 170, 255); }", None))
        self.XAxisSubButton.setProperty("lightCustomQss", QCoreApplication.translate("Frame", u"ToolButton {\n"
"    background: rgb(33, 150, 243);\n"
"}\n"
"\n"
"ToolButton:hover {\n"
"    background: rgb(33, 150, 243);\n"
"}", None))
        self.XAxisAddButton.setProperty("lightCustomQss", QCoreApplication.translate("Frame", u"ToolButton {\n"
"    background: rgb(33, 150, 243);\n"
"}\n"
"\n"
"ToolButton:hover {\n"
"    background: rgb(33, 150, 243);\n"
"}", None))
        self.YLable.setText(QCoreApplication.translate("Frame", u"Y", None))
        self.YAxisSubButton.setProperty("lightCustomQss", QCoreApplication.translate("Frame", u"ToolButton {\n"
"    background: rgb(33, 150, 243);\n"
"}\n"
"\n"
"ToolButton:hover {\n"
"    background: rgb(33, 150, 243);\n"
"}", None))
        self.YAxisAddButton.setProperty("lightCustomQss", QCoreApplication.translate("Frame", u"ToolButton {\n"
"    background: rgb(33, 150, 243);\n"
"}\n"
"\n"
"ToolButton:hover {\n"
"    background: rgb(33, 150, 243);\n"
"}", None))
        self.Zlable.setText(QCoreApplication.translate("Frame", u"Z", None))
        self.ZAxisSubButton.setProperty("lightCustomQss", QCoreApplication.translate("Frame", u"ToolButton {\n"
"    background: rgb(33, 150, 243);\n"
"}\n"
"\n"
"ToolButton:hover {\n"
"    background: rgb(33, 150, 243);\n"
"}", None))
        self.ZAxisAddButton.setProperty("lightCustomQss", QCoreApplication.translate("Frame", u"ToolButton {\n"
"    background: rgb(33, 150, 243);\n"
"}\n"
"\n"
"ToolButton:hover {\n"
"    background: rgb(33, 150, 243);\n"
"}", None))
        self.CoordinateStepLable.setText(QCoreApplication.translate("Frame", u"\u6b65\u957f", None))
        self.CoordinateStepSubButton.setProperty("lightCustomQss", QCoreApplication.translate("Frame", u"ToolButton {\n"
"    background: rgb(33, 150, 243);\n"
"}\n"
"\n"
"ToolButton:hover {\n"
"    background: rgb(33, 150, 243);\n"
"}", None))
        self.CoordinateStepEdit.setText(QCoreApplication.translate("Frame", u"10.000", None))
        self.CoordinateAddButton.setProperty("lightCustomQss", QCoreApplication.translate("Frame", u"ToolButton {\n"
"    background: rgb(33, 150, 243);\n"
"}\n"
"\n"
"ToolButton:hover {\n"
"    background: rgb(33, 150, 243);\n"
"}", None))
        self.RxLabel.setText(QCoreApplication.translate("Frame", u"Rx", None))
        self.RxAxisSubButton.setProperty("lightCustomQss", QCoreApplication.translate("Frame", u"ToolButton {\n"
"    background: rgb(33, 150, 243);\n"
"}\n"
"\n"
"ToolButton:hover {\n"
"    background: rgb(33, 150, 243);\n"
"}", None))
        self.RxAxisAddButton.setProperty("lightCustomQss", QCoreApplication.translate("Frame", u"ToolButton {\n"
"    background: rgb(33, 150, 243);\n"
"}\n"
"\n"
"ToolButton:hover {\n"
"    background: rgb(33, 150, 243);\n"
"}", None))
        self.RyLabel.setText(QCoreApplication.translate("Frame", u"Ry", None))
        self.RyAxisSubButton.setProperty("lightCustomQss", QCoreApplication.translate("Frame", u"ToolButton {\n"
"    background: rgb(33, 150, 243);\n"
"}\n"
"\n"
"ToolButton:hover {\n"
"    background: rgb(33, 150, 243);\n"
"}", None))
        self.RyAxisAddButton.setProperty("lightCustomQss", QCoreApplication.translate("Frame", u"ToolButton {\n"
"    background: rgb(33, 150, 243);\n"
"}\n"
"\n"
"ToolButton:hover {\n"
"    background: rgb(33, 150, 243);\n"
"}", None))
        self.RzLabel.setText(QCoreApplication.translate("Frame", u"Rz", None))
        self.RzAxisSubButton.setProperty("lightCustomQss", QCoreApplication.translate("Frame", u"ToolButton {\n"
"    background: rgb(33, 150, 243);\n"
"}\n"
"\n"
"ToolButton:hover {\n"
"    background: rgb(33, 150, 243);\n"
"}", None))
        self.RzAxisAddButton.setProperty("lightCustomQss", QCoreApplication.translate("Frame", u"ToolButton {\n"
"    background: rgb(33, 150, 243);\n"
"}\n"
"\n"
"ToolButton:hover {\n"
"    background: rgb(33, 150, 243);\n"
"}", None))
        self.ApStepLabel.setText(QCoreApplication.translate("Frame", u"\u89d2\u5ea6", None))
        self.ApStepSubButton.setProperty("lightCustomQss", QCoreApplication.translate("Frame", u"ToolButton {\n"
"    background: rgb(33, 150, 243);\n"
"}\n"
"\n"
"ToolButton:hover {\n"
"    background: rgb(33, 150, 243);\n"
"}", None))
        self.ApStepEdit.setText(QCoreApplication.translate("Frame", u"10", None))
        self.ApStepAddButton.setProperty("lightCustomQss", QCoreApplication.translate("Frame", u"ToolButton {\n"
"    background: rgb(33, 150, 243);\n"
"}\n"
"\n"
"ToolButton:hover {\n"
"    background: rgb(33, 150, 243);\n"
"}", None))
        self.SwitchButtonOneLable.setText(QCoreApplication.translate("Frame", u"IO 1", None))
        self.SwitchButtonOne.setOnText(QCoreApplication.translate("Frame", u"\u5f00", None))
        self.SwitchButtonOne.setOffText(QCoreApplication.translate("Frame", u"\u5173", None))
        self.SwitchButtonTwoLable.setText(QCoreApplication.translate("Frame", u"IO 2", None))
        self.SwitchButtonTwo.setOnText(QCoreApplication.translate("Frame", u"\u5f00", None))
        self.SwitchButtonTwo.setOffText(QCoreApplication.translate("Frame", u"\u5173", None))
        self.SwitchButtonThreeLable.setText(QCoreApplication.translate("Frame", u"IO 3", None))
        self.SwitchButtonThree.setOnText(QCoreApplication.translate("Frame", u"\u5f00", None))
        self.SwitchButtonThree.setOffText(QCoreApplication.translate("Frame", u"\u5173", None))
        self.SwitchButtonFourLable.setText(QCoreApplication.translate("Frame", u"IO 4", None))
        self.SwitchButtonFour.setOnText(QCoreApplication.translate("Frame", u"\u5f00", None))
        self.SwitchButtonFour.setOffText(QCoreApplication.translate("Frame", u"\u5173", None))
        self.ArmToolLabel.setText(QCoreApplication.translate("Frame", u"\u5de5\u5177", None))
        self.BodyLabel.setText(QCoreApplication.translate("Frame", u"\u6267\u884c", None))
        self.ArmToolSwitchButton.setOnText(QCoreApplication.translate("Frame", u"\u5438\u53d6", None))
        self.ArmToolSwitchButton.setOffText(QCoreApplication.translate("Frame", u"\u91ca\u653e", None))
        self.RobotArmZeroButton.setText(QCoreApplication.translate("Frame", u"\u56de\u96f6", None))
        self.RobotArmZeroButton.setProperty("lightCustomQss", QCoreApplication.translate("Frame", u"PushButton {\n"
"    background: rgb(255, 224, 0);\n"
"}\n"
"\n"
"PushButton:hover {\n"
"    background: rgb(255, 224, 0);\n"
"}", None))
        self.RobotArmResetButton.setText(QCoreApplication.translate("Frame", u"\u521d\u59cb\u5316", None))
        self.RobotArmResetButton.setProperty("lightCustomQss", QCoreApplication.translate("Frame", u"PushButton {\n"
"    background: rgb(0, 51, 160);\n"
"    color:white;\n"
"}\n"
"\n"
"PushButton:hover {\n"
"    background: rgb(0, 51, 160);\n"
"    color:white;\n"
"}", None))
    # retranslateUi

