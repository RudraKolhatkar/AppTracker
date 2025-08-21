# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Dashboard.ui'
##
## Created by: Qt User Interface Compiler version 6.9.1
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QFrame, QHBoxLayout,
    QHeaderView, QPushButton, QSizePolicy, QSpacerItem,
    QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(855, 591)
        Form.setStyleSheet(u"background-color: rgb(47, 46, 52);\n"
"color:white;")
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.TimeFrame = QFrame(Form)
        self.TimeFrame.setObjectName(u"TimeFrame")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.TimeFrame.sizePolicy().hasHeightForWidth())
        self.TimeFrame.setSizePolicy(sizePolicy)
        self.TimeFrame.setBaseSize(QSize(0, 20))
        self.TimeFrame.setStyleSheet(u"    QFrame#frame_2 {\n"
"        border: 0px;\n"
"    }")
        self.TimeFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.TimeFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.TimeFrame)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.addButton = QPushButton(self.TimeFrame)
        self.addButton.setObjectName(u"addButton")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.addButton.sizePolicy().hasHeightForWidth())
        self.addButton.setSizePolicy(sizePolicy1)
        self.addButton.setMaximumSize(QSize(30, 16777215))
        self.addButton.setStyleSheet(u"color: white")

        self.horizontalLayout.addWidget(self.addButton)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_3)

        self.yearButt = QPushButton(self.TimeFrame)
        self.yearButt.setObjectName(u"yearButt")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.yearButt.sizePolicy().hasHeightForWidth())
        self.yearButt.setSizePolicy(sizePolicy2)
        self.yearButt.setStyleSheet(u"color: white")
        self.yearButt.setCheckable(False)

        self.horizontalLayout.addWidget(self.yearButt)

        self.monthButt = QPushButton(self.TimeFrame)
        self.monthButt.setObjectName(u"monthButt")
        sizePolicy2.setHeightForWidth(self.monthButt.sizePolicy().hasHeightForWidth())
        self.monthButt.setSizePolicy(sizePolicy2)
        self.monthButt.setStyleSheet(u"color: white")
        self.monthButt.setCheckable(False)

        self.horizontalLayout.addWidget(self.monthButt)

        self.weekButt = QPushButton(self.TimeFrame)
        self.weekButt.setObjectName(u"weekButt")
        sizePolicy2.setHeightForWidth(self.weekButt.sizePolicy().hasHeightForWidth())
        self.weekButt.setSizePolicy(sizePolicy2)
        self.weekButt.setStyleSheet(u"color: white")
        self.weekButt.setCheckable(False)

        self.horizontalLayout.addWidget(self.weekButt)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)


        self.verticalLayout.addWidget(self.TimeFrame)

        self.ChartFrame = QFrame(Form)
        self.ChartFrame.setObjectName(u"ChartFrame")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.ChartFrame.sizePolicy().hasHeightForWidth())
        self.ChartFrame.setSizePolicy(sizePolicy3)
        self.ChartFrame.setStyleSheet(u"")
        self.ChartFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.ChartFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.ChartFrame)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout.addWidget(self.ChartFrame)

        self.tableWidget = QTableWidget(Form)
        if (self.tableWidget.columnCount() < 2):
            self.tableWidget.setColumnCount(2)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        self.tableWidget.setObjectName(u"tableWidget")
        sizePolicy3.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy3)
        self.tableWidget.setStyleSheet(u"    QHeaderView::section {\n"
"        color: white;\n"
"    }")
        self.tableWidget.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.tableWidget.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)
        self.tableWidget.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.tableWidget.setShowGrid(False)
        self.tableWidget.horizontalHeader().setVisible(True)
        self.tableWidget.verticalHeader().setVisible(False)

        self.verticalLayout.addWidget(self.tableWidget)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.addButton.setText(QCoreApplication.translate("Form", u"+", None))
        self.yearButt.setText(QCoreApplication.translate("Form", u"Year", None))
        self.monthButt.setText(QCoreApplication.translate("Form", u"Month", None))
        self.weekButt.setText(QCoreApplication.translate("Form", u"Week", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Form", u"Application", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Form", u"Uptime", None));
    # retranslateUi

