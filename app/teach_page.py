# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'teach_page.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
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
    QSizePolicy, QSpacerItem, QStackedWidget, QTableWidgetItem,
    QVBoxLayout, QWidget)

from qfluentwidgets import (CardWidget, ComboBox, HorizontalSeparator, LineEdit,
    Pivot, PlainTextEdit, PushButton, RadioButton,
    SegmentedWidget, StrongBodyLabel, TableWidget, ToolButton,
    VerticalSeparator)

class teach_page_frame(object):
    def setupUi(self, Frame):
        if not Frame.objectName():
            Frame.setObjectName(u"Frame")
        Frame.resize(1285, 688)
        self.horizontalLayout_5 = QHBoxLayout(Frame)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.verticalLayout_10 = QVBoxLayout()
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.TeachLayout = QVBoxLayout()
        self.TeachLayout.setObjectName(u"TeachLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer_30 = QSpacerItem(10, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_30)

        self.ActionImportButton = ToolButton(Frame)
        self.ActionImportButton.setObjectName(u"ActionImportButton")

        self.horizontalLayout.addWidget(self.ActionImportButton)

        self.horizontalSpacer_31 = QSpacerItem(5, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_31)

        self.ActionOutputButton = ToolButton(Frame)
        self.ActionOutputButton.setObjectName(u"ActionOutputButton")

        self.horizontalLayout.addWidget(self.ActionOutputButton)

        self.horizontalSpacer = QSpacerItem(320, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.RecordActivateButton = RadioButton(Frame)
        self.RecordActivateButton.setObjectName(u"RecordActivateButton")

        self.horizontalLayout.addWidget(self.RecordActivateButton)

        self.RecordDeActivateButton = RadioButton(Frame)
        self.RecordDeActivateButton.setObjectName(u"RecordDeActivateButton")
        self.RecordDeActivateButton.setChecked(True)

        self.horizontalLayout.addWidget(self.RecordDeActivateButton)

        self.VerticalSeparator_4 = VerticalSeparator(Frame)
        self.VerticalSeparator_4.setObjectName(u"VerticalSeparator_4")

        self.horizontalLayout.addWidget(self.VerticalSeparator_4)

        self.ActionStepRunButton = ToolButton(Frame)
        self.ActionStepRunButton.setObjectName(u"ActionStepRunButton")

        self.horizontalLayout.addWidget(self.ActionStepRunButton)

        self.horizontalSpacer_3 = QSpacerItem(5, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_3)

        self.ActionRunButton = ToolButton(Frame)
        self.ActionRunButton.setObjectName(u"ActionRunButton")

        self.horizontalLayout.addWidget(self.ActionRunButton)

        self.horizontalSpacer_4 = QSpacerItem(5, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_4)

        self.ActionLoopRunButton = ToolButton(Frame)
        self.ActionLoopRunButton.setObjectName(u"ActionLoopRunButton")

        self.horizontalLayout.addWidget(self.ActionLoopRunButton)

        self.ActionLoopTimes = LineEdit(Frame)
        self.ActionLoopTimes.setObjectName(u"ActionLoopTimes")
        self.ActionLoopTimes.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.ActionLoopTimes)

        self.horizontalSpacer_27 = QSpacerItem(10, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_27)


        self.TeachLayout.addLayout(self.horizontalLayout)

        self.ActionTableWidget = TableWidget(Frame)
        if (self.ActionTableWidget.columnCount() < 12):
            self.ActionTableWidget.setColumnCount(12)
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
        __qtablewidgetitem11 = QTableWidgetItem()
        self.ActionTableWidget.setHorizontalHeaderItem(11, __qtablewidgetitem11)
        self.ActionTableWidget.setObjectName(u"ActionTableWidget")

        self.TeachLayout.addWidget(self.ActionTableWidget)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer_29 = QSpacerItem(10, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_29)

        self.ActionDeleteButton = ToolButton(Frame)
        self.ActionDeleteButton.setObjectName(u"ActionDeleteButton")

        self.horizontalLayout_2.addWidget(self.ActionDeleteButton)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_5)

        self.ActionAddButton = ToolButton(Frame)
        self.ActionAddButton.setObjectName(u"ActionAddButton")

        self.horizontalLayout_2.addWidget(self.ActionAddButton)

        self.horizontalSpacer_6 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_6)

        self.ActionUpdateRowButton = ToolButton(Frame)
        self.ActionUpdateRowButton.setObjectName(u"ActionUpdateRowButton")
        icon = QIcon()
        iconThemeName = u"SEND"
        if QIcon.hasThemeIcon(iconThemeName):
            icon = QIcon.fromTheme(iconThemeName)
        else:
            icon.addFile(u".", QSize(), QIcon.Normal, QIcon.Off)

        self.ActionUpdateRowButton.setIcon(icon)

        self.horizontalLayout_2.addWidget(self.ActionUpdateRowButton)

        self.horizontalSpacer_7 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_7)

        self.ActionUpdateColButton = ToolButton(Frame)
        self.ActionUpdateColButton.setObjectName(u"ActionUpdateColButton")

        self.horizontalLayout_2.addWidget(self.ActionUpdateColButton)

        self.horizontalSpacer_28 = QSpacerItem(10, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_28)


        self.TeachLayout.addLayout(self.horizontalLayout_2)


        self.verticalLayout_10.addLayout(self.TeachLayout)

        self.HorizontalSeparator = HorizontalSeparator(Frame)
        self.HorizontalSeparator.setObjectName(u"HorizontalSeparator")

        self.verticalLayout_10.addWidget(self.HorizontalSeparator)

        self.TeachArmRunLogWindow = PlainTextEdit(Frame)
        self.TeachArmRunLogWindow.setObjectName(u"TeachArmRunLogWindow")
        self.TeachArmRunLogWindow.setReadOnly(True)

        self.verticalLayout_10.addWidget(self.TeachArmRunLogWindow)

        self.verticalLayout_10.setStretch(0, 7)
        self.verticalLayout_10.setStretch(2, 1)

        self.horizontalLayout_4.addLayout(self.verticalLayout_10)

        self.VerticalSeparator = VerticalSeparator(Frame)
        self.VerticalSeparator.setObjectName(u"VerticalSeparator")

        self.horizontalLayout_4.addWidget(self.VerticalSeparator)

        self.verticalLayout_11 = QVBoxLayout()
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.RobotArmControlSegmentedWidget = SegmentedWidget(Frame)
        self.RobotArmControlSegmentedWidget.setObjectName(u"RobotArmControlSegmentedWidget")

        self.verticalLayout_11.addWidget(self.RobotArmControlSegmentedWidget)

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
        self.horizontalSpacer_40 = QSpacerItem(10, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.JointOneLaylout.addItem(self.horizontalSpacer_40)

        self.JointOneLabel = StrongBodyLabel(self.ArmAngleControlCard)
        self.JointOneLabel.setObjectName(u"JointOneLabel")

        self.JointOneLaylout.addWidget(self.JointOneLabel)

        self.horizontalSpacer_2 = QSpacerItem(22, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

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

        self.horizontalSpacer_49 = QSpacerItem(10, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.JointOneLaylout.addItem(self.horizontalSpacer_49)


        self.verticalLayout_2.addLayout(self.JointOneLaylout)

        self.JointTwolout = QHBoxLayout()
        self.JointTwolout.setObjectName(u"JointTwolout")
        self.horizontalSpacer_41 = QSpacerItem(10, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.JointTwolout.addItem(self.horizontalSpacer_41)

        self.JointTwoLabel = StrongBodyLabel(self.ArmAngleControlCard)
        self.JointTwoLabel.setObjectName(u"JointTwoLabel")

        self.JointTwolout.addWidget(self.JointTwoLabel)

        self.horizontalSpacer_9 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

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

        self.horizontalSpacer_50 = QSpacerItem(10, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.JointTwolout.addItem(self.horizontalSpacer_50)


        self.verticalLayout_2.addLayout(self.JointTwolout)

        self.JointThreeLaylout = QHBoxLayout()
        self.JointThreeLaylout.setObjectName(u"JointThreeLaylout")
        self.horizontalSpacer_42 = QSpacerItem(10, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.JointThreeLaylout.addItem(self.horizontalSpacer_42)

        self.JointThreeLabel = StrongBodyLabel(self.ArmAngleControlCard)
        self.JointThreeLabel.setObjectName(u"JointThreeLabel")

        self.JointThreeLaylout.addWidget(self.JointThreeLabel)

        self.horizontalSpacer_10 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

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

        self.horizontalSpacer_51 = QSpacerItem(10, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.JointThreeLaylout.addItem(self.horizontalSpacer_51)


        self.verticalLayout_2.addLayout(self.JointThreeLaylout)

        self.JointFourLaylout = QHBoxLayout()
        self.JointFourLaylout.setObjectName(u"JointFourLaylout")
        self.horizontalSpacer_43 = QSpacerItem(10, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.JointFourLaylout.addItem(self.horizontalSpacer_43)

        self.JointFourLabel = StrongBodyLabel(self.ArmAngleControlCard)
        self.JointFourLabel.setObjectName(u"JointFourLabel")

        self.JointFourLaylout.addWidget(self.JointFourLabel)

        self.horizontalSpacer_11 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

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

        self.horizontalSpacer_52 = QSpacerItem(10, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.JointFourLaylout.addItem(self.horizontalSpacer_52)


        self.verticalLayout_2.addLayout(self.JointFourLaylout)

        self.JointFiveLaylout = QHBoxLayout()
        self.JointFiveLaylout.setObjectName(u"JointFiveLaylout")
        self.horizontalSpacer_44 = QSpacerItem(10, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.JointFiveLaylout.addItem(self.horizontalSpacer_44)

        self.JointFiveLabel = StrongBodyLabel(self.ArmAngleControlCard)
        self.JointFiveLabel.setObjectName(u"JointFiveLabel")

        self.JointFiveLaylout.addWidget(self.JointFiveLabel)

        self.horizontalSpacer_12 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

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

        self.horizontalSpacer_53 = QSpacerItem(10, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.JointFiveLaylout.addItem(self.horizontalSpacer_53)


        self.verticalLayout_2.addLayout(self.JointFiveLaylout)

        self.JointSixLaylout = QHBoxLayout()
        self.JointSixLaylout.setObjectName(u"JointSixLaylout")
        self.horizontalSpacer_45 = QSpacerItem(10, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.JointSixLaylout.addItem(self.horizontalSpacer_45)

        self.JointSixLabel = StrongBodyLabel(self.ArmAngleControlCard)
        self.JointSixLabel.setObjectName(u"JointSixLabel")

        self.JointSixLaylout.addWidget(self.JointSixLabel)

        self.horizontalSpacer_13 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

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

        self.horizontalSpacer_54 = QSpacerItem(10, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.JointSixLaylout.addItem(self.horizontalSpacer_54)


        self.verticalLayout_2.addLayout(self.JointSixLaylout)

        self.JointAngleStepLaylout = QHBoxLayout()
        self.JointAngleStepLaylout.setObjectName(u"JointAngleStepLaylout")
        self.horizontalSpacer_46 = QSpacerItem(10, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.JointAngleStepLaylout.addItem(self.horizontalSpacer_46)

        self.JointStepLabel = StrongBodyLabel(self.ArmAngleControlCard)
        self.JointStepLabel.setObjectName(u"JointStepLabel")

        self.JointAngleStepLaylout.addWidget(self.JointStepLabel)

        self.horizontalSpacer_14 = QSpacerItem(27, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

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

        self.horizontalSpacer_55 = QSpacerItem(10, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.JointAngleStepLaylout.addItem(self.horizontalSpacer_55)


        self.verticalLayout_2.addLayout(self.JointAngleStepLaylout)

        self.JointSpeedLaylout = QHBoxLayout()
        self.JointSpeedLaylout.setObjectName(u"JointSpeedLaylout")
        self.horizontalSpacer_47 = QSpacerItem(10, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.JointSpeedLaylout.addItem(self.horizontalSpacer_47)

        self.JointSpeedLabel = StrongBodyLabel(self.ArmAngleControlCard)
        self.JointSpeedLabel.setObjectName(u"JointSpeedLabel")

        self.JointSpeedLaylout.addWidget(self.JointSpeedLabel)

        self.horizontalSpacer_15 = QSpacerItem(27, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

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

        self.horizontalSpacer_56 = QSpacerItem(10, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.JointSpeedLaylout.addItem(self.horizontalSpacer_56)


        self.verticalLayout_2.addLayout(self.JointSpeedLaylout)

        self.JointDelayTimeLaylout = QHBoxLayout()
        self.JointDelayTimeLaylout.setObjectName(u"JointDelayTimeLaylout")
        self.horizontalSpacer_48 = QSpacerItem(10, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.JointDelayTimeLaylout.addItem(self.horizontalSpacer_48)

        self.JointDelayTimeLabel = StrongBodyLabel(self.ArmAngleControlCard)
        self.JointDelayTimeLabel.setObjectName(u"JointDelayTimeLabel")

        self.JointDelayTimeLaylout.addWidget(self.JointDelayTimeLabel)

        self.horizontalSpacer_18 = QSpacerItem(27, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

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

        self.horizontalSpacer_57 = QSpacerItem(10, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

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
        self.horizontalLayout_21 = QHBoxLayout(self.ArmEndToolsCoordinateControlCard)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalSpacer_32 = QSpacerItem(10, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_32)

        self.XLable = StrongBodyLabel(self.ArmEndToolsCoordinateControlCard)
        self.XLable.setObjectName(u"XLable")

        self.horizontalLayout_10.addWidget(self.XLable)

        self.horizontalSpacer_19 = QSpacerItem(32, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

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

        self.horizontalSpacer_36 = QSpacerItem(10, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_36)


        self.verticalLayout_4.addLayout(self.horizontalLayout_10)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalSpacer_33 = QSpacerItem(10, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.horizontalLayout_11.addItem(self.horizontalSpacer_33)

        self.YLable = StrongBodyLabel(self.ArmEndToolsCoordinateControlCard)
        self.YLable.setObjectName(u"YLable")

        self.horizontalLayout_11.addWidget(self.YLable)

        self.horizontalSpacer_20 = QSpacerItem(32, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

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

        self.horizontalSpacer_37 = QSpacerItem(10, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.horizontalLayout_11.addItem(self.horizontalSpacer_37)


        self.verticalLayout_4.addLayout(self.horizontalLayout_11)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalSpacer_34 = QSpacerItem(10, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_34)

        self.Zlable = StrongBodyLabel(self.ArmEndToolsCoordinateControlCard)
        self.Zlable.setObjectName(u"Zlable")

        self.horizontalLayout_13.addWidget(self.Zlable)

        self.horizontalSpacer_21 = QSpacerItem(32, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

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

        self.horizontalSpacer_38 = QSpacerItem(10, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_38)


        self.verticalLayout_4.addLayout(self.horizontalLayout_13)

        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalSpacer_35 = QSpacerItem(10, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.horizontalLayout_14.addItem(self.horizontalSpacer_35)

        self.CoordinateStepLable = StrongBodyLabel(self.ArmEndToolsCoordinateControlCard)
        self.CoordinateStepLable.setObjectName(u"CoordinateStepLable")

        self.horizontalLayout_14.addWidget(self.CoordinateStepLable)

        self.horizontalSpacer_22 = QSpacerItem(10, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

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

        self.horizontalSpacer_39 = QSpacerItem(10, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.horizontalLayout_14.addItem(self.horizontalSpacer_39)


        self.verticalLayout_4.addLayout(self.horizontalLayout_14)


        self.horizontalLayout_21.addLayout(self.verticalLayout_4)


        self.horizontalLayout_6.addWidget(self.ArmEndToolsCoordinateControlCard)

        self.ArmActionControlStackWidget.addWidget(self.ArmEndToolsCoordinateControlPage)
        self.ArmEndToolsPositionControlPage = QWidget()
        self.ArmEndToolsPositionControlPage.setObjectName(u"ArmEndToolsPositionControlPage")
        self.verticalLayout = QVBoxLayout(self.ArmEndToolsPositionControlPage)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.ArmEndToolsPositionControlCard = CardWidget(self.ArmEndToolsPositionControlPage)
        self.ArmEndToolsPositionControlCard.setObjectName(u"ArmEndToolsPositionControlCard")
        self.horizontalLayout_23 = QHBoxLayout(self.ArmEndToolsPositionControlCard)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalSpacer_58 = QSpacerItem(10, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.horizontalLayout_15.addItem(self.horizontalSpacer_58)

        self.RxLabel = StrongBodyLabel(self.ArmEndToolsPositionControlCard)
        self.RxLabel.setObjectName(u"RxLabel")

        self.horizontalLayout_15.addWidget(self.RxLabel)

        self.horizontalSpacer_23 = QSpacerItem(25, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.horizontalLayout_15.addItem(self.horizontalSpacer_23)

        self.RxAxisSubButton = ToolButton(self.ArmEndToolsPositionControlCard)
        self.RxAxisSubButton.setObjectName(u"RxAxisSubButton")

        self.horizontalLayout_15.addWidget(self.RxAxisSubButton)

        self.RxAxisEdit = LineEdit(self.ArmEndToolsPositionControlCard)
        self.RxAxisEdit.setObjectName(u"RxAxisEdit")
        self.RxAxisEdit.setAlignment(Qt.AlignCenter)
        self.RxAxisEdit.setReadOnly(True)

        self.horizontalLayout_15.addWidget(self.RxAxisEdit)

        self.RxAxisAddButton = ToolButton(self.ArmEndToolsPositionControlCard)
        self.RxAxisAddButton.setObjectName(u"RxAxisAddButton")

        self.horizontalLayout_15.addWidget(self.RxAxisAddButton)

        self.horizontalSpacer_62 = QSpacerItem(10, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.horizontalLayout_15.addItem(self.horizontalSpacer_62)


        self.verticalLayout_5.addLayout(self.horizontalLayout_15)

        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalSpacer_59 = QSpacerItem(10, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.horizontalLayout_16.addItem(self.horizontalSpacer_59)

        self.RyLabel = StrongBodyLabel(self.ArmEndToolsPositionControlCard)
        self.RyLabel.setObjectName(u"RyLabel")

        self.horizontalLayout_16.addWidget(self.RyLabel)

        self.horizontalSpacer_24 = QSpacerItem(24, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.horizontalLayout_16.addItem(self.horizontalSpacer_24)

        self.RyAxisSubButton = ToolButton(self.ArmEndToolsPositionControlCard)
        self.RyAxisSubButton.setObjectName(u"RyAxisSubButton")

        self.horizontalLayout_16.addWidget(self.RyAxisSubButton)

        self.RyAxisEdit = LineEdit(self.ArmEndToolsPositionControlCard)
        self.RyAxisEdit.setObjectName(u"RyAxisEdit")
        self.RyAxisEdit.setAlignment(Qt.AlignCenter)
        self.RyAxisEdit.setReadOnly(True)

        self.horizontalLayout_16.addWidget(self.RyAxisEdit)

        self.RyAxisAddButton = ToolButton(self.ArmEndToolsPositionControlCard)
        self.RyAxisAddButton.setObjectName(u"RyAxisAddButton")

        self.horizontalLayout_16.addWidget(self.RyAxisAddButton)

        self.horizontalSpacer_63 = QSpacerItem(10, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.horizontalLayout_16.addItem(self.horizontalSpacer_63)


        self.verticalLayout_5.addLayout(self.horizontalLayout_16)

        self.horizontalLayout_17 = QHBoxLayout()
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalSpacer_60 = QSpacerItem(10, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.horizontalLayout_17.addItem(self.horizontalSpacer_60)

        self.RzLabel = StrongBodyLabel(self.ArmEndToolsPositionControlCard)
        self.RzLabel.setObjectName(u"RzLabel")

        self.horizontalLayout_17.addWidget(self.RzLabel)

        self.horizontalSpacer_25 = QSpacerItem(24, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.horizontalLayout_17.addItem(self.horizontalSpacer_25)

        self.RzAxisSubButton = ToolButton(self.ArmEndToolsPositionControlCard)
        self.RzAxisSubButton.setObjectName(u"RzAxisSubButton")

        self.horizontalLayout_17.addWidget(self.RzAxisSubButton)

        self.RzAxisEdit = LineEdit(self.ArmEndToolsPositionControlCard)
        self.RzAxisEdit.setObjectName(u"RzAxisEdit")
        self.RzAxisEdit.setAlignment(Qt.AlignCenter)
        self.RzAxisEdit.setReadOnly(True)

        self.horizontalLayout_17.addWidget(self.RzAxisEdit)

        self.RzAxisAddButton = ToolButton(self.ArmEndToolsPositionControlCard)
        self.RzAxisAddButton.setObjectName(u"RzAxisAddButton")

        self.horizontalLayout_17.addWidget(self.RzAxisAddButton)

        self.horizontalSpacer_64 = QSpacerItem(10, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.horizontalLayout_17.addItem(self.horizontalSpacer_64)


        self.verticalLayout_5.addLayout(self.horizontalLayout_17)

        self.horizontalLayout_18 = QHBoxLayout()
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.horizontalSpacer_61 = QSpacerItem(10, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.horizontalLayout_18.addItem(self.horizontalSpacer_61)

        self.ApStepLabel = StrongBodyLabel(self.ArmEndToolsPositionControlCard)
        self.ApStepLabel.setObjectName(u"ApStepLabel")

        self.horizontalLayout_18.addWidget(self.ApStepLabel)

        self.horizontalSpacer_26 = QSpacerItem(10, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.horizontalLayout_18.addItem(self.horizontalSpacer_26)

        self.ApStepSubButton = ToolButton(self.ArmEndToolsPositionControlCard)
        self.ApStepSubButton.setObjectName(u"ApStepSubButton")

        self.horizontalLayout_18.addWidget(self.ApStepSubButton)

        self.ApStepEdit = LineEdit(self.ArmEndToolsPositionControlCard)
        self.ApStepEdit.setObjectName(u"ApStepEdit")
        self.ApStepEdit.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_18.addWidget(self.ApStepEdit)

        self.ApStepAddButton = ToolButton(self.ArmEndToolsPositionControlCard)
        self.ApStepAddButton.setObjectName(u"ApStepAddButton")

        self.horizontalLayout_18.addWidget(self.ApStepAddButton)

        self.horizontalSpacer_65 = QSpacerItem(10, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.horizontalLayout_18.addItem(self.horizontalSpacer_65)


        self.verticalLayout_5.addLayout(self.horizontalLayout_18)


        self.horizontalLayout_23.addLayout(self.verticalLayout_5)


        self.verticalLayout.addWidget(self.ArmEndToolsPositionControlCard)

        self.ArmActionControlStackWidget.addWidget(self.ArmEndToolsPositionControlPage)

        self.verticalLayout_11.addWidget(self.ArmActionControlStackWidget)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.horizontalLayout_tools = QHBoxLayout()
        self.horizontalLayout_tools.setSpacing(6)
        self.horizontalLayout_tools.setObjectName(u"horizontalLayout_tools")
        self.horizontalSpacer_16 = QSpacerItem(5, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.horizontalLayout_tools.addItem(self.horizontalSpacer_16)

        self.ArmToolLabel = StrongBodyLabel(Frame)
        self.ArmToolLabel.setObjectName(u"ArmToolLabel")

        self.horizontalLayout_tools.addWidget(self.ArmToolLabel)

        self.ArmToolComboBox = ComboBox(Frame)
        self.ArmToolComboBox.setObjectName(u"ArmToolComboBox")

        self.horizontalLayout_tools.addWidget(self.ArmToolComboBox)

        self.horizontalLayout_tools.setStretch(1, 2)
        self.horizontalLayout_tools.setStretch(2, 8)

        self.verticalLayout_9.addLayout(self.horizontalLayout_tools)

        self.horizontalLayout_tool_control = QHBoxLayout()
        self.horizontalLayout_tool_control.setObjectName(u"horizontalLayout_tool_control")
        self.horizontalSpacer_17 = QSpacerItem(5, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.horizontalLayout_tool_control.addItem(self.horizontalSpacer_17)

        self.ArmControlLabel = StrongBodyLabel(Frame)
        self.ArmControlLabel.setObjectName(u"ArmControlLabel")

        self.horizontalLayout_tool_control.addWidget(self.ArmControlLabel)

        self.ArmClawOpenButton = PushButton(Frame)
        self.ArmClawOpenButton.setObjectName(u"ArmClawOpenButton")

        self.horizontalLayout_tool_control.addWidget(self.ArmClawOpenButton)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_tool_control.addItem(self.horizontalSpacer_8)

        self.ArmClawCloseButton = PushButton(Frame)
        self.ArmClawCloseButton.setObjectName(u"ArmClawCloseButton")

        self.horizontalLayout_tool_control.addWidget(self.ArmClawCloseButton)


        self.verticalLayout_9.addLayout(self.horizontalLayout_tool_control)


        self.horizontalLayout_3.addLayout(self.verticalLayout_9)

        self.horizontalLayout_arm_init = QHBoxLayout()
        self.horizontalLayout_arm_init.setObjectName(u"horizontalLayout_arm_init")
        self.VerticalSeparator_3 = VerticalSeparator(Frame)
        self.VerticalSeparator_3.setObjectName(u"VerticalSeparator_3")

        self.horizontalLayout_arm_init.addWidget(self.VerticalSeparator_3)

        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.RobotArmResetButton = PushButton(Frame)
        self.RobotArmResetButton.setObjectName(u"RobotArmResetButton")

        self.verticalLayout_8.addWidget(self.RobotArmResetButton)

        self.RobotArmZeroButton = PushButton(Frame)
        self.RobotArmZeroButton.setObjectName(u"RobotArmZeroButton")

        self.verticalLayout_8.addWidget(self.RobotArmZeroButton)


        self.horizontalLayout_arm_init.addLayout(self.verticalLayout_8)

        self.RobotArmStopButton = PushButton(Frame)
        self.RobotArmStopButton.setObjectName(u"RobotArmStopButton")
        self.RobotArmStopButton.setMaximumSize(QSize(90, 90))

        self.horizontalLayout_arm_init.addWidget(self.RobotArmStopButton)


        self.horizontalLayout_3.addLayout(self.horizontalLayout_arm_init)

        self.horizontalLayout_3.setStretch(0, 4)
        self.horizontalLayout_3.setStretch(1, 7)

        self.verticalLayout_11.addLayout(self.horizontalLayout_3)

        self.verticalLayout_11.setStretch(1, 12)
        self.verticalLayout_11.setStretch(2, 2)

        self.horizontalLayout_4.addLayout(self.verticalLayout_11)

        self.horizontalLayout_4.setStretch(0, 7)
        self.horizontalLayout_4.setStretch(2, 3)

        self.horizontalLayout_5.addLayout(self.horizontalLayout_4)


        self.retranslateUi(Frame)

        self.ArmActionControlStackWidget.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(Frame)
    # setupUi

    def retranslateUi(self, Frame):
        Frame.setWindowTitle(QCoreApplication.translate("Frame", u"Frame", None))
        Frame.setProperty("lightCustomQss", "")
        self.ActionImportButton.setProperty("lightCustomQss", QCoreApplication.translate("Frame", u"ToolButton {\n"
"    background: rgb(125, 214, 249);\n"
"}\n"
"\n"
"ToolButton:hover {\n"
"    background: rgb(125, 214, 249);\n"
"}", None))
        self.ActionOutputButton.setProperty("lightCustomQss", QCoreApplication.translate("Frame", u"ToolButton {\n"
"    background: rgb(125, 214, 249);\n"
"}\n"
"\n"
"ToolButton:hover {\n"
"    background: rgb(125, 214, 249);\n"
"}", None))
        self.RecordActivateButton.setText(QCoreApplication.translate("Frame", u"\u5f55\u5236\u6a21\u5f0f", None))
        self.RecordDeActivateButton.setText(QCoreApplication.translate("Frame", u"\u666e\u901a\u6a21\u5f0f", None))
        self.ActionStepRunButton.setProperty("lightCustomQss", QCoreApplication.translate("Frame", u"ToolButton {\n"
"    background: rgb(125, 214, 249);\n"
"}\n"
"\n"
"ToolButton:hover {\n"
"    background: rgb(125, 214, 249);\n"
"}", None))
        self.ActionRunButton.setProperty("lightCustomQss", QCoreApplication.translate("Frame", u"ToolButton {\n"
"    background: rgb(125, 214, 249);\n"
"}\n"
"\n"
"ToolButton:hover {\n"
"    background: rgb(125, 214, 249);\n"
"}", None))
        self.ActionLoopRunButton.setProperty("lightCustomQss", QCoreApplication.translate("Frame", u"ToolButton {\n"
"    background: rgb(125, 214, 249);\n"
"}\n"
"\n"
"ToolButton:hover {\n"
"    background: rgb(125, 214, 249);\n"
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
        self.ActionDeleteButton.setProperty("lightCustomQss", QCoreApplication.translate("Frame", u"ToolButton {\n"
"    background: rgb(229, 142, 138);\n"
"}\n"
"\n"
"ToolButton:hover {\n"
"    background: rgb(229, 142, 138);\n"
"}", None))
        self.ActionAddButton.setProperty("lightCustomQss", QCoreApplication.translate("Frame", u"ToolButton {\n"
"    background: rgb(170, 211, 140);\n"
"}\n"
"\n"
"ToolButton:hover {\n"
"    background: rgb(170, 211, 140);\n"
"}", None))
        self.ActionUpdateRowButton.setProperty("lightCustomQss", QCoreApplication.translate("Frame", u"ToolButton {\n"
"    background: rgb(240, 203, 98);\n"
"}\n"
"\n"
"ToolButton:hover {\n"
"    background: rgb(240, 203, 98);\n"
"}", None))
        self.ActionUpdateColButton.setProperty("lightCustomQss", QCoreApplication.translate("Frame", u"ToolButton {\n"
"    background: rgb(125, 214, 249);\n"
"}\n"
"\n"
"ToolButton:hover {\n"
"    background: rgb(125, 214, 249);\n"
"}", None))
        self.JointOneLabel.setText(QCoreApplication.translate("Frame", u"\u5173\u82821", None))
        self.JointOneSubButton.setProperty("lightCustomQss", QCoreApplication.translate("Frame", u"ToolButton {\n"
"    background: rgb(125, 214, 249);\n"
"}\n"
"\n"
"ToolButton:hover {\n"
"    background: rgb(125, 214, 249);\n"
"}", None))
        self.JointOneAddButton.setProperty("lightCustomQss", QCoreApplication.translate("Frame", u"ToolButton {\n"
"    background: rgb(125, 214, 249);\n"
"}\n"
"\n"
"ToolButton:hover {\n"
"    background: rgb(125, 214, 249);\n"
"}", None))
        self.JointTwoLabel.setText(QCoreApplication.translate("Frame", u"\u5173\u82822", None))
        self.JointTwoSubButton.setProperty("lightCustomQss", QCoreApplication.translate("Frame", u"ToolButton {\n"
"    background: rgb(125, 214, 249);\n"
"}\n"
"\n"
"ToolButton:hover {\n"
"    background: rgb(125, 214, 249);\n"
"}", None))
        self.JointTwoAddButton.setProperty("lightCustomQss", QCoreApplication.translate("Frame", u"ToolButton {\n"
"    background: rgb(125, 214, 249);\n"
"}\n"
"\n"
"ToolButton:hover {\n"
"    background: rgb(125, 214, 249);\n"
"}", None))
        self.JointThreeLabel.setText(QCoreApplication.translate("Frame", u"\u5173\u82823", None))
        self.JointThreeSubButton.setProperty("lightCustomQss", QCoreApplication.translate("Frame", u"ToolButton {\n"
"    background: rgb(125, 214, 249);\n"
"}\n"
"\n"
"ToolButton:hover {\n"
"    background: rgb(125, 214, 249);\n"
"}", None))
        self.JointThreeAddButton.setProperty("lightCustomQss", QCoreApplication.translate("Frame", u"ToolButton {\n"
"    background: rgb(125, 214, 249);\n"
"}\n"
"\n"
"ToolButton:hover {\n"
"    background: rgb(125, 214, 249);\n"
"}", None))
        self.JointFourLabel.setText(QCoreApplication.translate("Frame", u"\u5173\u82824", None))
        self.JointFourSubButton.setProperty("lightCustomQss", QCoreApplication.translate("Frame", u"ToolButton {\n"
"    background: rgb(125, 214, 249);\n"
"}\n"
"\n"
"ToolButton:hover {\n"
"    background: rgb(125, 214, 249);\n"
"}", None))
        self.JointFourAddButton.setProperty("lightCustomQss", QCoreApplication.translate("Frame", u"ToolButton {\n"
"    background: rgb(125, 214, 249);\n"
"}\n"
"\n"
"ToolButton:hover {\n"
"    background: rgb(125, 214, 249);\n"
"}", None))
        self.JointFiveLabel.setText(QCoreApplication.translate("Frame", u"\u5173\u82825", None))
        self.JointFiveSubButton.setProperty("lightCustomQss", QCoreApplication.translate("Frame", u"ToolButton {\n"
"    background: rgb(125, 214, 249);\n"
"}\n"
"\n"
"ToolButton:hover {\n"
"    background: rgb(125, 214, 249);\n"
"}", None))
        self.JointFiveAddButton.setProperty("lightCustomQss", QCoreApplication.translate("Frame", u"ToolButton {\n"
"    background: rgb(125, 214, 249);\n"
"}\n"
"\n"
"ToolButton:hover {\n"
"    background: rgb(125, 214, 249);\n"
"}", None))
        self.JointSixLabel.setText(QCoreApplication.translate("Frame", u"\u5173\u82826", None))
        self.JointSixSubButton.setProperty("lightCustomQss", QCoreApplication.translate("Frame", u"ToolButton {\n"
"    background: rgb(125, 214, 249);\n"
"}\n"
"\n"
"ToolButton:hover {\n"
"    background: rgb(125, 214, 249);\n"
"}", None))
        self.JointSixAddButton.setProperty("lightCustomQss", QCoreApplication.translate("Frame", u"ToolButton {\n"
"    background: rgb(125, 214, 249);\n"
"}\n"
"\n"
"ToolButton:hover {\n"
"    background: rgb(125, 214, 249);\n"
"}", None))
        self.JointStepLabel.setText(QCoreApplication.translate("Frame", u"\u6b65\u957f", None))
        self.JointStepSubButton.setProperty("lightCustomQss", QCoreApplication.translate("Frame", u"ToolButton {\n"
"    background: rgb(125, 214, 249);\n"
"}\n"
"\n"
"ToolButton:hover {\n"
"    background: rgb(125, 214, 249);\n"
"}", None))
        self.JointStepEdit.setText(QCoreApplication.translate("Frame", u"5", None))
        self.JointStepAddButton.setProperty("lightCustomQss", QCoreApplication.translate("Frame", u"ToolButton {\n"
"    background: rgb(125, 214, 249);\n"
"}\n"
"\n"
"ToolButton:hover {\n"
"    background: rgb(125, 214, 249);\n"
"}", None))
        self.JointSpeedLabel.setText(QCoreApplication.translate("Frame", u"\u901f\u5ea6", None))
        self.JointSpeedDecButton.setProperty("lightCustomQss", QCoreApplication.translate("Frame", u"ToolButton {\n"
"    background: rgb(125, 214, 249);\n"
"}\n"
"\n"
"ToolButton:hover {\n"
"    background: rgb(125, 214, 249);\n"
"}", None))
        self.JointSpeedEdit.setText(QCoreApplication.translate("Frame", u"50", None))
        self.JointSpeedUpButton.setProperty("lightCustomQss", QCoreApplication.translate("Frame", u"ToolButton {\n"
"    background: rgb(125, 214, 249);\n"
"}\n"
"\n"
"ToolButton:hover {\n"
"    background: rgb(125, 214, 249);\n"
"}", None))
        self.JointDelayTimeLabel.setText(QCoreApplication.translate("Frame", u"\u5ef6\u65f6", None))
        self.JointDelayTimeSubButton.setProperty("lightCustomQss", QCoreApplication.translate("Frame", u"ToolButton {\n"
"    background: rgb(125, 214, 249);\n"
"}\n"
"\n"
"ToolButton:hover {\n"
"    background: rgb(125, 214, 249);\n"
"}", None))
        self.JointDelayTimeEdit.setText(QCoreApplication.translate("Frame", u"1", None))
        self.JointDelayTimeAddButton.setProperty("lightCustomQss", QCoreApplication.translate("Frame", u"ToolButton {\n"
"    background: rgb(125, 214, 249);\n"
"}\n"
"\n"
"ToolButton:hover {\n"
"    background: rgb(125, 214, 249);\n"
"}", None))
        self.XLable.setText(QCoreApplication.translate("Frame", u"X", None))
        self.XLable.setProperty("lightCustomQss", QCoreApplication.translate("Frame", u"PushButton {     background: rgb(0, 170, 255); }  PushButton:hover {     background: rgb(0, 170, 255); }", None))
        self.XAxisSubButton.setProperty("lightCustomQss", QCoreApplication.translate("Frame", u"ToolButton {\n"
"    background: rgb(125, 214, 249);\n"
"}\n"
"\n"
"ToolButton:hover {\n"
"    background: rgb(125, 214, 249);\n"
"}", None))
        self.XAxisAddButton.setProperty("lightCustomQss", QCoreApplication.translate("Frame", u"ToolButton {\n"
"    background: rgb(125, 214, 249);\n"
"}\n"
"\n"
"ToolButton:hover {\n"
"    background: rgb(125, 214, 249);\n"
"}", None))
        self.YLable.setText(QCoreApplication.translate("Frame", u"Y", None))
        self.YAxisSubButton.setProperty("lightCustomQss", QCoreApplication.translate("Frame", u"ToolButton {\n"
"    background: rgb(125, 214, 249);\n"
"}\n"
"\n"
"ToolButton:hover {\n"
"    background: rgb(125, 214, 249);\n"
"}", None))
        self.YAxisAddButton.setProperty("lightCustomQss", QCoreApplication.translate("Frame", u"ToolButton {\n"
"    background: rgb(125, 214, 249);\n"
"}\n"
"\n"
"ToolButton:hover {\n"
"    background: rgb(125, 214, 249);\n"
"}", None))
        self.Zlable.setText(QCoreApplication.translate("Frame", u"Z", None))
        self.ZAxisSubButton.setProperty("lightCustomQss", QCoreApplication.translate("Frame", u"ToolButton {\n"
"    background: rgb(125, 214, 249);\n"
"}\n"
"\n"
"ToolButton:hover {\n"
"    background: rgb(125, 214, 249);\n"
"}", None))
        self.ZAxisAddButton.setProperty("lightCustomQss", QCoreApplication.translate("Frame", u"ToolButton {\n"
"    background: rgb(125, 214, 249);\n"
"}\n"
"\n"
"ToolButton:hover {\n"
"    background: rgb(125, 214, 249);\n"
"}", None))
        self.CoordinateStepLable.setText(QCoreApplication.translate("Frame", u"\u6b65\u957f", None))
        self.CoordinateStepSubButton.setProperty("lightCustomQss", QCoreApplication.translate("Frame", u"ToolButton {\n"
"    background: rgb(125, 214, 249);\n"
"}\n"
"\n"
"ToolButton:hover {\n"
"    background: rgb(125, 214, 249);\n"
"}", None))
        self.CoordinateStepEdit.setText(QCoreApplication.translate("Frame", u"0.01", None))
        self.CoordinateAddButton.setProperty("lightCustomQss", QCoreApplication.translate("Frame", u"ToolButton {\n"
"    background: rgb(125, 214, 249);\n"
"}\n"
"\n"
"ToolButton:hover {\n"
"    background: rgb(125, 214, 249);\n"
"}", None))
        self.RxLabel.setText(QCoreApplication.translate("Frame", u"Rx", None))
        self.RxAxisSubButton.setProperty("lightCustomQss", QCoreApplication.translate("Frame", u"ToolButton {\n"
"    background: rgb(125, 214, 249);\n"
"}\n"
"\n"
"ToolButton:hover {\n"
"    background: rgb(125, 214, 249);\n"
"}", None))
        self.RxAxisAddButton.setProperty("lightCustomQss", QCoreApplication.translate("Frame", u"ToolButton {\n"
"    background: rgb(125, 214, 249);\n"
"}\n"
"\n"
"ToolButton:hover {\n"
"    background: rgb(125, 214, 249);\n"
"}", None))
        self.RyLabel.setText(QCoreApplication.translate("Frame", u"Ry", None))
        self.RyAxisSubButton.setProperty("lightCustomQss", QCoreApplication.translate("Frame", u"ToolButton {\n"
"    background: rgb(125, 214, 249);\n"
"}\n"
"\n"
"ToolButton:hover {\n"
"    background: rgb(125, 214, 249);\n"
"}", None))
        self.RyAxisAddButton.setProperty("lightCustomQss", QCoreApplication.translate("Frame", u"ToolButton {\n"
"    background: rgb(125, 214, 249);\n"
"}\n"
"\n"
"ToolButton:hover {\n"
"    background: rgb(125, 214, 249);\n"
"}", None))
        self.RzLabel.setText(QCoreApplication.translate("Frame", u"Rz", None))
        self.RzAxisSubButton.setProperty("lightCustomQss", QCoreApplication.translate("Frame", u"ToolButton {\n"
"    background: rgb(125, 214, 249);\n"
"}\n"
"\n"
"ToolButton:hover {\n"
"    background: rgb(125, 214, 249);\n"
"}", None))
        self.RzAxisAddButton.setProperty("lightCustomQss", QCoreApplication.translate("Frame", u"ToolButton {\n"
"    background: rgb(125, 214, 249);\n"
"}\n"
"\n"
"ToolButton:hover {\n"
"    background: rgb(125, 214, 249);\n"
"}", None))
        self.ApStepLabel.setText(QCoreApplication.translate("Frame", u"\u6b65\u957f", None))
        self.ApStepSubButton.setProperty("lightCustomQss", QCoreApplication.translate("Frame", u"ToolButton {\n"
"    background: rgb(125, 214, 249);\n"
"}\n"
"\n"
"ToolButton:hover {\n"
"    background: rgb(125, 214, 249);\n"
"}", None))
        self.ApStepEdit.setText(QCoreApplication.translate("Frame", u"10", None))
        self.ApStepAddButton.setProperty("lightCustomQss", QCoreApplication.translate("Frame", u"ToolButton {\n"
"    background: rgb(125, 214, 249);\n"
"}\n"
"\n"
"ToolButton:hover {\n"
"    background: rgb(125, 214, 249);\n"
"}", None))
        self.ArmToolLabel.setText(QCoreApplication.translate("Frame", u"\u5de5\u5177", None))
        self.ArmControlLabel.setText(QCoreApplication.translate("Frame", u"\u63a7\u5236", None))
        self.ArmClawOpenButton.setText(QCoreApplication.translate("Frame", u"\u5f00", None))
        self.ArmClawOpenButton.setProperty("lightCustomQss", QCoreApplication.translate("Frame", u"PushButton {\n"
"    background: rgb(125, 214, 249);\n"
"}\n"
"PushButton:hover {\n"
"    background: rgb(125, 214, 249);\n"
"}", None))
        self.ArmClawCloseButton.setText(QCoreApplication.translate("Frame", u"\u5173", None))
        self.ArmClawCloseButton.setProperty("lightCustomQss", QCoreApplication.translate("Frame", u"PushButton {\n"
"    background: rgb(229, 142, 138);\n"
"}\n"
"PushButton:hover {\n"
"    background: rgb(229, 142, 138);\n"
"}", None))
        self.RobotArmResetButton.setText(QCoreApplication.translate("Frame", u"\u590d\u4f4d", None))
        self.RobotArmResetButton.setProperty("lightCustomQss", QCoreApplication.translate("Frame", u"PushButton {\n"
"    background: rgb(240, 203, 98);\n"
"}\n"
"\n"
"PushButton:hover {\n"
"    background: rgb(240, 203, 98);\n"
"}", None))
        self.RobotArmZeroButton.setText(QCoreApplication.translate("Frame", u"\u5f52\u96f6", None))
        self.RobotArmZeroButton.setProperty("lightCustomQss", QCoreApplication.translate("Frame", u"PushButton {\n"
"    background: rgb(170, 211, 140);\n"
"}\n"
"\n"
"PushButton:hover {\n"
"    background: rgb(170, 211, 140);\n"
"}", None))
        self.RobotArmStopButton.setText(QCoreApplication.translate("Frame", u"\u6025\u505c", None))
        self.RobotArmStopButton.setProperty("lightCustomQss", QCoreApplication.translate("Frame", u"PushButton {\n"
"    background: rgb(229, 142, 138);\n"
"}\n"
"\n"
"PushButton:hover {\n"
"    background: rgb(229, 142, 138);\n"
"}", None))
    # retranslateUi

