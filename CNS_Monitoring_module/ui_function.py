from PySide2.QtCharts import *
from PySide2.QtWidgets import *
from CNS_Monitoring_module.Main_ONLY_INTERFACE import *


class UIFunction_CLICK(Mainwindow):
    def initial_cond(self, mem):
        self.ui.Line_ini_0.setMaximumHeight(0)
        self.ui.Content_menu_empty_2.setMaximumHeight(55)
        self.ui.Label_mal_0_case.setMaximumHeight(0)  # 20->0
        self.ui.Label_mal_1_nub.setMaximumHeight(0)  # 20->0
        self.ui.Label_mal_2_time.setMaximumHeight(0)  # 20->0
        self.ui.Line_mal_0_case.setMaximumHeight(0)  # 20->0
        self.ui.Line_mal_1_nub.setMaximumHeight(0)  # 20->0
        self.ui.Line_mal_2_time.setMaximumHeight(0)  # 20->0
        self.ui.Mal_setting.setText('Malfunction\nSetting')
        #------------------------------------------------------------------
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

    def toggleMenu(self, maxWidth, enable):
        if enable:
            # Get width
            width_ = self.ui.Content_left.width()
            maxExtend = maxWidth
            standard = 100 #pt

            # Set max width
            if width_ == 100:
                widthExtended = maxExtend
                self.ui.Line_ini_0.setMaximumHeight(20)             # 20->0
                self.ui.Content_menu_empty_2.setMaximumHeight(35)   # 30->5
                self.ui.Label_mal_0_case.setMaximumHeight(20)       # 20->0
                self.ui.Label_mal_1_nub.setMaximumHeight(20)       # 20->0
                self.ui.Label_mal_2_time.setMaximumHeight(20)       # 20->0
                self.ui.Line_mal_0_case.setMaximumHeight(20)       # 20->0
                self.ui.Line_mal_1_nub.setMaximumHeight(20)       # 20->0
                self.ui.Line_mal_2_time.setMaximumHeight(20)       # 20->0

                self.ui.Mal_setting.setText('Malfunction Setting')

            else:
                widthExtended = standard
                self.ui.Line_ini_0.setMaximumHeight(0)
                self.ui.Content_menu_empty_2.setMaximumHeight(55)
                self.ui.Label_mal_0_case.setMaximumHeight(0)  # 20->0
                self.ui.Label_mal_1_nub.setMaximumHeight(0)  # 20->0
                self.ui.Label_mal_2_time.setMaximumHeight(0)  # 20->0
                self.ui.Line_mal_0_case.setMaximumHeight(0)  # 20->0
                self.ui.Line_mal_1_nub.setMaximumHeight(0)  # 20->0
                self.ui.Line_mal_2_time.setMaximumHeight(0)  # 20->0
                self.ui.Mal_setting.setText('Malfunction\nSetting')

            # Animation
            self.animation = QPropertyAnimation(self.ui.Content_left, b"minimumWidth")
            self.animation.setDuration(100)
            self.animation.setStartValue(width_)
            self.animation.setEndValue(widthExtended)
            self.animation.start()

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


class UIFunction_CHART:
    """
    ex.
    호출
    self.CHART_1 = UIFunction_CHART(parent=self.ui.GP_0_2, title='A2', label=['A', 'B'])
    그래프 값 추가
    self.CHART_0.appendXYValue(line_nub=0, x=self.x_test, y=self.y_test)
    그래프 업데이트
    self.update_CHART(line_nub)

    """

    def __init__(self, parent=None, title='', label=['']):
        self.title = title
        self.label = label
        self.max_line = len(label)

        parent.addWidget(self.makeChartView())
        self.line_series = [QtCharts.QLineSeries() for _ in range(self.max_line)]
        [self.line_series[_].setName(self.label[_]) for _ in range(self.max_line)]
        self.min_max_val = {'max_x':0, 'max_y':1.05, 'min_x':0, 'min_y':0}

        self.line_axis_x = QtCharts.QValueAxis()
        self.line_axis_x.setTickCount(5)
        self.line_axis_y = QtCharts.QValueAxis()
        self.line_axis_y.setTickCount(5)

    def makeChartView(self):
        self.chartCanv = QtCharts.QChart()
        self.chartCanv.setMargins(QtCore.QMargins(0, 0, 0, 0))

        # self.chartCanv.setAnimationOptions(QtCharts.QChart.SeriesAnimations)
        # self.chartCanv.setAnimationOptions(QtCharts.QChart.AllAnimations)
        self.chartCanv.setTitle(self.title)

        self.chartView = QtCharts.QChartView(self.chartCanv)
        self.chartView.setRenderHint(QPainter.Antialiasing)

        size = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        size.setHorizontalStretch(0)
        self.chartView.setSizePolicy(size)



        return self.chartView

    def appendXYValue(self, line_nub, x, y):
        if x == 0:
            self.min_max_val = {'max_x': 0, 'max_y': 0, 'min_x': 0, 'min_y': 0}
            self.line_series[line_nub].clear()

        if len(self.line_series[line_nub].points()) > 0:
            get_point = self.line_series[line_nub].points()[-1]
            if int(get_point.x()) != x:
                self.line_series[line_nub].append(x, y)
                if x >= self.min_max_val['max_x'] * 0.9:
                    self.min_max_val['max_x'] = x * 1.005
                # if y >= self.min_max_val['max_y'] * 0.9:
                #     self.min_max_val['max_y'] = y * 1.1
                self.update_CHART(line_nub)
        else:
            self.line_series[line_nub].append(x, y)
            if x >= self.min_max_val['max_x'] * 0.9:
                self.min_max_val['max_x'] = x * 1.1
            # if y >= self.min_max_val['max_y'] * 0.9:
            #     self.min_max_val['max_y'] = y * 1.005
            self.update_CHART(line_nub)

    def update_CHART(self, line_nub):
        self.chartCanv.removeSeries(self.line_series[line_nub])
        self.chartCanv.removeAxis(self.line_axis_x)
        self.chartCanv.removeAxis(self.line_axis_y)

        self.line_axis_x = QtCharts.QValueAxis()
        self.line_axis_x.setTickCount(5)
        if self.min_max_val['max_x'] > 100:
            self.line_axis_x.setRange(self.min_max_val['max_x']-100, self.min_max_val['max_x'])
        else:
            self.line_axis_x.setRange(self.min_max_val['min_x'], self.min_max_val['max_x'])
        self.line_axis_y = QtCharts.QValueAxis()
        self.line_axis_y.setTickCount(5)
        self.line_axis_y.setRange(self.min_max_val['min_y'], self.min_max_val['max_y'])

        self.chartCanv.addSeries(self.line_series[line_nub])
        self.chartCanv.addAxis(self.line_axis_x, Qt.AlignBottom)
        self.chartCanv.addAxis(self.line_axis_y, Qt.AlignLeft)

        self.line_series[line_nub].attachAxis(self.line_axis_x)
        self.line_series[line_nub].attachAxis(self.line_axis_y)
