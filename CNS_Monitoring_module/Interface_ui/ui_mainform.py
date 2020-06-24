# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainformgnEvNI.ui'
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
        MainWindow.resize(1000, 745)
        MainWindow.setMinimumSize(QSize(1000, 500))
        MainWindow.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.Top_bar = QFrame(self.centralwidget)
        self.Top_bar.setObjectName(u"Top_bar")
        self.Top_bar.setMaximumSize(QSize(16777215, 40))
        self.Top_bar.setStyleSheet(u"background-color: rgb(29, 28, 53);\n"
"")
        self.Top_bar.setFrameShape(QFrame.NoFrame)
        self.Top_bar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.Top_bar)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.Top_toggle = QFrame(self.Top_bar)
        self.Top_toggle.setObjectName(u"Top_toggle")
        self.Top_toggle.setMaximumSize(QSize(100, 100))
        self.Top_toggle.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.Top_toggle.setFrameShape(QFrame.NoFrame)
        self.Top_toggle.setFrameShadow(QFrame.Plain)
        self.Top_toggle.setLineWidth(0)
        self.verticalLayout_2 = QVBoxLayout(self.Top_toggle)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
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

        self.verticalLayout_2.addWidget(self.Run)


        self.horizontalLayout.addWidget(self.Top_toggle)

        self.Top_width = QFrame(self.Top_bar)
        self.Top_width.setObjectName(u"Top_width")
        self.Top_width.setFrameShape(QFrame.NoFrame)
        self.Top_width.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.Top_width)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.Top_width_output = QLabel(self.Top_width)
        self.Top_width_output.setObjectName(u"Top_width_output")
        self.Top_width_output.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 75 14pt \"\ub9d1\uc740 \uace0\ub515\";")
        self.Top_width_output.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_3.addWidget(self.Top_width_output)

        self.Top_width_emp = QLabel(self.Top_width)
        self.Top_width_emp.setObjectName(u"Top_width_emp")
        self.Top_width_emp.setMaximumSize(QSize(300, 16777215))
        self.Top_width_emp.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 75 14pt \"\ub9d1\uc740 \uace0\ub515\";")
        self.Top_width_emp.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.Top_width_emp)


        self.horizontalLayout.addWidget(self.Top_width)


        self.verticalLayout.addWidget(self.Top_bar)

        self.Content = QFrame(self.centralwidget)
        self.Content.setObjectName(u"Content")
        self.Content.setFrameShape(QFrame.NoFrame)
        self.Content.setFrameShadow(QFrame.Raised)
        self.Content.setLineWidth(0)
        self.horizontalLayout_2 = QHBoxLayout(self.Content)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.Content_left = QFrame(self.Content)
        self.Content_left.setObjectName(u"Content_left")
        self.Content_left.setMaximumSize(QSize(100, 16777215))
        self.Content_left.setStyleSheet(u"background-color: rgb(37, 35, 63);")
        self.Content_left.setFrameShape(QFrame.StyledPanel)
        self.Content_left.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.Content_left)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.Content_menu = QFrame(self.Content_left)
        self.Content_menu.setObjectName(u"Content_menu")
        self.Content_menu.setFrameShape(QFrame.NoFrame)
        self.Content_menu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.Content_menu)
        self.verticalLayout_4.setSpacing(5)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(5, 5, 5, 5)
        self.Ini_setting = QPushButton(self.Content_menu)
        self.Ini_setting.setObjectName(u"Ini_setting")
        self.Ini_setting.setMaximumSize(QSize(16777215, 20))
        self.Ini_setting.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	font: 75 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"	border: 2px solid  #dddddd;\n"
"}\n"
"QPushButton:hover {\n"
"	color: rgb(0, 0, 0);\n"
"	font: 75 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"	border: 2px solid  #dddddd;\n"
"	background-color: rgb(229, 229, 229);\n"
"}\n"
"QPushButton:pressed{\n"
"	color: rgb(204, 18, 89);\n"
"	font: 75 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"	border: 2px solid  #dddddd;\n"
"	background-color: rgb(229, 229, 229);\n"
"}\n"
"")

        self.verticalLayout_4.addWidget(self.Ini_setting)

        self.Line_ini_0 = QLineEdit(self.Content_menu)
        self.Line_ini_0.setObjectName(u"Line_ini_0")
        self.Line_ini_0.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.Line_ini_0.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.Line_ini_0)

        self.Content_menu_empty_2 = QLabel(self.Content_menu)
        self.Content_menu_empty_2.setObjectName(u"Content_menu_empty_2")
        self.Content_menu_empty_2.setMaximumSize(QSize(16777215, 30))

        self.verticalLayout_4.addWidget(self.Content_menu_empty_2)

        self.Mal_setting = QPushButton(self.Content_menu)
        self.Mal_setting.setObjectName(u"Mal_setting")
        self.Mal_setting.setMaximumSize(QSize(16777215, 40))
        self.Mal_setting.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	font: 75 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"	border: 2px solid  #dddddd;\n"
"}\n"
"QPushButton:hover {\n"
"	color: rgb(0, 0, 0);\n"
"	font: 75 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"	border: 2px solid  #dddddd;\n"
"	background-color: rgb(229, 229, 229);\n"
"}\n"
"QPushButton:pressed{\n"
"	color: rgb(204, 18, 89);\n"
"	font: 75 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"	border: 2px solid  #dddddd;\n"
"	background-color: rgb(229, 229, 229);\n"
"}\n"
"")

        self.verticalLayout_4.addWidget(self.Mal_setting)

        self.Label_mal_0_case = QLabel(self.Content_menu)
        self.Label_mal_0_case.setObjectName(u"Label_mal_0_case")
        self.Label_mal_0_case.setMaximumSize(QSize(16777215, 20))
        self.Label_mal_0_case.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 75 9pt \"\ub9d1\uc740 \uace0\ub515\";")
        self.Label_mal_0_case.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.Label_mal_0_case)

        self.Line_mal_0_case = QLineEdit(self.Content_menu)
        self.Line_mal_0_case.setObjectName(u"Line_mal_0_case")
        self.Line_mal_0_case.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.Line_mal_0_case.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.Line_mal_0_case)

        self.Label_mal_1_nub = QLabel(self.Content_menu)
        self.Label_mal_1_nub.setObjectName(u"Label_mal_1_nub")
        self.Label_mal_1_nub.setMaximumSize(QSize(16777215, 20))
        self.Label_mal_1_nub.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 75 9pt \"\ub9d1\uc740 \uace0\ub515\";")
        self.Label_mal_1_nub.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.Label_mal_1_nub)

        self.Line_mal_1_nub = QLineEdit(self.Content_menu)
        self.Line_mal_1_nub.setObjectName(u"Line_mal_1_nub")
        self.Line_mal_1_nub.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.Line_mal_1_nub.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.Line_mal_1_nub)

        self.Label_mal_2_time = QLabel(self.Content_menu)
        self.Label_mal_2_time.setObjectName(u"Label_mal_2_time")
        self.Label_mal_2_time.setMaximumSize(QSize(16777215, 20))
        self.Label_mal_2_time.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 75 9pt \"\ub9d1\uc740 \uace0\ub515\";")
        self.Label_mal_2_time.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.Label_mal_2_time)

        self.Line_mal_2_time = QLineEdit(self.Content_menu)
        self.Line_mal_2_time.setObjectName(u"Line_mal_2_time")
        self.Line_mal_2_time.setMaximumSize(QSize(16777215, 20))
        self.Line_mal_2_time.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.Line_mal_2_time.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.Line_mal_2_time)

        self.Content_menu_empty_0 = QPushButton(self.Content_menu)
        self.Content_menu_empty_0.setObjectName(u"Content_menu_empty_0")
        self.Content_menu_empty_0.setMaximumSize(QSize(16777215, 1000))
        self.Content_menu_empty_0.setStyleSheet(u"border: none; ")

        self.verticalLayout_4.addWidget(self.Content_menu_empty_0)


        self.verticalLayout_3.addWidget(self.Content_menu)


        self.horizontalLayout_2.addWidget(self.Content_left)

        self.Content_right = QFrame(self.Content)
        self.Content_right.setObjectName(u"Content_right")
        self.Content_right.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.Content_right.setFrameShape(QFrame.StyledPanel)
        self.Content_right.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.Content_right)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.Coten_right_0_top = QFrame(self.Content_right)
        self.Coten_right_0_top.setObjectName(u"Coten_right_0_top")
        self.Coten_right_0_top.setFrameShape(QFrame.StyledPanel)
        self.Coten_right_0_top.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.Coten_right_0_top)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.GP_0_1 = QVBoxLayout()
        self.GP_0_1.setObjectName(u"GP_0_1")

        self.horizontalLayout_4.addLayout(self.GP_0_1)

        self.GP_0_2 = QVBoxLayout()
        self.GP_0_2.setObjectName(u"GP_0_2")

        self.horizontalLayout_4.addLayout(self.GP_0_2)

        self.GP_0_3 = QVBoxLayout()
        self.GP_0_3.setObjectName(u"GP_0_3")

        self.horizontalLayout_4.addLayout(self.GP_0_3)

        self.GP_0_4 = QVBoxLayout()
        self.GP_0_4.setObjectName(u"GP_0_4")

        self.horizontalLayout_4.addLayout(self.GP_0_4)

        self.GP_0_5 = QVBoxLayout()
        self.GP_0_5.setObjectName(u"GP_0_5")

        self.horizontalLayout_4.addLayout(self.GP_0_5)


        self.verticalLayout_5.addWidget(self.Coten_right_0_top)

        self.Coten_right_1_bot = QFrame(self.Content_right)
        self.Coten_right_1_bot.setObjectName(u"Coten_right_1_bot")
        self.Coten_right_1_bot.setFrameShape(QFrame.StyledPanel)
        self.Coten_right_1_bot.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.Coten_right_1_bot)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.GP_1_1 = QVBoxLayout()
        self.GP_1_1.setObjectName(u"GP_1_1")

        self.horizontalLayout_5.addLayout(self.GP_1_1)

        self.GP_1_2 = QVBoxLayout()
        self.GP_1_2.setObjectName(u"GP_1_2")

        self.horizontalLayout_5.addLayout(self.GP_1_2)

        self.GP_1_3 = QVBoxLayout()
        self.GP_1_3.setObjectName(u"GP_1_3")

        self.horizontalLayout_5.addLayout(self.GP_1_3)

        self.GP_1_4 = QVBoxLayout()
        self.GP_1_4.setObjectName(u"GP_1_4")

        self.horizontalLayout_5.addLayout(self.GP_1_4)

        self.GP_1_5 = QVBoxLayout()
        self.GP_1_5.setObjectName(u"GP_1_5")

        self.horizontalLayout_5.addLayout(self.GP_1_5)


        self.verticalLayout_5.addWidget(self.Coten_right_1_bot)


        self.horizontalLayout_2.addWidget(self.Content_right)


        self.verticalLayout.addWidget(self.Content)

        MainWindow.setCentralWidget(self.centralwidget)

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
        self.Mal_setting.setText(QCoreApplication.translate("MainWindow", u"Malfunction Setting", None))
        self.Label_mal_0_case.setText(QCoreApplication.translate("MainWindow", u"Mal_case", None))
        self.Label_mal_1_nub.setText(QCoreApplication.translate("MainWindow", u"Mal_number", None))
        self.Label_mal_2_time.setText(QCoreApplication.translate("MainWindow", u"Mal_time", None))
        self.Content_menu_empty_0.setText("")
    # retranslateUi

