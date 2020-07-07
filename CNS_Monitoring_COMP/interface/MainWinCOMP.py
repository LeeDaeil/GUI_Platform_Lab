# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWinCOMPwSCKLX.ui'
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
        MainWindow.resize(938, 682)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.Sys = QFrame(self.centralwidget)
        self.Sys.setObjectName(u"Sys")
        self.Sys.setMinimumSize(QSize(0, 0))
        self.Sys.setMaximumSize(QSize(80, 16777215))
        self.Sys.setFrameShape(QFrame.StyledPanel)
        self.Sys.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.Sys)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.SysRCS = QRadioButton(self.Sys)
        self.SysRCS.setObjectName(u"SysRCS")

        self.verticalLayout.addWidget(self.SysRCS)

        self.SysCVCS = QRadioButton(self.Sys)
        self.SysCVCS.setObjectName(u"SysCVCS")

        self.verticalLayout.addWidget(self.SysCVCS)

        self.SysRHR = QRadioButton(self.Sys)
        self.SysRHR.setObjectName(u"SysRHR")

        self.verticalLayout.addWidget(self.SysRHR)

        self.SysMSTB = QRadioButton(self.Sys)
        self.SysMSTB.setObjectName(u"SysMSTB")

        self.verticalLayout.addWidget(self.SysMSTB)

        self.SysFWS = QRadioButton(self.Sys)
        self.SysFWS.setObjectName(u"SysFWS")

        self.verticalLayout.addWidget(self.SysFWS)

        self.SysCOND = QRadioButton(self.Sys)
        self.SysCOND.setObjectName(u"SysCOND")

        self.verticalLayout.addWidget(self.SysCOND)

        self.SysELEC = QRadioButton(self.Sys)
        self.SysELEC.setObjectName(u"SysELEC")

        self.verticalLayout.addWidget(self.SysELEC)

        self.SysROD = QRadioButton(self.Sys)
        self.SysROD.setObjectName(u"SysROD")

        self.verticalLayout.addWidget(self.SysROD)


        self.horizontalLayout.addWidget(self.Sys)

        self.Right = QFrame(self.centralwidget)
        self.Right.setObjectName(u"Right")
        self.Right.setFrameShape(QFrame.StyledPanel)
        self.Right.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.Right)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(5, 5, 5, 5)
        self.ShowTable = QTableView(self.Right)
        self.ShowTable.setObjectName(u"ShowTable")
        self.ShowTable.setMinimumSize(QSize(0, 0))
        self.ShowTable.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout.addWidget(self.ShowTable, 0, 0, 1, 1)


        self.horizontalLayout.addWidget(self.Right)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 938, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.SysRCS.setText(QCoreApplication.translate("MainWindow", u"RCS", None))
        self.SysCVCS.setText(QCoreApplication.translate("MainWindow", u"CVCS", None))
        self.SysRHR.setText(QCoreApplication.translate("MainWindow", u"RHR", None))
        self.SysMSTB.setText(QCoreApplication.translate("MainWindow", u"MS/TB", None))
        self.SysFWS.setText(QCoreApplication.translate("MainWindow", u"FWS", None))
        self.SysCOND.setText(QCoreApplication.translate("MainWindow", u"COND", None))
        self.SysELEC.setText(QCoreApplication.translate("MainWindow", u"ELEC", None))
        self.SysROD.setText(QCoreApplication.translate("MainWindow", u"ROD", None))
    # retranslateUi

