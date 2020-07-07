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

        self.setWindowTitle('F1:입력 변수 체크, F2:입력 변수 찾기, F3: 뒤로 검토 F4: 앞으로 검토, F5 그림 붙이기')

        self.checkVal = 0

        # Make DB
        self.db = self.make_db()
        if os.path.isfile('Andb.txt'):
            self.ANdb = {}
            with open('Andb.txt', 'r') as f:
                while True:
                    temp = f.readline().split('\n')[0].split('\t')
                    if temp[0] == '':
                        break
                    self.ANdb[temp[0]] = {
                        'SYS': temp[1], 'TYPE': temp[2], 'ONECONT': temp[3], 'OnManOpen': temp[4],
                        'OffAutoClose': temp[5], 'Purpose': temp[6]
                    }

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
        if e.key() == Qt.Key_F2 or e.key() == Qt.Key_F3 or e.key() == Qt.Key_F4:
            if e.key() == Qt.Key_F3 or e.key() == Qt.Key_F4:

                if e.key() == Qt.Key_F4:
                    self.checkVal += 1
                else:
                    self.checkVal -= 1

                if self.checkVal >= len(self.ANdb.keys()):
                    self.checkVal = len(self.ANdb.keys())-1
                if self.checkVal < 0:
                    self.checkVal = 0

                one_key_pa = list(self.ANdb.keys())[self.checkVal]
                self.ui.ID_input.setText(one_key_pa)

                print(self.checkVal)
                # Load PARA
                if self.ui.ID_input.text() in self.ANdb.keys():
                    print('Ok! Load')
                    print(self.ANdb)
                    self.check_nub(self.ui.Sys, self.ANdb[self.ui.ID_input.text()]['SYS'])
                    self.check_nub(self.ui.Type_bu, self.ANdb[self.ui.ID_input.text()]['TYPE'])
                    self.check_nub(self.ui.ID_0, self.ANdb[self.ui.ID_input.text()]['ONECONT'])
                    self.ui.ID_input_2.setText(self.ANdb[self.ui.ID_input.text()]['OnManOpen'])
                    self.ui.ID_input_3.setText(self.ANdb[self.ui.ID_input.text()]['OffAutoClose'])
                    self.ui.ID_input_4.setText(self.ANdb[self.ui.ID_input.text()]['Purpose'])

                    if self.ui.ID_input.text() in self.db.keys():
                        self.ui.Des_out.setText(self.db[self.ui.ID_input.text()])
                        self.ui.Des_out.setStyleSheet('color: rgb(9, 93, 0);')
                        self.ui.label_2.setStyleSheet('color: rgb(9, 93, 0);')
                        self.ui.label_3.setStyleSheet('color: rgb(9, 93, 0);')

                else:
                    print('No para')
                    self.ui.Des_out.setText('No PARA in ANdb =============')
                    self.ui.Des_out.setStyleSheet('color: rgb(255, 0, 0);')
                    self.ui.label_2.setStyleSheet('color: rgb(0, 0, 0);')
                    self.ui.label_3.setStyleSheet('color: rgb(0, 0, 0);')

            else:
                # Load PARA
                if self.ui.ID_input.text() in self.ANdb.keys():
                    print('Ok! Load')
                    print(self.ANdb)
                    self.check_nub(self.ui.Sys, self.ANdb[self.ui.ID_input.text()]['SYS'])
                    self.check_nub(self.ui.Type_bu, self.ANdb[self.ui.ID_input.text()]['TYPE'])
                    self.check_nub(self.ui.ID_0, self.ANdb[self.ui.ID_input.text()]['ONECONT'])
                    self.ui.ID_input_2.setText(self.ANdb[self.ui.ID_input.text()]['OnManOpen'])
                    self.ui.ID_input_3.setText(self.ANdb[self.ui.ID_input.text()]['OffAutoClose'])
                    self.ui.ID_input_4.setText(self.ANdb[self.ui.ID_input.text()]['Purpose'])

                    if self.ui.ID_input.text() in self.db.keys():
                        self.ui.Des_out.setText(self.db[self.ui.ID_input.text()])
                        self.ui.Des_out.setStyleSheet('color: rgb(9, 93, 0);')
                        self.ui.label_2.setStyleSheet('color: rgb(9, 93, 0);')
                        self.ui.label_3.setStyleSheet('color: rgb(9, 93, 0);')

                else:
                    print('No para')
                    self.ui.Des_out.setText('No PARA in ANdb =============')
                    self.ui.Des_out.setStyleSheet('color: rgb(255, 0, 0);')
                    self.ui.label_2.setStyleSheet('color: rgb(0, 0, 0);')
                    self.ui.label_3.setStyleSheet('color: rgb(0, 0, 0);')

            # Load img
            self.ui.Des_img.setAlignment(Qt.AlignCenter)
            if os.path.isfile(f'Img_fold/{self.ui.ID_input.text()}.png'):
                self.ui.Des_img.setPixmap(QPixmap(f'Img_fold/{self.ui.ID_input.text()}.png'))
            else:
                self.ui.Des_img.setPixmap(None)  # remove img

        if e.key() == Qt.Key_F1:
            # ID
            if self.ui.ID_input.text() in self.db.keys():
                self.ui.Des_out.setText(self.db[self.ui.ID_input.text()])
                self.ui.Des_out.setStyleSheet('color: rgb(9, 93, 0);')
            else:
                self.ui.Des_out.setText('No PARA =============')
                self.ui.Des_out.setStyleSheet('color: rgb(255, 0, 0);')

            # Automatic fill
            if self.ui.ID_input_2.text() == '' and self.ui.ID_input_3.text() == '':
                self.ui.ID_input_2.setText('KSWO')
                self.ui.ID_input_3.setText('KSWO')
            if self.ui.ID_yes.isChecked():
                self.ui.ID_input_3.setText(self.ui.ID_input_2.text())

            # Check Control val
            if self.ui.ID_input_2.text() in self.db.keys():
                self.ui.label_2.setStyleSheet('color: rgb(9, 93, 0);')
            else:
                self.ui.label_2.setStyleSheet('color: rgb(255, 0, 0);')
            if self.ui.ID_input_3.text() in self.db.keys():
                self.ui.label_3.setStyleSheet('color: rgb(9, 93, 0);')
            else:
                self.ui.label_3.setStyleSheet('color: rgb(255, 0, 0);')

        if e.key() == Qt.Key_F5:
            temp = QApplication.clipboard()
            if not temp.image().isNull():
                pixmap = QPixmap(temp.image())
                self.ui.Des_img.setAlignment(Qt.AlignCenter)
                self.ui.Des_img.setPixmap(pixmap)

    # SAVE
    def Save_info(self):
        print('save')
        if not self.ui.ID_input.text() == '':
            getPara = self.ui.ID_input.text()
            self.ANdb[self.ui.ID_input.text()] = {
                'SYS': self.get_nub(frame=self.ui.Sys),
                'TYPE': self.get_nub(frame=self.ui.Type_bu),
                'ONECONT': self.get_nub(frame=self.ui.ID_0),
                'OnManOpen': self.ui.ID_input_2.text(),
                'OffAutoClose': self.ui.ID_input_3.text(),
                'Purpose': self.ui.ID_input_4.text(),
            }
            self.ui.ID_input.setText('')
            self.ui.ID_input_2.setText('')
            self.ui.ID_input_3.setText('')
            self.ui.ID_input_4.setText('')

            # Save img
            if not self.ui.Des_img.pixmap() == None:
                getPixMap = self.ui.Des_img.pixmap()
                getPixMap.save(f'Img_fold/{getPara}.png')   # save img
                self.ui.Des_img.setPixmap(None)             # remove img

    def get_nub(self, frame):
        fin_nub, iter_nub = 0, 0
        for child in frame.children():
            if type(child) is type(QRadioButton()):
                if child.isChecked():
                    fin_nub = iter_nub
                iter_nub += 1
        return fin_nub

    def check_nub(self, frame, nub):
        nub = int(nub)
        fin_nub, iter_nub = 0, 0
        for child in frame.children():
            if type(child) is type(QRadioButton()):
                if nub == iter_nub:
                    child.setChecked(True)
                iter_nub += 1

    # END FILE
    def end_file_and_save(self):
        with open('Andb.txt', 'w') as f:
            for key in self.ANdb.keys():
                f.write('{}\t{}\t{}\t{}\t{}\t{}\t{}\n'.format(key, self.ANdb[key]['SYS'], self.ANdb[key]['TYPE'],
                                                          self.ANdb[key]['ONECONT'],self.ANdb[key]['OnManOpen'],
                                                          self.ANdb[key]['OffAutoClose'], self.ANdb[key]['Purpose']))
        print("Save_file")
        sys.exit()

if __name__ == '__main__':
    # test for interface
    app = QApplication(sys.argv)
    w = Mainwindow(None)
    sys.exit(app.exec_())