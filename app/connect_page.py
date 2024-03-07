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
        self.widget = QWidget(self.HeaderCardWidget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(440, 61, 271, 121))
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.StrongBodyLabel_2 = StrongBodyLabel(self.widget)
        self.StrongBodyLabel_2.setObjectName(u"StrongBodyLabel_2")

        self.gridLayout.addWidget(self.StrongBodyLabel_2, 1, 0, 1, 1)

        self.LineEdit = LineEdit(self.widget)
        self.LineEdit.setObjectName(u"LineEdit")

        self.gridLayout.addWidget(self.LineEdit, 0, 1, 1, 1)

        self.StrongBodyLabel = StrongBodyLabel(self.widget)
        self.StrongBodyLabel.setObjectName(u"StrongBodyLabel")

        self.gridLayout.addWidget(self.StrongBodyLabel, 0, 0, 1, 1)

        self.LineEdit_2 = LineEdit(self.widget)
        self.LineEdit_2.setObjectName(u"LineEdit_2")

        self.gridLayout.addWidget(self.LineEdit_2, 1, 1, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.PushButton_4 = PushButton(self.widget)
        self.PushButton_4.setObjectName(u"PushButton_4")
        self.PushButton_4.setProperty("hasIcon", False)

        self.horizontalLayout.addWidget(self.PushButton_4)

        self.PushButton_2 = PushButton(self.widget)
        self.PushButton_2.setObjectName(u"PushButton_2")
        self.PushButton_2.setProperty("hasIcon", False)

        self.horizontalLayout.addWidget(self.PushButton_2)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.PushButton = PushButton(self.HeaderCardWidget)
        self.PushButton.setObjectName(u"PushButton")
        self.PushButton.setGeometry(QRect(520, 190, 110, 31))
        self.PushButton.setMaximumSize(QSize(200, 16777215))
        self.PushButton.setLayoutDirection(Qt.LeftToRight)
        self.PushButton.setProperty("hasIcon", False)

        self.verticalLayout_4.addWidget(self.HeaderCardWidget)

        self.HeaderCardWidget_2 = HeaderCardWidget(Frame)
        self.HeaderCardWidget_2.setObjectName(u"HeaderCardWidget_2")
        self.layoutWidget = QWidget(self.HeaderCardWidget_2)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(440, 60, 281, 117))
        self.verticalLayout_2 = QVBoxLayout(self.layoutWidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.StrongBodyLabel_3 = StrongBodyLabel(self.layoutWidget)
        self.StrongBodyLabel_3.setObjectName(u"StrongBodyLabel_3")

        self.gridLayout_2.addWidget(self.StrongBodyLabel_3, 1, 0, 1, 1)

        self.LineEdit_3 = LineEdit(self.layoutWidget)
        self.LineEdit_3.setObjectName(u"LineEdit_3")

        self.gridLayout_2.addWidget(self.LineEdit_3, 0, 1, 1, 1)

        self.StrongBodyLabel_4 = StrongBodyLabel(self.layoutWidget)
        self.StrongBodyLabel_4.setObjectName(u"StrongBodyLabel_4")

        self.gridLayout_2.addWidget(self.StrongBodyLabel_4, 0, 0, 1, 1)

        self.PasswordLineEdit = PasswordLineEdit(self.layoutWidget)
        self.PasswordLineEdit.setObjectName(u"PasswordLineEdit")

        self.gridLayout_2.addWidget(self.PasswordLineEdit, 1, 1, 1, 1)


        self.verticalLayout_2.addLayout(self.gridLayout_2)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.PushButton_5 = PushButton(self.layoutWidget)
        self.PushButton_5.setObjectName(u"PushButton_5")

        self.horizontalLayout_2.addWidget(self.PushButton_5)

        self.PushButton_3 = PushButton(self.layoutWidget)
        self.PushButton_3.setObjectName(u"PushButton_3")

        self.horizontalLayout_2.addWidget(self.PushButton_3)


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
        self.StrongBodyLabel_5 = StrongBodyLabel(self.layoutWidget_2)
        self.StrongBodyLabel_5.setObjectName(u"StrongBodyLabel_5")

        self.gridLayout_3.addWidget(self.StrongBodyLabel_5, 1, 0, 1, 1)

        self.StrongBodyLabel_6 = StrongBodyLabel(self.layoutWidget_2)
        self.StrongBodyLabel_6.setObjectName(u"StrongBodyLabel_6")

        self.gridLayout_3.addWidget(self.StrongBodyLabel_6, 0, 0, 1, 1)

        self.ComboBox = ComboBox(self.layoutWidget_2)
        self.ComboBox.setObjectName(u"ComboBox")

        self.gridLayout_3.addWidget(self.ComboBox, 0, 1, 1, 1)

        self.ComboBox_2 = ComboBox(self.layoutWidget_2)
        self.ComboBox_2.setObjectName(u"ComboBox_2")
        self.ComboBox_2.setFlat(False)

        self.gridLayout_3.addWidget(self.ComboBox_2, 1, 1, 1, 1)


        self.verticalLayout_3.addLayout(self.gridLayout_3)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.PushButton_6 = PushButton(self.layoutWidget_2)
        self.PushButton_6.setObjectName(u"PushButton_6")

        self.horizontalLayout_3.addWidget(self.PushButton_6)

        self.PushButton_7 = PushButton(self.layoutWidget_2)
        self.PushButton_7.setObjectName(u"PushButton_7")

        self.horizontalLayout_3.addWidget(self.PushButton_7)


        self.verticalLayout_3.addLayout(self.horizontalLayout_3)


        self.verticalLayout_4.addWidget(self.HeaderCardWidget_3)


        self.horizontalLayout_4.addLayout(self.verticalLayout_4)


        self.retranslateUi(Frame)

        self.ComboBox_2.setDefault(False)


        QMetaObject.connectSlotsByName(Frame)
    # setupUi

    def retranslateUi(self, Frame):
        Frame.setWindowTitle(QCoreApplication.translate("Frame", u"Frame", None))
        self.HeaderCardWidget.setTitle(QCoreApplication.translate("Frame", u"\u673a\u68b0\u81c2\u8fde\u63a5\u914d\u7f6e", None))
        self.StrongBodyLabel_2.setText(QCoreApplication.translate("Frame", u"\u7aef\u53e3\u53f7", None))
        self.StrongBodyLabel.setText(QCoreApplication.translate("Frame", u"\u76ee\u6807 IP", None))
        self.PushButton_4.setText(QCoreApplication.translate("Frame", u"\u91cd\u7f6e", None))
        self.PushButton_2.setText(QCoreApplication.translate("Frame", u"\u786e\u5b9a", None))
        self.PushButton.setText(QCoreApplication.translate("Frame", u"\u8fde\u63a5\u673a\u68b0\u81c2", None))
        self.HeaderCardWidget_2.setTitle(QCoreApplication.translate("Frame", u"\u673a\u68b0\u81c2 WiFi \u6a21\u5f0f\u914d\u7f6e", None))
        self.StrongBodyLabel_3.setText(QCoreApplication.translate("Frame", u"WiFi \u5bc6\u7801", None))
        self.StrongBodyLabel_4.setText(QCoreApplication.translate("Frame", u"WiFi SSID", None))
        self.PushButton_5.setText(QCoreApplication.translate("Frame", u"\u91cd\u7f6e", None))
        self.PushButton_3.setText(QCoreApplication.translate("Frame", u"\u786e\u5b9a", None))
        self.HeaderCardWidget_3.setTitle(QCoreApplication.translate("Frame", u"\u673a\u68b0\u81c2\u4e32\u53e3\u8fde\u63a5\u914d\u7f6e", None))
        self.StrongBodyLabel_5.setText(QCoreApplication.translate("Frame", u"\u6ce2\u7279\u7387", None))
        self.StrongBodyLabel_6.setText(QCoreApplication.translate("Frame", u"COM \u53e3", None))
        self.ComboBox_2.setText(QCoreApplication.translate("Frame", u"115200", None))
        self.PushButton_6.setText(QCoreApplication.translate("Frame", u"\u5237\u65b0", None))
        self.PushButton_7.setText(QCoreApplication.translate("Frame", u"\u786e\u5b9a", None))
    # retranslateUi

