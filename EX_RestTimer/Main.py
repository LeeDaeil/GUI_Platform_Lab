import sys
import time
import datetime
import pandas as pd

from PySide2.QtWidgets import QApplication, QWidget, QMainWindow, QMessageBox
from PySide2.QtCore import *

# GUI FILE
from EX_RestTimer.Interface.Maininterface import Ui_MainWindow

# IMPORT FUNCTION


class Mainwindow(QMainWindow):
    def __init__(self, mem):
        super().__init__()
        self.setWindowFlags(Qt.WindowStaysOnTopHint)

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.inital_val = [50, 60]
        self.ui.StPoint.setText(f'{self.inital_val[0]}')
        self.ui.EndPoint.setText(f'{self.inital_val[1]}')

        timer = QTimer(self)
        for _ in [self.update_window]:
            timer.timeout.connect(_)
        timer.start(300)
        self.show()

    def update_window(self):
        CurrentTime = [datetime.datetime.now().hour,
                       datetime.datetime.now().minute,
                       datetime.datetime.now().second]

        self.ui.ShowTime.setText(f'{CurrentTime[0]:02}:'
                                 f'{CurrentTime[1]:02}:'
                                 f'{CurrentTime[2]:02}')
        if self.ui.pushButton.isChecked():
            # Check digit
            if not self.ui.StPoint.text().isdigit():
                self.ui.StPoint.setText(f'{self.inital_val[0]}')
            else:
                self.inital_val[0] = int(self.ui.StPoint.text())

            if not self.ui.EndPoint.text().isdigit():
                self.ui.EndPoint.setText(f'{self.inital_val[1]}')
            else:
                self.inital_val[1] = int(self.ui.EndPoint.text())

            # Check logic
            if self.inital_val[0] >= self.inital_val[1]:
                # ERROR
                self.inital_val[1] = self.inital_val[0] + 1
                if self.inital_val[1] > 60:
                    self.inital_val[0] -= 1
                    self.inital_val[1] = self.inital_val[0] + 1
                # Update
                self.ui.StPoint.setText(f'{self.inital_val[0]}')
                self.ui.EndPoint.setText(f'{self.inital_val[0]}')

            # Monitoring !
            if int(self.ui.StPoint.text()) <= CurrentTime[1] < int(self.ui.EndPoint.text()):
                msg = QMessageBox(self)
                msg.setGeometry(400, 500, 100, 100)
                msg.setText(str('Reading Device, Please Wait...'))
                msg.addButton("OK", QMessageBox.YesRole)
                msg.show()
                msg.exec_()



if __name__ == '__main__':
    # test for interface
    app = QApplication(sys.argv)
    w = Mainwindow(None)
    sys.exit(app.exec_())