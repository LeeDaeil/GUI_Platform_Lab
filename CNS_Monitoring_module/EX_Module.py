import multiprocessing
from time import sleep

import pandas as pd
import copy
import numpy as np
from CNS_Monitoring_module.EX_CNS_Send_UDP import CNS_Send_Signal
from CNS_Monitoring_module.EX_NetworkTool import NetTool

TEST_FOR_LOAD = False

class EX_module(multiprocessing.Process):
    def __init__(self, mem):
        multiprocessing.Process.__init__(self)

        self.mem = mem[0]           # main mem connection
        self.Act_list = mem[1]      # main mem connection
        self.NET_OUT = mem[2]       # main mem connection
        self.NET_OUT_COPY = copy.deepcopy(self.NET_OUT)
        self.trig_mem = mem[-1]     # main mem connection

        with open('EX_pro.txt', 'r') as f:
            self.cns_ip, self.cns_port = f.read().split('\t')  # [cns ip],[cns port]
        self.CNS_udp = CNS_Send_Signal(self.cns_ip, int(self.cns_port))

    def send_action_append(self, pa, va):
        for _ in range(len(pa)):
            self.para.append(pa[_])
            self.val.append(va[_])

    def send_action(self, R_A):
        R_A=0
        # 전송될 변수와 값 저장하는 리스트
        self.para = []
        self.val = []

        Load_setpoint = self.mem['KBCDO22']['V']
        # Load_setpoint = self.mem['KBCDO20']['V']
        Mismatch = self.mem['ZINST15']['V']
        Down_LOAD = self.mem['KSWO224']['V']
        UP_LOAD = self.mem['KSWO225']['V']

        # if Mismatch > 0:
        #     if 840 < Load_setpoint:
        #         self.send_action_append(['KSWO224', 'KSWO225'], [1, 0]) # down
        # else:
        #     self.send_action_append(['KSWO224', 'KSWO225'], [0, 0])  # stay
        #
        self.send_action_append(['KSWO228', 'KSWO29'], [1, 1])  # Man
        if Mismatch > 0:
            if self.mem['KCNTOMS']['V'] < 2000:
                if 840 < Load_setpoint:
                    print('B')
                    self.send_action_append(['KSWO229', 'KSWO230'], [1, 0]) # down
            if self.mem['KCNTOMS']['V'] > 4000:
                if Load_setpoint < 900:
                    print('A')
                    self.send_action_append(['KSWO229', 'KSWO230'], [0, 1]) # Up
        else:
            self.send_action_append(['KSWO229', 'KSWO223'], [0, 0])  # stay

        if Mismatch < 0:
            self.send_action_append(['KSWO33', 'KSWO32'], [0, 1])  # In
        elif Mismatch >= 0.1:
            self.send_action_append(['KSWO33', 'KSWO32'], [1, 0])  # Out
        else:
            self.send_action_append(['KSWO33', 'KSWO32'], [0, 0])  # Stay

        print(self.mem['KCNTOMS']['V'], Mismatch, Load_setpoint)

        # if R_A == 0:
        #     self.send_action_append(['KSWO33', 'KSWO32'], [0, 0])  # Stay
        # elif R_A == 1:
        #     self.send_action_append(['KSWO33', 'KSWO32'], [1, 0])  # Out
        # elif R_A == 2:
        #     self.send_action_append(['KSWO33', 'KSWO32'], [0, 1])  # In
        #
        # elif R_A == 3:
        #     self.send_action_append(['KSWO97', 'KSWO77'], [1, 1])  # Pump On - Make-up
        # elif R_A == 4:
        #     self.send_action_append(['KSWO97', 'KSWO76'], [0, 1])  # Pump off - Auto
        # elif R_A == 5:
        #     self.send_action_append(['KSWO97', 'KSWO75'], [1, 1])  # Pump off - Boric


        self.CNS_udp._send_control_signal(self.para, self.val)

    def run(self):
        get_nub_act_list = len(self.Act_list)
        input_windows = []

        # Call NetToolBox
        NetToolBox = NetTool()

        while True:
            if self.trig_mem['Loop'] and self.trig_mem['Run']:
                print('계산중....', end='\t')
                ##
                # input_windows.append(NetToolBox.make_input_window(self.mem)[0])
                # if len(input_windows) > 10:
                #     input_windows = input_windows[1:]
                #     out = NetToolBox.NetBox.predict(np.array([input_windows]))
                    # self.NET_OUT['Net_1'].append(out)
                    # print(out)
                #
                ##
                get_input = np.array(NetToolBox.make_input_window_ST(nub=0, db=self.mem))
                # NetBox return (1, 5) shape -> [0] -> (5)
                self.NET_OUT_COPY['Net_0'] = NetToolBox.NetBox[0].predict(get_input)[0]

                get_input = np.array(NetToolBox.make_input_window_ST(nub=1, db=self.mem))
                self.NET_OUT_COPY['Net_1'] = NetToolBox.NetBox[1].predict(get_input)[0]

                get_input = np.array(NetToolBox.make_input_window_ST(nub=2, db=self.mem))
                self.NET_OUT_COPY['Net_2'] = NetToolBox.NetBox[2].predict(get_input)[0]

                get_input = np.array(NetToolBox.make_input_window_ST(nub=3, db=self.mem))
                self.NET_OUT_COPY['Net_3'] = NetToolBox.NetBox[3].predict(get_input)[0]

                get_input = np.array(NetToolBox.make_input_window_ST(nub=4, db=self.mem))
                self.NET_OUT_COPY['Net_4'] = NetToolBox.NetBox[4].predict(get_input)[0]

                get_input = np.array(NetToolBox.make_input_window_ST(nub=5, db=self.mem))
                self.NET_OUT_COPY['Net_5'] = NetToolBox.NetBox[5].predict(get_input)[0]

                get_input = np.array(NetToolBox.make_input_window_ST(nub=6, db=self.mem))
                self.NET_OUT_COPY['Net_6'] = NetToolBox.NetBox[6].predict(get_input)[0]

                get_input = np.array(NetToolBox.make_input_window_ST(nub=7, db=self.mem))
                self.NET_OUT_COPY['Net_7'] = NetToolBox.NetBox[7].predict(get_input)[0]

                get_input = np.array(NetToolBox.make_input_window_ST(nub=8, db=self.mem))
                self.NET_OUT_COPY['Net_8'] = NetToolBox.NetBox[8].predict(get_input)[0]

                self.NET_OUT_COPY['Net_Count'] += 1

                # Update NET_OUT memory
                for NET_OUT_key in self.NET_OUT_COPY.keys():
                    self.NET_OUT[NET_OUT_key] = self.NET_OUT_COPY[NET_OUT_key]

                ##
                print('계산 종료! ....', end='\t')
                print(self, self.mem['KCNTOMS'], self.Act_list, self.trig_mem['Loop'], self.trig_mem['Run'])
                self.trig_mem['Run'] = False