# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'AddAppDialog.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QDialog, QFrame,
    QGridLayout, QLineEdit, QListWidget, QListWidgetItem,
    QPushButton, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(632, 447)
        Dialog.setStyleSheet(u"background-color: rgb(61, 64, 69);\n"
"color:white;")
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.searchLineEdit = QLineEdit(Dialog)
        self.searchLineEdit.setObjectName(u"searchLineEdit")
        self.searchLineEdit.setStyleSheet(u"border:1px solid grey;\n"
"color:white")

        self.verticalLayout.addWidget(self.searchLineEdit)

        self.foundAppsList = QListWidget(Dialog)
        self.foundAppsList.setObjectName(u"foundAppsList")
        self.foundAppsList.setStyleSheet(u"border:1px solid grey;\n"
"color : white")
        self.foundAppsList.setEditTriggers(QAbstractItemView.EditTrigger.DoubleClicked)

        self.verticalLayout.addWidget(self.foundAppsList)

        self.buttonFrame = QFrame(Dialog)
        self.buttonFrame.setObjectName(u"buttonFrame")
        self.buttonFrame.setStyleSheet(u"QFrame{\n"
"border:1px solid grey\n"
"}\n"
"")
        self.buttonFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.buttonFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout = QGridLayout(self.buttonFrame)
        self.gridLayout.setObjectName(u"gridLayout")
        self.addButton = QPushButton(self.buttonFrame)
        self.addButton.setObjectName(u"addButton")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.addButton.sizePolicy().hasHeightForWidth())
        self.addButton.setSizePolicy(sizePolicy)
        self.addButton.setStyleSheet(u"color: white")

        self.gridLayout.addWidget(self.addButton, 1, 1, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 1, 0, 1, 1)


        self.verticalLayout.addWidget(self.buttonFrame)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.addButton.setText(QCoreApplication.translate("Dialog", u"Add", None))
    # retranslateUi

