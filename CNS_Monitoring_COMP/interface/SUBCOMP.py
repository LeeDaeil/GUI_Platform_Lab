# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'SUBCOMPtNaTPH.ui'
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


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(250, 308)
        self.verticalLayout_2 = QVBoxLayout(Dialog)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame = QFrame(Dialog)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.SYS = QLabel(self.frame)
        self.SYS.setObjectName(u"SYS")
        self.SYS.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.SYS)

        self.TYPE = QLabel(self.frame)
        self.TYPE.setObjectName(u"TYPE")
        self.TYPE.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.TYPE)

        self.ONECONT = QLabel(self.frame)
        self.ONECONT.setObjectName(u"ONECONT")
        self.ONECONT.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.ONECONT)

        self.OnManOpen = QLabel(self.frame)
        self.OnManOpen.setObjectName(u"OnManOpen")
        self.OnManOpen.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.OnManOpen)

        self.OffAutoClose = QLabel(self.frame)
        self.OffAutoClose.setObjectName(u"OffAutoClose")
        self.OffAutoClose.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.OffAutoClose)

        self.OffAutoClose_2 = QLabel(self.frame)
        self.OffAutoClose_2.setObjectName(u"OffAutoClose_2")
        self.OffAutoClose_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.OffAutoClose_2)


        self.verticalLayout_2.addWidget(self.frame)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.SYS.setText(QCoreApplication.translate("Dialog", u"SYS", None))
        self.TYPE.setText(QCoreApplication.translate("Dialog", u"TYPE", None))
        self.ONECONT.setText(QCoreApplication.translate("Dialog", u"ONECONT", None))
        self.OnManOpen.setText(QCoreApplication.translate("Dialog", u"OnManOpen", None))
        self.OffAutoClose.setText(QCoreApplication.translate("Dialog", u"OffAutoClose", None))
        self.OffAutoClose_2.setText(QCoreApplication.translate("Dialog", u"Purpose", None))
    # retranslateUi

