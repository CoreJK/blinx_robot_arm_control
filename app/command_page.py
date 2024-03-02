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
        Frame.resize(900, 678)
        self.widget = QWidget(Frame)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(50, 10, 811, 646))
        self.verticalLayout_2 = QVBoxLayout(self.widget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.StrongBodyLabel = StrongBodyLabel(self.widget)
        self.StrongBodyLabel.setObjectName(u"StrongBodyLabel")

        self.verticalLayout.addWidget(self.StrongBodyLabel)

        self.PlainTextEdit = PlainTextEdit(self.widget)
        self.PlainTextEdit.setObjectName(u"PlainTextEdit")

        self.verticalLayout.addWidget(self.PlainTextEdit)

        self.StrongBodyLabel_2 = StrongBodyLabel(self.widget)
        self.StrongBodyLabel_2.setObjectName(u"StrongBodyLabel_2")

        self.verticalLayout.addWidget(self.StrongBodyLabel_2)

        self.PlainTextEdit_2 = PlainTextEdit(self.widget)
        self.PlainTextEdit_2.setObjectName(u"PlainTextEdit_2")

        self.verticalLayout.addWidget(self.PlainTextEdit_2)


        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.PlainTextEdit_3 = PlainTextEdit(self.widget)
        self.PlainTextEdit_3.setObjectName(u"PlainTextEdit_3")

        self.horizontalLayout.addWidget(self.PlainTextEdit_3)

        self.PushButton = PushButton(self.widget)
        self.PushButton.setObjectName(u"PushButton")

        self.horizontalLayout.addWidget(self.PushButton)


        self.verticalLayout_2.addLayout(self.horizontalLayout)


        self.retranslateUi(Frame)

        QMetaObject.connectSlotsByName(Frame)
    # setupUi

    def retranslateUi(self, Frame):
        Frame.setWindowTitle(QCoreApplication.translate("Frame", u"Frame", None))
        self.StrongBodyLabel.setText(QCoreApplication.translate("Frame", u"\u547d\u4ee4\u53d1\u9001", None))
        self.StrongBodyLabel_2.setText(QCoreApplication.translate("Frame", u"\u547d\u4ee4\u53d1\u9001", None))
        self.PushButton.setText("")
    # retranslateUi

