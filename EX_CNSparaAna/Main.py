import sys
import time
import datetime
import pandas as pd
import os

from PySide2.QtWidgets import QApplication, QWidget, QMainWindow, QMessageBox, QRadioButton
from PySide2.QtCore import *
from PySide2.QtGui import *

# GUI FILE
from EX_CNSparaAna.MainWin import Ui_MainWindow

# IMPORT FUNCTION


class Mainwindow(QMainWindow):
    def __init__(self, mem):
        super().__init__()
        self.setWindowFlags(Qt.WindowStaysOnTopHint)

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Make DB
        self.db = self.make_db()
        if os.path.isfile('Andb.csv'):
            self.ANdb = pd.read_csv('Andb.csv').to_dict()
        else:
            self.ANdb = {}

        # Save info
        self.ui.End_bu.clicked.connect(self.end_file_and_save)
        self.ui.Saveby.clicked.connect(self.Save_info)
        self.show()

    def make_db(self):
        db = {}
        with open('db.txt', 'r') as f:
            while True:
                temp = f.readline().split('\t')
                if temp[0] == '':
                    break
                db[temp[0]] = temp[2]
        return db

    def keyPressEvent(self, e):
        # Find
        if e.key() == Qt.Key_F2:
            # Load PARA
            if self.ui.ID_input.text() in self.ANdb.keys():
                print('Ok! Load')
                self.check_nub(self.ui.Sys, self.ANdb[self.ui.ID_input.text()]['SYS'])
                self.check_nub(self.ui.Type_bu, self.ANdb[self.ui.ID_input.text()]['TYPE'])
                self.check_nub(self.ui.ID_0, self.ANdb[self.ui.ID_input.text()]['ONECONT'])
                self.ui.ID_input_2.setText(self.ANdb[self.ui.ID_input.text()]['OnManOpen'])
                self.ui.ID_input_3.setText(self.ANdb[self.ui.ID_input.text()]['OffAutoClose'])
            else:
                print('No para')
                self.ui.Des_out.setText('No PARA in ANdb =============')
                self.ui.Des_out.setStyleSheet('color: rgb(255, 0, 0);')

        if e.key() == Qt.Key_F1:
            # ID
            if self.ui.ID_input.text() in self.db.keys():
                self.ui.Des_out.setText(self.db[self.ui.ID_input.text()])
                self.ui.Des_out.setStyleSheet('color: rgb(9, 93, 0);')
            else:
                self.ui.Des_out.setText('No PARA =============')
                self.ui.Des_out.setStyleSheet('color: rgb(255, 0, 0);')

            # Check Control val
            if self.ui.ID_input_2.text() in self.db.keys():
                self.ui.label_2.setStyleSheet('color: rgb(9, 93, 0);')
            else:
                self.ui.label_2.setStyleSheet('color: rgb(255, 0, 0);')
            if self.ui.ID_input_3.text() in self.db.keys():
                self.ui.label_3.setStyleSheet('color: rgb(9, 93, 0);')
            else:
                self.ui.label_3.setStyleSheet('color: rgb(255, 0, 0);')

    # SAVE
    def Save_info(self):
        print('save')
        if not self.ui.ID_input.text() == '':
            self.ANdb[self.ui.ID_input.text()] = {
                'SYS': self.get_nub(frame=self.ui.Sys),
                'TYPE': self.get_nub(frame=self.ui.Type_bu),
                'ONECONT': self.get_nub(frame=self.ui.ID_0),
                'OnManOpen': self.ui.ID_input_2.text(),
                'OffAutoClose': self.ui.ID_input_3.text(),
            }

    def get_nub(self, frame):
        fin_nub, iter_nub = 0, 0
        for child in frame.children():
            if type(child) is type(QRadioButton()):
                if child.isChecked():
                    fin_nub = iter_nub
                iter_nub += 1
        return fin_nub

    def check_nub(self, frame, nub):
        fin_nub, iter_nub = 0, 0
        for child in frame.children():
            if type(child) is type(QRadioButton()):
                if nub == iter_nub:
                    child.setChecked(True)
                iter_nub += 1

    # END FILE
    def end_file_and_save(self):
        out = pd.DataFrame(self.ANdb)
        out.to_csv('Andb.csv')
        print("Save_file")
        sys.exit()

if __name__ == '__main__':
    # test for interface
    app = QApplication(sys.argv)
    w = Mainwindow(None)
    sys.exit(app.exec_())