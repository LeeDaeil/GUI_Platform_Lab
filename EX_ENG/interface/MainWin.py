# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWInrIkNek.ui'
##
## Created by: Qt User Interface Compiler version 5.15.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QDate, QDateTime, QMetaObject,
    QObject, QPoint, QRect, QSize, QTime, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter,
    QPixmap, QRadialGradient)
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.Nub_Frame = QFrame(self.centralwidget)
        self.Nub_Frame.setObjectName(u"Nub_Frame")
        self.Nub_Frame.setFrameShape(QFrame.StyledPanel)
        self.Nub_Frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.Nub_Frame)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.lineEdit = QLineEdit(self.Nub_Frame)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setMinimumSize(QSize(100, 0))
        self.lineEdit.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout.addWidget(self.lineEdit)

        self.horizontalSpacer = QSpacerItem(677, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)


        self.verticalLayout.addWidget(self.Nub_Frame)

        self.DB_Frame = QFrame(self.centralwidget)
        self.DB_Frame.setObjectName(u"DB_Frame")
        self.DB_Frame.setFrameShape(QFrame.StyledPanel)
        self.DB_Frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.DB_Frame)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.DB_Tabel = QTableView(self.DB_Frame)
        self.DB_Tabel.setObjectName(u"DB_Tabel")

        self.horizontalLayout_2.addWidget(self.DB_Tabel)


        self.verticalLayout.addWidget(self.DB_Frame)

        self.ContPanel = QFrame(self.centralwidget)
        self.ContPanel.setObjectName(u"ContPanel")
        self.ContPanel.setFrameShape(QFrame.StyledPanel)
        self.ContPanel.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.ContPanel)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.CallPrint = QPushButton(self.ContPanel)
        self.CallPrint.setObjectName(u"CallPrint")
        self.CallPrint.setMinimumSize(QSize(70, 0))

        self.horizontalLayout_3.addWidget(self.CallPrint)

        self.horizontalSpacer_2 = QSpacerItem(10, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)

        self.CallMakeDB = QPushButton(self.ContPanel)
        self.CallMakeDB.setObjectName(u"CallMakeDB")
        self.CallMakeDB.setMinimumSize(QSize(70, 0))

        self.horizontalLayout_3.addWidget(self.CallMakeDB)

        self.horizontalSpacer_3 = QSpacerItem(10, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_3)

        self.CallSend = QPushButton(self.ContPanel)
        self.CallSend.setObjectName(u"CallSend")
        self.CallSend.setMinimumSize(QSize(70, 0))

        self.horizontalLayout_3.addWidget(self.CallSend)

        self.horizontalSpacer_4 = QSpacerItem(10, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_4)

        self.CallShowAns = QPushButton(self.ContPanel)
        self.CallShowAns.setObjectName(u"CallShowAns")
        self.CallShowAns.setMinimumSize(QSize(70, 0))

        self.horizontalLayout_3.addWidget(self.CallShowAns)

        self.horizontalSpacer_5 = QSpacerItem(10, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_5)

        self.CallExit = QPushButton(self.ContPanel)
        self.CallExit.setObjectName(u"CallExit")
        self.CallExit.setMinimumSize(QSize(70, 0))

        self.horizontalLayout_3.addWidget(self.CallExit)


        self.verticalLayout.addWidget(self.ContPanel)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.CallPrint.setText(QCoreApplication.translate("MainWindow", u"Print", None))
        self.CallMakeDB.setText(QCoreApplication.translate("MainWindow", u"\ubb38\uc81c\ub9cc\ub4e4\uae30", None))
        self.CallSend.setText(QCoreApplication.translate("MainWindow", u"\uc81c\ucd9c", None))
        self.CallShowAns.setText(QCoreApplication.translate("MainWindow", u"\uc815\ub2f5\ubcf4\uae30", None))
        self.CallExit.setText(QCoreApplication.translate("MainWindow", u"\ub2eb\uae30", None))
    # retranslateUi

