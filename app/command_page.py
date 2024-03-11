# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'command_page.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QSizePolicy,
    QVBoxLayout, QWidget)

from qfluentwidgets import (PlainTextEdit, PushButton, StrongBodyLabel)

class command_page_frame(object):
    def setupUi(self, Frame):
        if not Frame.objectName():
            Frame.setObjectName(u"Frame")
        Frame.resize(1120, 650)
        self.horizontalLayout_3 = QHBoxLayout(Frame)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.SendLabel = StrongBodyLabel(Frame)
        self.SendLabel.setObjectName(u"SendLabel")

        self.verticalLayout.addWidget(self.SendLabel)

        self.CommandSendWindow = PlainTextEdit(Frame)
        self.CommandSendWindow.setObjectName(u"CommandSendWindow")

        self.verticalLayout.addWidget(self.CommandSendWindow)

        self.ResponseLabel = StrongBodyLabel(Frame)
        self.ResponseLabel.setObjectName(u"ResponseLabel")

        self.verticalLayout.addWidget(self.ResponseLabel)

        self.CommandResWindow = PlainTextEdit(Frame)
        self.CommandResWindow.setObjectName(u"CommandResWindow")

        self.verticalLayout.addWidget(self.CommandResWindow)


        self.horizontalLayout_2.addLayout(self.verticalLayout)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.CommandArmRunLogLabel = StrongBodyLabel(Frame)
        self.CommandArmRunLogLabel.setObjectName(u"CommandArmRunLogLabel")

        self.verticalLayout_2.addWidget(self.CommandArmRunLogLabel)

        self.CommandEditWindow = PlainTextEdit(Frame)
        self.CommandEditWindow.setObjectName(u"CommandEditWindow")

        self.verticalLayout_2.addWidget(self.CommandEditWindow)


        self.horizontalLayout.addLayout(self.verticalLayout_2)

        self.CommandSendButton = PushButton(Frame)
        self.CommandSendButton.setObjectName(u"CommandSendButton")

        self.horizontalLayout.addWidget(self.CommandSendButton)


        self.horizontalLayout_2.addLayout(self.horizontalLayout)


        self.horizontalLayout_3.addLayout(self.horizontalLayout_2)


        self.retranslateUi(Frame)

        QMetaObject.connectSlotsByName(Frame)
    # setupUi

    def retranslateUi(self, Frame):
        Frame.setWindowTitle(QCoreApplication.translate("Frame", u"Frame", None))
        self.SendLabel.setText(QCoreApplication.translate("Frame", u"\u547d\u4ee4\u53d1\u9001", None))
        self.ResponseLabel.setText(QCoreApplication.translate("Frame", u"\u547d\u4ee4\u63a5\u6536", None))
        self.CommandArmRunLogLabel.setText(QCoreApplication.translate("Frame", u"\u547d\u4ee4\u7f16\u8f91\u7a97\u53e3", None))
        self.CommandSendButton.setText(QCoreApplication.translate("Frame", u"\u53d1\u9001", None))
    # retranslateUi

