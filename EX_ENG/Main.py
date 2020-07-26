# Sys import
import sys
import os
import pandas as pd
import random

# Qt lib
from PySide2.QtWidgets import QApplication, QWidget, QMainWindow, QHeaderView, QTableWidgetItem, QMessageBox, QCheckBox, \
    QGridLayout
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtPrintSupport import *


# GUI file
from EX_ENG.interface.MainWin import Ui_MainWindow

# Import Function


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # DB check
        self.DBCkeck()

        # Show interface
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # 버튼
        self.ui.CallPrint.clicked.connect(self.CallPrint)
        self.ui.CallMakeDB.clicked.connect(self.CallMakeDB)
        self.ui.CallSend.clicked.connect(self.CallSend)
        self.ui.CallShowAns.clicked.connect(self.CallShowAns)
        self.ui.CallExit.clicked.connect(self.CallExit)

        # DIS
        self.DISUpdate()
        self.SendCount = 0
        self.ShowAnsCount = 0
        self.show()

    def DBCkeck(self):
        if os.path.isfile('Db.csv'):    # 파일 확인
            # 있으면 DB 업데이트
            self.DB = pd.read_csv('Db.csv')
        else:
            # 없으면 DB 파일 작성
            self.DB = pd.DataFrame(data=[[1, 2, 3, 4]], columns=['K', 'E', 'K_prob', 'E_prob'])
            self.DB.to_csv('Db.csv', index=False)   # index false 해야 unnamed가 없어짐.
        print(self.DB)
        pass

    def DISUpdate(self):
        self.ui.lineEdit.setText('-1')
        self.UpdateTable(nub=int(self.ui.lineEdit.text()))
        pass

    def UpdateOneCell(self, nub_label, row_c, ansmode=0):
        get_db_line = self.DB.iloc[nub_label]
        self.ui.DB_Tabel.setItem(row_c, 0, QTableWidgetItem(str(get_db_line.name)))
        if ansmode == 0:
            type_nub = random.randint(0, 2)  # 0 Ko, 1: eng
            if type_nub == 1:
                self.ui.DB_Tabel.setItem(row_c, 1, QTableWidgetItem(str(get_db_line['K'])))
                self.ui.DB_Tabel.setItem(row_c, 2, QTableWidgetItem(str(get_db_line['E'][0:2])))
            else:
                self.ui.DB_Tabel.setItem(row_c, 1, QTableWidgetItem(str('')))
                self.ui.DB_Tabel.setItem(row_c, 2, QTableWidgetItem(str(get_db_line['E'])))
        elif ansmode == 1:
            type_nub = int(self.ui.DB_Tabel.item(row_c, 3).text())
            if type_nub == 1:
                self.ui.DB_Tabel.setItem(row_c, 1, QTableWidgetItem(str(get_db_line['K'])))
                self.ui.DB_Tabel.setItem(row_c, 2, QTableWidgetItem(str(get_db_line['E'][0:2])))
            else:
                self.ui.DB_Tabel.setItem(row_c, 1, QTableWidgetItem(str('')))
                self.ui.DB_Tabel.setItem(row_c, 2, QTableWidgetItem(str(get_db_line['E'])))
        elif ansmode == 2:
            type_nub = int(self.ui.DB_Tabel.item(row_c, 3).text())
            self.ui.DB_Tabel.setItem(row_c, 1, QTableWidgetItem(str(get_db_line['K'])))
            self.ui.DB_Tabel.setItem(row_c, 2, QTableWidgetItem(str(get_db_line['E'])))

        self.ui.DB_Tabel.setItem(row_c, 3, QTableWidgetItem(str(type_nub)))
        self.ui.DB_Tabel.setCellWidget(row_c, 4, CheckBOX())

    def UpdateTable(self, nub=int(1)):
        self.ui.DB_Tabel.clear()

        RowCount,  ColumnCount = 0, 0
        # 테이블 모양 선정
        if nub == -1: # All db show
            RowCount, ColumnCount, ColumnLabel = len(self.DB), len(self.DB.keys()) + 1, ["Nub"] + list(self.DB.keys())
        else:
            nub = nub if nub < len(self.DB) else len(self.DB)  # DB의 크기보다 작게 선정
            RowCount, ColumnCount, ColumnLabel = nub, 5, ["Nub", "K", "E", "Type", "Check"]

        # 테이블 모양 업데이트
        self.ui.DB_Tabel.setRowCount(RowCount)
        self.ui.DB_Tabel.setColumnCount(ColumnCount)
        self.ui.DB_Tabel.setHorizontalHeaderLabels(ColumnLabel)
        # 크기 조절
        header_in_table = self.ui.DB_Tabel.horizontalHeader()
        header_in_table.resizeSection(0, 10)
        header_in_table.setSectionResizeMode(0, QHeaderView.Fixed)
        header_in_table.setSectionResizeMode(1, QHeaderView.Stretch)
        header_in_table.setSectionResizeMode(2, QHeaderView.Stretch)
        header_in_table.setSectionResizeMode(3, QHeaderView.ResizeToContents)
        header_in_table.setSectionResizeMode(4, QHeaderView.ResizeToContents)

        # DB를 테이블에 업데이트
        if nub == -1: # All db show
            row_c = 0
            for K, E, K_prob, E_prob in zip(self.DB["K"], self.DB["E"], self.DB["K_prob"], self.DB["E_prob"]):
                self.ui.DB_Tabel.setItem(row_c, 0, QTableWidgetItem(str(row_c)))
                self.ui.DB_Tabel.setItem(row_c, 1, QTableWidgetItem(K))
                self.ui.DB_Tabel.setItem(row_c, 2, QTableWidgetItem(E))
                self.ui.DB_Tabel.setItem(row_c, 3, QTableWidgetItem(str(K_prob)))
                self.ui.DB_Tabel.setItem(row_c, 4, QTableWidgetItem(str(E_prob)))
                row_c += 1
        else:
            # TODO
            #  랜덤 픽 말고 확률적으로 선택하도록 만들어야함.
            # 값 선택
            want_select = nub
            self.nub_label = []
            rand_nub = random.randint(0, len(self.DB) - 1)
            for i in range(nub):
                while rand_nub in self.nub_label:
                    rand_nub = random.randint(0, len(self.DB) - 1)
                self.nub_label.append(rand_nub)
            print(self.nub_label)

            # 선택된 Nub의 값 출력
            row_c = 0
            for nub_label in self.nub_label:
                self.UpdateOneCell(nub_label=nub_label, row_c=row_c, ansmode=0)
                row_c += 1

    def CallPrint(self):
        dialog = QPrintPreviewDialog()
        dialog.paintRequested.connect(self.CallPrintPage)
        dialog.exec_()
        pass

    def CallPrintPage(self, printer):
        painter = QPainter()
        painter.setRenderHint(QPainter.Antialiasing)
        painter.begin(printer)
        screen = self.ui.DB_Tabel.grab()
        painter.drawPixmap(10, 10, screen)
        painter.end()
        pass

    def CallMakeDB(self):
        self.UpdateTable(nub=int(self.ui.lineEdit.text()))
        self.SendCount = 0
        self.ShowAnsCount = 0

    def CallSend(self):
        nub = int(self.ui.lineEdit.text())
        if nub == -1 and self.ui.DB_Tabel.rowCount() == len(self.DB):
            # self.DB.loc[0]['K']
            for i in range(len(self.DB)):
                self.DB.loc[i] = [self.ui.DB_Tabel.item(i, 1).text(), self.ui.DB_Tabel.item(i, 2).text(),
                                  float(self.ui.DB_Tabel.item(i, 3).text()), float(self.ui.DB_Tabel.item(i, 4).text())]
            msg = QMessageBox(self, text="DB 업데이트")
            msg.show()
        else:
            if self.SendCount == 0:
                for i in range(self.ui.DB_Tabel.rowCount()):
                    nub_in_db = int(self.ui.DB_Tabel.item(i, 0).text())
                    type_in_db = int(self.ui.DB_Tabel.item(i, 3).text())
                    check_info = self.ui.DB_Tabel.cellWidget(i, 4).Comb.checkState()
                    if check_info == Qt.Checked:
                        if type_in_db == 0:
                            self.DB.iloc[nub_in_db, 2] = self.DB.iloc[nub_in_db, 2] + 0.01
                        else:
                            self.DB.iloc[nub_in_db, 3] = self.DB.iloc[nub_in_db, 3] + 0.01
                    else:
                        if type_in_db == 0:
                            self.DB.iloc[nub_in_db, 2] = self.DB.iloc[nub_in_db, 2] - 0.01
                        else:
                            self.DB.iloc[nub_in_db, 3] = self.DB.iloc[nub_in_db, 3] - 0.01
                msg = QMessageBox(self, text="Prob 업데이트")
                msg.show()
                self.SendCount += 1
            else:
                msg = QMessageBox(self, text="Prob 업데이트 이미 수행함.")
                msg.show()
        print(self.DB)

    def CallShowAns(self):
        self.ShowAnsCount = 1 if self.ShowAnsCount == 0 else 0
        # 선택된 Nub의 값 출력
        row_c = 0
        for nub_label in self.nub_label:
            self.UpdateOneCell(nub_label=nub_label, row_c=row_c, ansmode=self.ShowAnsCount + 1)
            row_c += 1
        pass

    def CallExit(self):
        self.close()

    def closeEvent(self, e):
        # 종료
        self.DB.to_csv('Db.csv', index=False)   # index false 해야 unnamed가 없어짐.


class CheckBOX(QWidget):
    def __init__(self):
        super().__init__()
        self.Comb = QCheckBox()
        self.QHLayer = QGridLayout()
        self.QHLayer.setAlignment(Qt.AlignCenter)
        self.QHLayer.addWidget(self.Comb)
        self.QHLayer.setContentsMargins(0, 0, 0, 0)
        self.setLayout(self.QHLayer)

    def mousePressEvent(self, e):
        if self.Comb.checkState() == Qt.Checked:
            self.Comb.setCheckState(Qt.Unchecked)
        else:
            self.Comb.setCheckState(Qt.Checked)


if __name__ == '__main__':
    # test for interface
    app = QApplication(sys.argv)
    w = MainWindow()
    sys.exit(app.exec_())






















