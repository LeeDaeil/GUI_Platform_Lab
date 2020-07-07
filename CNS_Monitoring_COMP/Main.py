import sys
import time
import datetime
import pandas as pd
import os

from PySide2.QtWidgets import QApplication, QWidget, QMainWindow, QMessageBox, QRadioButton
from PySide2.QtCore import *
from PySide2.QtGui import *

# GUI FILE
from CNS_Monitoring_COMP.interface.MainWinCOMP import Ui_MainWindow

# IMPORT FUNCTION
from COMMON.UiFunction import *

class Mainwindow(QMainWindow):
    def __init__(self, mem):
        super().__init__()
        self.setWindowFlags(Qt.WindowStaysOnTopHint)

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ANdb = read_ANdb()

        # Save info
        self.show()


if __name__ == '__main__':
    # test for interface
    app = QApplication(sys.argv)
    w = Mainwindow(None)
    sys.exit(app.exec_())