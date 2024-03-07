# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'connect_page.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QSizePolicy, QVBoxLayout, QWidget)

from qfluentwidgets import (CardWidget, ComboBox, HeaderCardWidget, LineEdit,
    PasswordLineEdit, PushButton, SimpleCardWidget, StrongBodyLabel)

class connect_page_frame(object):
    def setupUi(self, Frame):
        if not Frame.objectName():
            Frame.setObjectName(u"Frame")
        Frame.resize(987, 728)
        self.horizontalLayout_4 = QHBoxLayout(Frame)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.HeaderCardWidget = HeaderCardWidget(Frame)
        self.HeaderCardWidget.setObjectName(u"HeaderCardWidget")
        self.layoutWidget = QWidget(self.HeaderCardWidget)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(440, 61, 271, 121))
        self.verticalLayout = QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.TargetPortLabel = StrongBodyLabel(self.layoutWidget)
        self.TargetPortLabel.setObjectName(u"TargetPortLabel")

        self.gridLayout.addWidget(self.TargetPortLabel, 1, 0, 1, 1)

        self.TargetIpEdit = LineEdit(self.layoutWidget)
        self.TargetIpEdit.setObjectName(u"TargetIpEdit")

        self.gridLayout.addWidget(self.TargetIpEdit, 0, 1, 1, 1)

        self.TargetIpLabel = StrongBodyLabel(self.layoutWidget)
        self.TargetIpLabel.setObjectName(u"TargetIpLabel")

        self.gridLayout.addWidget(self.TargetIpLabel, 0, 0, 1, 1)

        self.TargetPortEdit = LineEdit(self.layoutWidget)
        self.TargetPortEdit.setObjectName(u"TargetPortEdit")

        self.gridLayout.addWidget(self.TargetPortEdit, 1, 1, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.IpPortInfoRestButton = PushButton(self.layoutWidget)
        self.IpPortInfoRestButton.setObjectName(u"IpPortInfoRestButton")
        self.IpPortInfoRestButton.setProperty("hasIcon", False)

        self.horizontalLayout.addWidget(self.IpPortInfoRestButton)

        self.IpPortInfoSubmitButton = PushButton(self.layoutWidget)
        self.IpPortInfoSubmitButton.setObjectName(u"IpPortInfoSubmitButton")
        self.IpPortInfoSubmitButton.setProperty("hasIcon", False)

        self.horizontalLayout.addWidget(self.IpPortInfoSubmitButton)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.RobotArmLinkButton = PushButton(self.HeaderCardWidget)
        self.RobotArmLinkButton.setObjectName(u"RobotArmLinkButton")
        self.RobotArmLinkButton.setGeometry(QRect(520, 190, 110, 31))
        self.RobotArmLinkButton.setMaximumSize(QSize(200, 16777215))
        self.RobotArmLinkButton.setLayoutDirection(Qt.LeftToRight)
        self.RobotArmLinkButton.setProperty("hasIcon", False)

        self.verticalLayout_4.addWidget(self.HeaderCardWidget)

        self.HeaderCardWidget_2 = HeaderCardWidget(Frame)
        self.HeaderCardWidget_2.setObjectName(u"HeaderCardWidget_2")
        self.layoutWidget1 = QWidget(self.HeaderCardWidget_2)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(440, 60, 281, 117))
        self.verticalLayout_2 = QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.WiFiPasswdLabel = StrongBodyLabel(self.layoutWidget1)
        self.WiFiPasswdLabel.setObjectName(u"WiFiPasswdLabel")

        self.gridLayout_2.addWidget(self.WiFiPasswdLabel, 1, 0, 1, 1)

        self.WiFiSsidEdit = LineEdit(self.layoutWidget1)
        self.WiFiSsidEdit.setObjectName(u"WiFiSsidEdit")

        self.gridLayout_2.addWidget(self.WiFiSsidEdit, 0, 1, 1, 1)

        self.WiFiSsidLabel = StrongBodyLabel(self.layoutWidget1)
        self.WiFiSsidLabel.setObjectName(u"WiFiSsidLabel")

        self.gridLayout_2.addWidget(self.WiFiSsidLabel, 0, 0, 1, 1)

        self.WiFiPasswordLineEdit = PasswordLineEdit(self.layoutWidget1)
        self.WiFiPasswordLineEdit.setObjectName(u"WiFiPasswordLineEdit")

        self.gridLayout_2.addWidget(self.WiFiPasswordLineEdit, 1, 1, 1, 1)


        self.verticalLayout_2.addLayout(self.gridLayout_2)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.WiFiInfoReset = PushButton(self.layoutWidget1)
        self.WiFiInfoReset.setObjectName(u"WiFiInfoReset")

        self.horizontalLayout_2.addWidget(self.WiFiInfoReset)

        self.WiFiInfoSubmit = PushButton(self.layoutWidget1)
        self.WiFiInfoSubmit.setObjectName(u"WiFiInfoSubmit")

        self.horizontalLayout_2.addWidget(self.WiFiInfoSubmit)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)


        self.verticalLayout_4.addWidget(self.HeaderCardWidget_2)

        self.HeaderCardWidget_3 = HeaderCardWidget(Frame)
        self.HeaderCardWidget_3.setObjectName(u"HeaderCardWidget_3")
        self.layoutWidget_2 = QWidget(self.HeaderCardWidget_3)
        self.layoutWidget_2.setObjectName(u"layoutWidget_2")
        self.layoutWidget_2.setGeometry(QRect(440, 60, 281, 121))
        self.verticalLayout_3 = QVBoxLayout(self.layoutWidget_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.BaudRatesLabel = StrongBodyLabel(self.layoutWidget_2)
        self.BaudRatesLabel.setObjectName(u"BaudRatesLabel")

        self.gridLayout_3.addWidget(self.BaudRatesLabel, 1, 0, 1, 1)

        self.SerialNumLabel = StrongBodyLabel(self.layoutWidget_2)
        self.SerialNumLabel.setObjectName(u"SerialNumLabel")

        self.gridLayout_3.addWidget(self.SerialNumLabel, 0, 0, 1, 1)

        self.SerialNumComboBox = ComboBox(self.layoutWidget_2)
        self.SerialNumComboBox.setObjectName(u"SerialNumComboBox")

        self.gridLayout_3.addWidget(self.SerialNumComboBox, 0, 1, 1, 1)

        self.BaudRatesComboBox = ComboBox(self.layoutWidget_2)
        self.BaudRatesComboBox.setObjectName(u"BaudRatesComboBox")
        self.BaudRatesComboBox.setFlat(False)

        self.gridLayout_3.addWidget(self.BaudRatesComboBox, 1, 1, 1, 1)


        self.verticalLayout_3.addLayout(self.gridLayout_3)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.SbInfoFreshButton = PushButton(self.layoutWidget_2)
        self.SbInfoFreshButton.setObjectName(u"SbInfoFreshButton")

        self.horizontalLayout_3.addWidget(self.SbInfoFreshButton)

        self.SbInfoSubmitButton = PushButton(self.layoutWidget_2)
        self.SbInfoSubmitButton.setObjectName(u"SbInfoSubmitButton")

        self.horizontalLayout_3.addWidget(self.SbInfoSubmitButton)


        self.verticalLayout_3.addLayout(self.horizontalLayout_3)


        self.verticalLayout_4.addWidget(self.HeaderCardWidget_3)


        self.horizontalLayout_4.addLayout(self.verticalLayout_4)


        self.retranslateUi(Frame)

        self.BaudRatesComboBox.setDefault(False)


        QMetaObject.connectSlotsByName(Frame)
    # setupUi

    def retranslateUi(self, Frame):
        Frame.setWindowTitle(QCoreApplication.translate("Frame", u"Frame", None))
        self.HeaderCardWidget.setTitle(QCoreApplication.translate("Frame", u"\u673a\u68b0\u81c2\u8fde\u63a5\u914d\u7f6e", None))
        self.TargetPortLabel.setText(QCoreApplication.translate("Frame", u"\u7aef\u53e3\u53f7", None))
        self.TargetIpLabel.setText(QCoreApplication.translate("Frame", u"\u76ee\u6807 IP", None))
        self.IpPortInfoRestButton.setText(QCoreApplication.translate("Frame", u"\u91cd\u7f6e", None))
        self.IpPortInfoSubmitButton.setText(QCoreApplication.translate("Frame", u"\u786e\u5b9a", None))
        self.RobotArmLinkButton.setText(QCoreApplication.translate("Frame", u"\u8fde\u63a5\u673a\u68b0\u81c2", None))
        self.HeaderCardWidget_2.setTitle(QCoreApplication.translate("Frame", u"\u673a\u68b0\u81c2 WiFi \u6a21\u5f0f\u914d\u7f6e", None))
        self.WiFiPasswdLabel.setText(QCoreApplication.translate("Frame", u"WiFi \u5bc6\u7801", None))
        self.WiFiSsidLabel.setText(QCoreApplication.translate("Frame", u"WiFi SSID", None))
        self.WiFiInfoReset.setText(QCoreApplication.translate("Frame", u"\u91cd\u7f6e", None))
        self.WiFiInfoSubmit.setText(QCoreApplication.translate("Frame", u"\u786e\u5b9a", None))
        self.HeaderCardWidget_3.setTitle(QCoreApplication.translate("Frame", u"\u673a\u68b0\u81c2\u4e32\u53e3\u8fde\u63a5\u914d\u7f6e", None))
        self.BaudRatesLabel.setText(QCoreApplication.translate("Frame", u"\u6ce2\u7279\u7387", None))
        self.SerialNumLabel.setText(QCoreApplication.translate("Frame", u"COM \u53e3", None))
        self.BaudRatesComboBox.setText(QCoreApplication.translate("Frame", u"115200", None))
        self.SbInfoFreshButton.setText(QCoreApplication.translate("Frame", u"\u5237\u65b0", None))
        self.SbInfoSubmitButton.setText(QCoreApplication.translate("Frame", u"\u786e\u5b9a", None))
    # retranslateUi

