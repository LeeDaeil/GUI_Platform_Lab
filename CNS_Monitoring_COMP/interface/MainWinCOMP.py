# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWinCOMPzLuGsQ.ui'
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
        MainWindow.resize(763, 845)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_4 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.Top_bar = QFrame(self.centralwidget)
        self.Top_bar.setObjectName(u"Top_bar")
        self.Top_bar.setMaximumSize(QSize(16777215, 40))
        self.Top_bar.setStyleSheet(u"background-color: rgb(29, 28, 53);\n"
"")
        self.Top_bar.setFrameShape(QFrame.NoFrame)
        self.Top_bar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.Top_bar)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.Top_toggle = QFrame(self.Top_bar)
        self.Top_toggle.setObjectName(u"Top_toggle")
        self.Top_toggle.setMaximumSize(QSize(100, 100))
        self.Top_toggle.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.Top_toggle.setFrameShape(QFrame.NoFrame)
        self.Top_toggle.setFrameShadow(QFrame.Plain)
        self.Top_toggle.setLineWidth(0)
        self.verticalLayout_3 = QVBoxLayout(self.Top_toggle)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.Run = QPushButton(self.Top_toggle)
        self.Run.setObjectName(u"Run")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Run.sizePolicy().hasHeightForWidth())
        self.Run.setSizePolicy(sizePolicy)
        self.Run.setStyleSheet(u"QPushButton {\n"
"	font: 70 14pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"	background-color: rgb(255, 209, 0);\n"
"}\n"
"QPushButton:hover {\n"
"	font: 70 14pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"	background-color: rgb(255, 93, 86);\n"
"}\n"
"QPushButton:checked {\n"
"	font: 70 14pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"	background-color: rgb(0, 93, 86);\n"
"	border: none; \n"
"}\n"
"\n"
"")
        self.Run.setCheckable(True)

        self.verticalLayout_3.addWidget(self.Run)


        self.horizontalLayout_2.addWidget(self.Top_toggle)

        self.Top_width = QFrame(self.Top_bar)
        self.Top_width.setObjectName(u"Top_width")
        self.Top_width.setFrameShape(QFrame.NoFrame)
        self.Top_width.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.Top_width)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.Top_width_output = QLabel(self.Top_width)
        self.Top_width_output.setObjectName(u"Top_width_output")
        self.Top_width_output.setStyleSheet(u"QLabel {\n"
"    border: 2px solid rgb(52,49,89);\n"
"    border-radius: 5px;\n"
"    padding: 0 8px;\n"
"    background: rgb(52,49,89);\n"
"	font: 75 14pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"	color: rgb(255, 255, 255);\n"
"    selection-background-color: darkgray;\n"
"}")
        self.Top_width_output.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_3.addWidget(self.Top_width_output)

        self.Top_width_emp = QLabel(self.Top_width)
        self.Top_width_emp.setObjectName(u"Top_width_emp")
        self.Top_width_emp.setMaximumSize(QSize(300, 16777215))
        self.Top_width_emp.setStyleSheet(u"QLabel {\n"
"    border: 2px solid rgb(52,49,89);\n"
"    border-radius: 5px;\n"
"    padding: 0 8px;\n"
"    background: rgb(52,49,89);\n"
"	font: 75 14pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"	color: rgb(255, 255, 255);\n"
"    selection-background-color: darkgray;\n"
"}")
        self.Top_width_emp.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.Top_width_emp)


        self.horizontalLayout_2.addWidget(self.Top_width)


        self.verticalLayout_4.addWidget(self.Top_bar)

        self.Bottom = QFrame(self.centralwidget)
        self.Bottom.setObjectName(u"Bottom")
        self.Bottom.setFrameShape(QFrame.StyledPanel)
        self.Bottom.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.Bottom)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.Content_menu = QFrame(self.Bottom)
        self.Content_menu.setObjectName(u"Content_menu")
        self.Content_menu.setMaximumSize(QSize(150, 16777215))
        self.Content_menu.setFrameShape(QFrame.NoFrame)
        self.Content_menu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.Content_menu)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, -1)
        self.Ini_setting = QPushButton(self.Content_menu)
        self.Ini_setting.setObjectName(u"Ini_setting")
        self.Ini_setting.setMaximumSize(QSize(16777215, 20))
        self.Ini_setting.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	font: 75 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"    border-radius: 10px;\n"
"	background-color: rgb(52,49,89);\n"
"}\n"
"QPushButton:hover {\n"
"	color: rgb(255, 255, 255);\n"
"	font: 75 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"	border: 1px solid  #dddddd;\n"
"    border-radius: 10px;\n"
"	background-color: rgb(52,49,89);\n"
"}\n"
"QPushButton:pressed{\n"
"	color: rgb(204, 18, 89);\n"
"	font: 75 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"	border: 2px solid  #dddddd;\n"
"    border-radius: 10px;\n"
"	background-color: rgb(52,49,89);\n"
"}\n"
"")

        self.verticalLayout_2.addWidget(self.Ini_setting)

        self.Line_ini_0 = QLineEdit(self.Content_menu)
        self.Line_ini_0.setObjectName(u"Line_ini_0")
        self.Line_ini_0.setStyleSheet(u"QLineEdit {\n"
"    border: 2px solid rgb(52,49,89);\n"
"    border-radius: 5px;\n"
"    padding: 0 8px;\n"
"    background: rgb(52,49,89);\n"
"	color: rgb(255, 255, 255);\n"
"    selection-background-color: darkgray;\n"
"}")
        self.Line_ini_0.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.Line_ini_0)

        self.Content_menu_empty_2 = QLabel(self.Content_menu)
        self.Content_menu_empty_2.setObjectName(u"Content_menu_empty_2")
        self.Content_menu_empty_2.setMaximumSize(QSize(16777215, 30))

        self.verticalLayout_2.addWidget(self.Content_menu_empty_2)

        self.Mal_setting = QPushButton(self.Content_menu)
        self.Mal_setting.setObjectName(u"Mal_setting")
        self.Mal_setting.setMaximumSize(QSize(16777215, 40))
        self.Mal_setting.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	font: 75 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"    border-radius: 10px;\n"
"	background-color: rgb(52,49,89);\n"
"}\n"
"QPushButton:hover {\n"
"	color: rgb(255, 255, 255);\n"
"	font: 75 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"	border: 1px solid  #dddddd;\n"
"    border-radius: 10px;\n"
"	background-color: rgb(52,49,89);\n"
"}\n"
"QPushButton:pressed{\n"
"	color: rgb(204, 18, 89);\n"
"	font: 75 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"	border: 2px solid  #dddddd;\n"
"    border-radius: 10px;\n"
"	background-color: rgb(52,49,89);\n"
"}\n"
"")

        self.verticalLayout_2.addWidget(self.Mal_setting)

        self.Label_mal_0_case = QLabel(self.Content_menu)
        self.Label_mal_0_case.setObjectName(u"Label_mal_0_case")
        self.Label_mal_0_case.setMaximumSize(QSize(16777215, 20))
        self.Label_mal_0_case.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 75 9pt \"\ub9d1\uc740 \uace0\ub515\";")
        self.Label_mal_0_case.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.Label_mal_0_case)

        self.Line_mal_0_case = QLineEdit(self.Content_menu)
        self.Line_mal_0_case.setObjectName(u"Line_mal_0_case")
        self.Line_mal_0_case.setStyleSheet(u"QLineEdit {\n"
"    border: 2px solid rgb(52,49,89);\n"
"    border-radius: 5px;\n"
"    padding: 0 8px;\n"
"    background: rgb(52,49,89);\n"
"	color: rgb(255, 255, 255);\n"
"    selection-background-color: darkgray;\n"
"}")
        self.Line_mal_0_case.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.Line_mal_0_case)

        self.Label_mal_1_nub = QLabel(self.Content_menu)
        self.Label_mal_1_nub.setObjectName(u"Label_mal_1_nub")
        self.Label_mal_1_nub.setMaximumSize(QSize(16777215, 20))
        self.Label_mal_1_nub.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 75 9pt \"\ub9d1\uc740 \uace0\ub515\";")
        self.Label_mal_1_nub.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.Label_mal_1_nub)

        self.Line_mal_1_nub = QLineEdit(self.Content_menu)
        self.Line_mal_1_nub.setObjectName(u"Line_mal_1_nub")
        self.Line_mal_1_nub.setStyleSheet(u"QLineEdit {\n"
"    border: 2px solid rgb(52,49,89);\n"
"    border-radius: 5px;\n"
"    padding: 0 8px;\n"
"    background: rgb(52,49,89);\n"
"	color: rgb(255, 255, 255);\n"
"    selection-background-color: darkgray;\n"
"}")
        self.Line_mal_1_nub.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.Line_mal_1_nub)

        self.Label_mal_2_time = QLabel(self.Content_menu)
        self.Label_mal_2_time.setObjectName(u"Label_mal_2_time")
        self.Label_mal_2_time.setMaximumSize(QSize(16777215, 20))
        self.Label_mal_2_time.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 75 9pt \"\ub9d1\uc740 \uace0\ub515\";")
        self.Label_mal_2_time.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.Label_mal_2_time)

        self.Line_mal_2_time = QLineEdit(self.Content_menu)
        self.Line_mal_2_time.setObjectName(u"Line_mal_2_time")
        self.Line_mal_2_time.setMaximumSize(QSize(16777215, 20))
        self.Line_mal_2_time.setStyleSheet(u"QLineEdit {\n"
"    border: 2px solid rgb(52,49,89);\n"
"    border-radius: 5px;\n"
"    padding: 0 8px;\n"
"    background: rgb(52,49,89);\n"
"	color: rgb(255, 255, 255);\n"
"    selection-background-color: darkgray;\n"
"}")
        self.Line_mal_2_time.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.Line_mal_2_time)

        self.Sys = QFrame(self.Content_menu)
        self.Sys.setObjectName(u"Sys")
        self.Sys.setMinimumSize(QSize(0, 0))
        self.Sys.setMaximumSize(QSize(16777215, 16777215))
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


        self.verticalLayout_2.addWidget(self.Sys)


        self.horizontalLayout.addWidget(self.Content_menu)

        self.Right = QFrame(self.Bottom)
        self.Right.setObjectName(u"Right")
        self.Right.setFrameShape(QFrame.StyledPanel)
        self.Right.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.Right)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(5, 5, 5, 5)
        self.ShowTable = QTableWidget(self.Right)
        self.ShowTable.setObjectName(u"ShowTable")
        self.ShowTable.setMinimumSize(QSize(0, 0))
        self.ShowTable.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout.addWidget(self.ShowTable, 0, 0, 1, 1)


        self.horizontalLayout.addWidget(self.Right)


        self.verticalLayout_4.addWidget(self.Bottom)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 763, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.Run.setText(QCoreApplication.translate("MainWindow", u"RUN", None))
        self.Top_width_output.setText(QCoreApplication.translate("MainWindow", u"Current Condition:", None))
        self.Top_width_emp.setText("")
        self.Ini_setting.setText(QCoreApplication.translate("MainWindow", u"Initial Setting", None))
        self.Content_menu_empty_2.setText("")
        self.Mal_setting.setText(QCoreApplication.translate("MainWindow", u"Malfunction\n"
"Setting", None))
        self.Label_mal_0_case.setText(QCoreApplication.translate("MainWindow", u"Mal_case", None))
        self.Label_mal_1_nub.setText(QCoreApplication.translate("MainWindow", u"Mal_number", None))
        self.Label_mal_2_time.setText(QCoreApplication.translate("MainWindow", u"Mal_time", None))
        self.SysRCS.setText(QCoreApplication.translate("MainWindow", u"RCS", None))
        self.SysCVCS.setText(QCoreApplication.translate("MainWindow", u"CVCS", None))
        self.SysRHR.setText(QCoreApplication.translate("MainWindow", u"RHR", None))
        self.SysMSTB.setText(QCoreApplication.translate("MainWindow", u"MS/TB", None))
        self.SysFWS.setText(QCoreApplication.translate("MainWindow", u"FWS", None))
        self.SysCOND.setText(QCoreApplication.translate("MainWindow", u"COND", None))
        self.SysELEC.setText(QCoreApplication.translate("MainWindow", u"ELEC", None))
        self.SysROD.setText(QCoreApplication.translate("MainWindow", u"ROD", None))
    # retranslateUi

