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
    QSizePolicy, QTableWidgetItem, QVBoxLayout, QWidget)

from qfluentwidgets import (LineEdit, PillPushButton, PushButton, RadioButton,
    TableWidget, ToggleButton)

class teach_page_frame(object):
    def setupUi(self, Frame):
        if not Frame.objectName():
            Frame.setObjectName(u"Frame")
        Frame.resize(1078, 570)
        self.widget = QWidget(Frame)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(10, 20, 931, 541))
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.PillPushButton_2 = PillPushButton(self.widget)
        self.PillPushButton_2.setObjectName(u"PillPushButton_2")

        self.horizontalLayout.addWidget(self.PillPushButton_2)

        self.PillPushButton_3 = PillPushButton(self.widget)
        self.PillPushButton_3.setObjectName(u"PillPushButton_3")

        self.horizontalLayout.addWidget(self.PillPushButton_3)

        self.RadioButton = RadioButton(self.widget)
        self.RadioButton.setObjectName(u"RadioButton")

        self.horizontalLayout.addWidget(self.RadioButton)

        self.RadioButton_2 = RadioButton(self.widget)
        self.RadioButton_2.setObjectName(u"RadioButton_2")

        self.horizontalLayout.addWidget(self.RadioButton_2)

        self.PillPushButton_4 = PillPushButton(self.widget)
        self.PillPushButton_4.setObjectName(u"PillPushButton_4")

        self.horizontalLayout.addWidget(self.PillPushButton_4)

        self.PillPushButton_5 = PillPushButton(self.widget)
        self.PillPushButton_5.setObjectName(u"PillPushButton_5")

        self.horizontalLayout.addWidget(self.PillPushButton_5)

        self.PillPushButton_6 = PillPushButton(self.widget)
        self.PillPushButton_6.setObjectName(u"PillPushButton_6")

        self.horizontalLayout.addWidget(self.PillPushButton_6)

        self.LineEdit = LineEdit(self.widget)
        self.LineEdit.setObjectName(u"LineEdit")

        self.horizontalLayout.addWidget(self.LineEdit)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.TableWidget = TableWidget(self.widget)
        if (self.TableWidget.columnCount() < 10):
            self.TableWidget.setColumnCount(10)
        __qtablewidgetitem = QTableWidgetItem()
        self.TableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.TableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.TableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.TableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.TableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.TableWidget.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.TableWidget.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.TableWidget.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.TableWidget.setHorizontalHeaderItem(8, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.TableWidget.setHorizontalHeaderItem(9, __qtablewidgetitem9)
        self.TableWidget.setObjectName(u"TableWidget")

        self.verticalLayout.addWidget(self.TableWidget)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.PillPushButton_7 = PillPushButton(self.widget)
        self.PillPushButton_7.setObjectName(u"PillPushButton_7")

        self.horizontalLayout_2.addWidget(self.PillPushButton_7)

        self.PillPushButton_8 = PillPushButton(self.widget)
        self.PillPushButton_8.setObjectName(u"PillPushButton_8")

        self.horizontalLayout_2.addWidget(self.PillPushButton_8)

        self.PillPushButton_9 = PillPushButton(self.widget)
        self.PillPushButton_9.setObjectName(u"PillPushButton_9")

        self.horizontalLayout_2.addWidget(self.PillPushButton_9)

        self.PillPushButton_10 = PillPushButton(self.widget)
        self.PillPushButton_10.setObjectName(u"PillPushButton_10")

        self.horizontalLayout_2.addWidget(self.PillPushButton_10)


        self.verticalLayout.addLayout(self.horizontalLayout_2)


        self.retranslateUi(Frame)

        QMetaObject.connectSlotsByName(Frame)
    # setupUi

    def retranslateUi(self, Frame):
        Frame.setWindowTitle(QCoreApplication.translate("Frame", u"Frame", None))
        self.PillPushButton_2.setText(QCoreApplication.translate("Frame", u"\u5bfc\u5165\u52a8\u4f5c", None))
        self.PillPushButton_3.setText(QCoreApplication.translate("Frame", u"\u5bfc\u51fa\u52a8\u4f5c", None))
        self.RadioButton.setText("")
        self.RadioButton_2.setText("")
        self.PillPushButton_4.setText(QCoreApplication.translate("Frame", u"\u987a\u5e8f\u6267\u884c", None))
        self.PillPushButton_5.setText(QCoreApplication.translate("Frame", u"\u5355\u6b21\u6267\u884c", None))
        self.PillPushButton_6.setText(QCoreApplication.translate("Frame", u"\u5faa\u73af\u6267\u884c", None))
        self.LineEdit.setText(QCoreApplication.translate("Frame", u"1~100", None))
        ___qtablewidgetitem = self.TableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Frame", u"J1", None));
        ___qtablewidgetitem1 = self.TableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Frame", u"J2", None));
        ___qtablewidgetitem2 = self.TableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Frame", u"J3", None));
        ___qtablewidgetitem3 = self.TableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Frame", u"J4", None));
        ___qtablewidgetitem4 = self.TableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Frame", u"\u901f\u5ea6", None));
        ___qtablewidgetitem5 = self.TableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("Frame", u"\u5de5\u5177", None));
        ___qtablewidgetitem6 = self.TableWidget.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("Frame", u"\u5f00\u5173", None));
        ___qtablewidgetitem7 = self.TableWidget.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("Frame", u"\u5ef6\u65f6", None));
        ___qtablewidgetitem8 = self.TableWidget.horizontalHeaderItem(8)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("Frame", u"\u5907\u6ce8", None));
        self.PillPushButton_7.setText(QCoreApplication.translate("Frame", u"\u5220\u9664\u52a8\u4f5c", None))
        self.PillPushButton_8.setText(QCoreApplication.translate("Frame", u"\u6dfb\u52a0\u52a8\u4f5c", None))
        self.PillPushButton_9.setText(QCoreApplication.translate("Frame", u"\u66f4\u65b0\u884c", None))
        self.PillPushButton_10.setText(QCoreApplication.translate("Frame", u"\u66f4\u65b0\u5217", None))
    # retranslateUi

