import sys
import time
import datetime
import pandas as pd
import multiprocessing
import os

from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *

# GUI FILE
from CNS_Monitoring_COMP.interface.MainWinCOMP import Ui_MainWindow

# IMPORT FUNCTION
from COMMON.UiFunction import *
from CNS_Monitoring_module.EX_CNS_Send_UDP import *


class interface_function(multiprocessing.Process):
    def __init__(self, mem):
        multiprocessing.Process.__init__(self)
        self.mem = mem

    def run(self):
        app = QApplication(sys.argv)
        w = Mainwindow(self.mem)
        sys.exit(app.exec_())


class Mainwindow(QMainWindow):
    def __init__(self, mem):
        super().__init__()
        self.setWindowFlags(Qt.WindowStaysOnTopHint)

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Load ANdb
        self.ANdb = read_ANdb()

        self.ANdbSysInfo = {'0': 0, '1': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0}
        for keyANdb in self.ANdb.keys():
            self.ANdbSysInfo[self.ANdb[keyANdb]['SYS']] += 1
        print(self.ANdbSysInfo)

        # Mem
        if mem == None: # TEST Stay
            pass
        else:
            self.mem = mem[0]       # main mem connection
            self.Act_list = mem[1]  # main mem connection
            self.NET_OUT = mem[2]   # main mem connection
            self.trig_mem = mem[-1] # main mem connection
            # ---- 초기함수 호출
            self.call_cns_udp_sender()
            # ---- 버튼 명령
            self.ui.Run.clicked.connect(self.run_cns)
            # # >> FUNCTION
            # self.ui.Content_menu_empty_0.clicked.connect(lambda: UIFunction_CLICK.toggleMenu(self, 300, True))
            self.ui.Ini_setting.clicked.connect(lambda: self.setInitialCondition(self.CNS_udp, True))
            self.ui.Mal_setting.clicked.connect(lambda: self.setMalCondition(self.CNS_udp, True))
            # ==========================================================================================================
            self.infoInitialNub = 1
            self.infoMalCase = 0
            self.infoMalNub = 0
            self.infoMalTime = 0

            def updateTopBar():
                self.ui.Top_width_output.setText(f'Current Condition: {self.infoInitialNub:3} | '
                                                 f'{self.infoMalCase:2} |'
                                                 f'{self.infoMalNub:8} | '
                                                 f'{self.infoMalTime:4}')

            updateTopBar()

        # Connect button
        self.ui.SysRCS.clicked.connect(lambda: self.UpdateTable(self.ui.SysRCS, 0))
        self.ui.SysCVCS.clicked.connect(lambda: self.UpdateTable(self.ui.SysCVCS, 1))
        self.ui.SysRHR.clicked.connect(lambda: self.UpdateTable(self.ui.SysRHR, 2))
        self.ui.SysMSTB.clicked.connect(lambda: self.UpdateTable(self.ui.SysMSTB, 3))
        self.ui.SysFWS.clicked.connect(lambda: self.UpdateTable(self.ui.SysFWS, 4))
        self.ui.SysCOND.clicked.connect(lambda: self.UpdateTable(self.ui.SysCOND, 5))
        self.ui.SysELEC.clicked.connect(lambda: self.UpdateTable(self.ui.SysELEC, 6))
        self.ui.SysROD.clicked.connect(lambda: self.UpdateTable(self.ui.SysROD, 7))

        timer = QTimer(self)
        for _ in [self.UpdateTableREALTIEM]:
            timer.timeout.connect(_)
        timer.start(300)

        # Save info
        self.show()

    def call_cns_udp_sender(self):
        # CNS 정보 읽기
        with open('EX_pro.txt', 'r') as f:
            self.cns_ip, self.cns_port = f.read().split('\t')  # [cns ip],[cns port]
        self.CNS_udp = CNS_Send_Signal(self.cns_ip, int(self.cns_port))

    def run_cns(self):
        if self.ui.Run.isChecked():
            self.trig_mem['Loop'] = True
        else:
            self.trig_mem['Loop'] = False

    def setInitialCondition(self, CNS_UDP, enable):
        def callWorngMSG():
            worng_int_mgb = QMessageBox()
            worng_int_mgb.setIcon(QMessageBox.Critical)  # 메세지창 내부에 표시될 아이콘
            worng_int_mgb.setText("잘못된 입력 값입니다.")  # 메세지 제목
            worng_int_mgb.exec_()
        def updateTopBar():
            self.ui.Top_width_output.setText(f'Current Condition: {self.infoInitialNub:3} | '
                                             f'{self.infoMalCase:2} |'
                                             f'{self.infoMalNub:8} | '
                                             f'{self.infoMalTime:4}')

        if enable:
            # Check int Val
            if self.ui.Line_ini_0.text().isdigit():
                # is int
                self.infoInitialNub = int(self.ui.Line_ini_0.text())
                updateTopBar()
                # >> Send Initial Condition !! =========================================================================
                self.CNS_udp._send_control_signal(['KFZRUN', 'KSWO277'], [5, self.infoInitialNub])
                # >> ===================================================================================================
                # Clean Txt box
                self.ui.Line_ini_0.setText('')
            else:
                # is not int
                callWorngMSG()
                # Clean Txt box
                self.ui.Line_ini_0.setText('')

    def setMalCondition(self, CNS_UDP, enable):
        def callWorngMSG():
            worng_int_mgb = QMessageBox()
            worng_int_mgb.setIcon(QMessageBox.Critical)  # 메세지창 내부에 표시될 아이콘
            worng_int_mgb.setText("잘못된 입력 값입니다.")  # 메세지 제목
            worng_int_mgb.exec_()
        def updateTopBar():
            self.ui.Top_width_output.setText(f'Current Condition: {self.infoInitialNub:3} | '
                                             f'{self.infoMalCase:2} |'
                                             f'{self.infoMalNub:8} | '
                                             f'{self.infoMalTime:4}')

        if enable:
            # Check int Val
            if self.ui.Line_mal_0_case.text().isdigit() and self.ui.Line_mal_1_nub.text().isdigit() \
                    and self.ui.Line_mal_2_time.text().isdigit():
                # is int
                self.infoMalCase = int(self.ui.Line_mal_0_case.text())
                self.infoMalNub = int(self.ui.Line_mal_1_nub.text())
                self.infoMalTime = int(self.ui.Line_mal_2_time.text())
                updateTopBar()
                # >> Send Mal Condition !! =========================================================================
                CNS_UDP._send_control_signal(['KFZRUN', 'KSWO280', 'KSWO279', 'KSWO278'],
                                             [10, self.infoMalCase, self.infoMalNub, self.infoMalTime])
                # >> ===================================================================================================
                # Clean Txt box
                self.ui.Line_mal_0_case.setText('')
                self.ui.Line_mal_1_nub.setText('')
                self.ui.Line_mal_2_time.setText('')
            else:
                # is not int
                callWorngMSG()
                # Clean Txt box
                self.ui.Line_mal_0_case.setText('')
                self.ui.Line_mal_1_nub.setText('')
                self.ui.Line_mal_2_time.setText('')

    # ============================================================================================================ #

    def UpdateTable(self, radio_ui, sys_nub):
        # remove
        self.UpdateTableValue(sys_nub)
        self.UpdataTableIMG(sys_nub)

    def UpdateTableREALTIEM(self):
        sys_val = 0
        if self.ui.SysRCS.isChecked(): sys_val = 0
        if self.ui.SysCVCS.isChecked(): sys_val = 1
        if self.ui.SysRHR.isChecked(): sys_val = 2
        if self.ui.SysMSTB.isChecked(): sys_val = 3
        if self.ui.SysFWS.isChecked(): sys_val = 4
        if self.ui.SysCOND.isChecked(): sys_val = 5
        if self.ui.SysELEC.isChecked(): sys_val = 6
        if self.ui.SysROD.isChecked(): sys_val = 7
        self.UpdateTableValue(sys_val)
        self.UpdataTableIMG(sys_val)
        self.ui.ShowTable.resizeColumnsToContents()
        self.ui.ShowTable.resizeRowsToContents()

    def UpdateTableValue(self, sys_nub):
        self.ui.ShowTable.clear()

        self.ui.ShowTable.setRowCount(7)
        if self.ANdbSysInfo[str(sys_nub)] % 7 == 0:
            max_col = self.ANdbSysInfo[str(sys_nub)] // 7      # 10개//10 ->1... -> 1
        else:
            max_col = self.ANdbSysInfo[str(sys_nub)]//7 + 1    # 14개//10 ->1... -> 2
        self.ui.ShowTable.setColumnCount(max_col * 4)           # 3열 * n개

        # self.ui.ShowTable.setRowCount(self.ANdbSysInfo[str(sys_nub)])
        # self.ui.ShowTable.setColumnCount(4)
        current_row = 0
        current_col = 0
        for keyANdb in self.ANdb.keys():
            if self.ANdb[keyANdb]['SYS'] == str(sys_nub):
                # Update Value(t-1 = t_0), Value(t = t_1)
                if len(self.mem['KCNTOMS']['D']) == 2:
                    self.ui.ShowTable.setItem(current_row, 1 + current_col, QTableWidgetItem('{:4.2f}'.format(self.mem[keyANdb]['L'][0])))
                    self.ui.ShowTable.setItem(current_row, 2 + current_col, QTableWidgetItem('{:4.2f}'.format(self.mem[keyANdb]['D'][1])))
                elif len(self.mem['KCNTOMS']['D']) == 0:
                    self.ui.ShowTable.setItem(current_row, 1 + current_col, QTableWidgetItem(str(0)))
                    self.ui.ShowTable.setItem(current_row, 2 + current_col, QTableWidgetItem(str(0)))
                else:
                    self.ui.ShowTable.setItem(current_row, 1 + current_col, QTableWidgetItem('{:4.2f}'.format(self.mem[keyANdb]['D'][0])))
                    self.ui.ShowTable.setItem(current_row, 2 + current_col, QTableWidgetItem('{:4.2f}'.format(self.mem[keyANdb]['D'][0])))

                # Update PARANAVE, ICON(Same or Not same)
                if float(self.ui.ShowTable.item(current_row, 1 + current_col).text()) == \
                        float(self.ui.ShowTable.item(current_row, 2 + current_col).text()):
                    ICON_ = QTableWidgetItem(keyANdb)
                    ICON_.setIcon(QIcon("interface/Same.png"))
                else:
                    ICON_ = QTableWidgetItem(keyANdb)
                    ICON_.setIcon(QIcon("interface/NotSame.png"))
                self.ui.ShowTable.setItem(current_row, 0 + current_col, ICON_)

                current_row += 1
                if current_row >= 7:
                    current_row = 0
                    current_col += 4

    def UpdataTableIMG(self, sys_nub):
        current_row = 0
        current_col = 0

        for row in range(0, self.ANdbSysInfo[str(sys_nub)]):
            get_img = QPixmap(f'Img_fold/{self.ui.ShowTable.item(current_row, current_col).text()}.png')
            temp_item = QTableWidgetItem()
            temp_item.setData(Qt.DecorationRole, get_img.scaled(80, 200, Qt.KeepAspectRatio))
            self.ui.ShowTable.setItem(current_row, current_col+3, temp_item)

            current_row += 1
            if current_row >= 7:
                current_row = 0
                current_col += 4


if __name__ == '__main__':
    # test for interface
    app = QApplication(sys.argv)
    w = Mainwindow(None)
    sys.exit(app.exec_())