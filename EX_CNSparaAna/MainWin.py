# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWinIleLuL.ui'
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
        MainWindow.resize(396, 630)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_3 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.Sys = QFrame(self.frame)
        self.Sys.setObjectName(u"Sys")
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


        self.horizontalLayout_5.addWidget(self.Sys)

        self.Type_bu = QFrame(self.frame)
        self.Type_bu.setObjectName(u"Type_bu")
        self.Type_bu.setFrameShape(QFrame.StyledPanel)
        self.Type_bu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.Type_bu)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.Onoff_0 = QLabel(self.Type_bu)
        self.Onoff_0.setObjectName(u"Onoff_0")

        self.verticalLayout_2.addWidget(self.Onoff_0)

        self.Onoff_1 = QRadioButton(self.Type_bu)
        self.Onoff_1.setObjectName(u"Onoff_1")

        self.verticalLayout_2.addWidget(self.Onoff_1)

        self.Onoff_2 = QRadioButton(self.Type_bu)
        self.Onoff_2.setObjectName(u"Onoff_2")

        self.verticalLayout_2.addWidget(self.Onoff_2)

        self.Onoff_3 = QRadioButton(self.Type_bu)
        self.Onoff_3.setObjectName(u"Onoff_3")

        self.verticalLayout_2.addWidget(self.Onoff_3)

        self.Onoff_4 = QRadioButton(self.Type_bu)
        self.Onoff_4.setObjectName(u"Onoff_4")

        self.verticalLayout_2.addWidget(self.Onoff_4)

        self.Onoff_5 = QRadioButton(self.Type_bu)
        self.Onoff_5.setObjectName(u"Onoff_5")

        self.verticalLayout_2.addWidget(self.Onoff_5)

        self.Ran_0 = QLabel(self.Type_bu)
        self.Ran_0.setObjectName(u"Ran_0")

        self.verticalLayout_2.addWidget(self.Ran_0)

        self.Ran_1 = QRadioButton(self.Type_bu)
        self.Ran_1.setObjectName(u"Ran_1")

        self.verticalLayout_2.addWidget(self.Ran_1)

        self.Ran_2 = QRadioButton(self.Type_bu)
        self.Ran_2.setObjectName(u"Ran_2")

        self.verticalLayout_2.addWidget(self.Ran_2)

        self.Ran_3 = QRadioButton(self.Type_bu)
        self.Ran_3.setObjectName(u"Ran_3")

        self.verticalLayout_2.addWidget(self.Ran_3)

        self.Mode_0 = QLabel(self.Type_bu)
        self.Mode_0.setObjectName(u"Mode_0")

        self.verticalLayout_2.addWidget(self.Mode_0)

        self.Mode_1 = QRadioButton(self.Type_bu)
        self.Mode_1.setObjectName(u"Mode_1")

        self.verticalLayout_2.addWidget(self.Mode_1)

        self.Mode_2 = QRadioButton(self.Type_bu)
        self.Mode_2.setObjectName(u"Mode_2")

        self.verticalLayout_2.addWidget(self.Mode_2)

        self.Mode_3 = QRadioButton(self.Type_bu)
        self.Mode_3.setObjectName(u"Mode_3")

        self.verticalLayout_2.addWidget(self.Mode_3)

        self.Mode_4 = QRadioButton(self.Type_bu)
        self.Mode_4.setObjectName(u"Mode_4")

        self.verticalLayout_2.addWidget(self.Mode_4)


        self.horizontalLayout_5.addWidget(self.Type_bu)


        self.verticalLayout_3.addWidget(self.frame)

        self.ID_ = QFrame(self.centralwidget)
        self.ID_.setObjectName(u"ID_")
        self.ID_.setFrameShape(QFrame.StyledPanel)
        self.ID_.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.ID_)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.frame_3 = QFrame(self.ID_)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_3)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.frame_3)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(120, 0))
        self.label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.label)

        self.ID_input = QLineEdit(self.frame_3)
        self.ID_input.setObjectName(u"ID_input")

        self.horizontalLayout.addWidget(self.ID_input)


        self.verticalLayout_5.addWidget(self.frame_3)

        self.frame_2 = QFrame(self.ID_)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_2)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.label_5 = QLabel(self.frame_2)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMinimumSize(QSize(120, 0))
        self.label_5.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_4.addWidget(self.label_5)

        self.Des_out = QLabel(self.frame_2)
        self.Des_out.setObjectName(u"Des_out")
        self.Des_out.setMinimumSize(QSize(120, 0))
        self.Des_out.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_4.addWidget(self.Des_out)


        self.verticalLayout_5.addWidget(self.frame_2)


        self.verticalLayout_3.addWidget(self.ID_)

        self.ID_0 = QFrame(self.centralwidget)
        self.ID_0.setObjectName(u"ID_0")
        self.ID_0.setFrameShape(QFrame.StyledPanel)
        self.ID_0.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.ID_0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_4 = QLabel(self.ID_0)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(120, 0))
        self.label_4.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_4.addWidget(self.label_4)

        self.ID_yes = QRadioButton(self.ID_0)
        self.ID_yes.setObjectName(u"ID_yes")

        self.horizontalLayout_4.addWidget(self.ID_yes)

        self.ID_no = QRadioButton(self.ID_0)
        self.ID_no.setObjectName(u"ID_no")

        self.horizontalLayout_4.addWidget(self.ID_no)


        self.verticalLayout_3.addWidget(self.ID_0)

        self.ID_1 = QFrame(self.centralwidget)
        self.ID_1.setObjectName(u"ID_1")
        self.ID_1.setFrameShape(QFrame.StyledPanel)
        self.ID_1.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.ID_1)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, -1, 0)
        self.label_2 = QLabel(self.ID_1)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(120, 0))
        self.label_2.setStyleSheet(u"color: rgb(9, 93, 0);")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.label_2)

        self.ID_input_2 = QLineEdit(self.ID_1)
        self.ID_input_2.setObjectName(u"ID_input_2")

        self.horizontalLayout_2.addWidget(self.ID_input_2)


        self.verticalLayout_3.addWidget(self.ID_1)

        self.ID_2 = QFrame(self.centralwidget)
        self.ID_2.setObjectName(u"ID_2")
        self.ID_2.setFrameShape(QFrame.StyledPanel)
        self.ID_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.ID_2)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, -1, 0)
        self.label_3 = QLabel(self.ID_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(120, 0))
        self.label_3.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.label_3)

        self.ID_input_3 = QLineEdit(self.ID_2)
        self.ID_input_3.setObjectName(u"ID_input_3")

        self.horizontalLayout_3.addWidget(self.ID_input_3)


        self.verticalLayout_3.addWidget(self.ID_2)

        self.Saveby = QPushButton(self.centralwidget)
        self.Saveby.setObjectName(u"Saveby")

        self.verticalLayout_3.addWidget(self.Saveby)

        self.End_bu = QPushButton(self.centralwidget)
        self.End_bu.setObjectName(u"End_bu")

        self.verticalLayout_3.addWidget(self.End_bu)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 396, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        QWidget.setTabOrder(self.SysRCS, self.SysCVCS)
        QWidget.setTabOrder(self.SysCVCS, self.SysRHR)
        QWidget.setTabOrder(self.SysRHR, self.SysMSTB)
        QWidget.setTabOrder(self.SysMSTB, self.SysFWS)
        QWidget.setTabOrder(self.SysFWS, self.SysCOND)
        QWidget.setTabOrder(self.SysCOND, self.SysELEC)
        QWidget.setTabOrder(self.SysELEC, self.SysROD)
        QWidget.setTabOrder(self.SysROD, self.Onoff_1)
        QWidget.setTabOrder(self.Onoff_1, self.Onoff_2)
        QWidget.setTabOrder(self.Onoff_2, self.Onoff_3)
        QWidget.setTabOrder(self.Onoff_3, self.Onoff_4)
        QWidget.setTabOrder(self.Onoff_4, self.Ran_1)
        QWidget.setTabOrder(self.Ran_1, self.Ran_2)
        QWidget.setTabOrder(self.Ran_2, self.Ran_3)
        QWidget.setTabOrder(self.Ran_3, self.Mode_1)
        QWidget.setTabOrder(self.Mode_1, self.Mode_2)
        QWidget.setTabOrder(self.Mode_2, self.Mode_3)
        QWidget.setTabOrder(self.Mode_3, self.Mode_4)
        QWidget.setTabOrder(self.Mode_4, self.ID_input)
        QWidget.setTabOrder(self.ID_input, self.ID_yes)
        QWidget.setTabOrder(self.ID_yes, self.ID_no)
        QWidget.setTabOrder(self.ID_no, self.ID_input_2)
        QWidget.setTabOrder(self.ID_input_2, self.ID_input_3)

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
        self.Onoff_0.setText(QCoreApplication.translate("MainWindow", u"On/off \ubc84\ud2bc", None))
        self.Onoff_1.setText(QCoreApplication.translate("MainWindow", u"On/Off Signal block on/off", None))
        self.Onoff_2.setText(QCoreApplication.translate("MainWindow", u"On/Off \ud788\ud130 on/off", None))
        self.Onoff_3.setText(QCoreApplication.translate("MainWindow", u"On/Off \ud38c\ud504 on/off", None))
        self.Onoff_4.setText(QCoreApplication.translate("MainWindow", u"On/Off \ubc38\ube0c on/off", None))
        self.Onoff_5.setText(QCoreApplication.translate("MainWindow", u"On/Off \uae30\uae30 on/off", None))
        self.Ran_0.setText(QCoreApplication.translate("MainWindow", u"\uc870\uc808 \ubc84\ud2bc", None))
        self.Ran_1.setText(QCoreApplication.translate("MainWindow", u"\uc870\uc808 \ubc84\ud2bc (up/down) Setpoint \uc870\uc808 \ubc84\ud2bc", None))
        self.Ran_2.setText(QCoreApplication.translate("MainWindow", u"\uc870\uc808 \ubc84\ud2bc (up/down) \ubc38\ube0c\uac1c\ub3c4 \uc870\uc808 \ubc84\ud2bc", None))
        self.Ran_3.setText(QCoreApplication.translate("MainWindow", u"\uc870\uc808 \ubc84\ud2bc (up/down) \uc81c\uc5b4\ubd09 \uc870\uc808 \ubc84\ud2bc", None))
        self.Mode_0.setText(QCoreApplication.translate("MainWindow", u"Mode \ubc84\ud2bc", None))
        self.Mode_1.setText(QCoreApplication.translate("MainWindow", u"Mode \ubc84\ud2bc Auto/Man \uc120\ud0dd \ubc84\ud2bc", None))
        self.Mode_2.setText(QCoreApplication.translate("MainWindow", u"Mode \ubc84\ud2bc Make-up mode \uc120\ud0dd \ubc84\ud2bc", None))
        self.Mode_3.setText(QCoreApplication.translate("MainWindow", u"Mode \ubc84\ud2bc \uc81c\uc5b4\ubd09 \ubaa8\ub4dc \uc120\ud0dd \ubc84\ud2bc", None))
        self.Mode_4.setText(QCoreApplication.translate("MainWindow", u"Mode \ubc84\ud2bc \uc6b0\ud68c \uc720\ub85c \uc120\ud0dd \ubc84\ud2bc", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"ID", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Des", None))
        self.Des_out.setText(QCoreApplication.translate("MainWindow", u"Des info", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"One Control", None))
        self.ID_yes.setText(QCoreApplication.translate("MainWindow", u"Yes", None))
        self.ID_no.setText(QCoreApplication.translate("MainWindow", u"No", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"On/Man/Open ID", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Off/Auto/Close ID", None))
        self.Saveby.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.End_bu.setText(QCoreApplication.translate("MainWindow", u"End", None))
    # retranslateUi

