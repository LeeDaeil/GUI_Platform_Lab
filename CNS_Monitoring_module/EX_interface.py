import sys
import multiprocessing
import time
import pandas as pd

from PySide2.QtWidgets import QApplication, QWidget

from CNS_Monitoring_module.EX_CNS_Send_UDP import *

# GUI FILE
from CNS_Monitoring_module.Interface_ui.ui_mainform import Ui_MainWindow

# IMPORT FUNCTION
from CNS_Monitoring_module.ui_function import *

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

        print('Test UI 호출')
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

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

            # ==========================================================================================================
            UIFunction_CLICK.initial_cond(self, self.mem)
            self.CHART_0 = UIFunction_CHART(parent=self.ui.GP_0_1, title='A1', label=['Normal',
                                                                                      'LOCA', 'SGTR', 'MSLB', 'MFLB'])
            # self.CHART_1 = UIFunction_CHART(parent=self.ui.GP_0_2, title='A2', label=['Normal',
            #                                                                           'LOCA', 'SGTR', 'MSLB', 'MFLB'])
            # self.CHART_2 = UIFunction_CHART(parent=self.ui.GP_0_3, title='A3', label=['Normal',
            #                                                                           'LOCA', 'SGTR', 'MSLB', 'MFLB'])
            # self.CHART_3 = UIFunction_CHART(parent=self.ui.GP_0_4, title='A4', label=['Normal',
            #                                                                           'LOCA', 'SGTR', 'MSLB', 'MFLB'])
            # self.CHART_4 = UIFunction_CHART(parent=self.ui.GP_0_5, title='A5', label=['Normal',
            #                                                                           'LOCA', 'SGTR', 'MSLB', 'MFLB'])
            #
            # # >> FUNCTION
            self.ui.Content_menu_empty_0.clicked.connect(lambda: UIFunction_CLICK.toggleMenu(self, 300, True))
            self.ui.Ini_setting.clicked.connect(lambda: UIFunction_CLICK.setInitialCondition(self, self.CNS_udp, True))
            self.ui.Mal_setting.clicked.connect(lambda: UIFunction_CLICK.setMalCondition(self, self.CNS_udp, True))
            # ==========================================================================================================
            timer = QtCore.QTimer(self)
            for _ in [self.update_plot]:
                timer.timeout.connect(_)
            timer.start(300)
        self.show()

    def call_cns_udp_sender(self):
        # CNS 정보 읽기
        with open('EX_pro.txt', 'r') as f:
            self.cns_ip, self.cns_port = f.read().split('\t')   # [cns ip],[cns port]
        self.CNS_udp = CNS_Send_Signal(self.cns_ip, int(self.cns_port))

    def run_cns(self):
        if self.ui.Run.isChecked():
            self.trig_mem['Loop'] = True
        else:
            self.trig_mem['Loop'] = False

    def update_plot(self):
        # display power
        power = self.mem['QPROREL']['V']*100
        self.ui.Top_width_emp.setText(f'Reactor Power : {power:.2f}[%]')
        # Draw Chart
        if self.NET_OUT['Net_Count'] != 0:
            for _ in range(5):
                self.CHART_0.appendXYValue(line_nub=_, x=self.NET_OUT['Net_Count'], y=self.NET_OUT['Net_0'][_])
                # self.CHART_1.appendXYValue(line_nub=_, x=self.NET_OUT['Net_Count'], y=self.NET_OUT['Net_1'][_])
                # self.CHART_2.appendXYValue(line_nub=_, x=self.NET_OUT['Net_Count'], y=self.NET_OUT['Net_2'][_])
        pass

if __name__ == '__main__':
    # test for interface
    app = QApplication(sys.argv)
    w = Mainwindow(None)
    sys.exit(app.exec_())