import sys
from PyQt5.QtGui import *
from PyQt5.Qt import *
from PyQt5.QtWidgets import *
from PyQt5.Qt import pyqtSignal

import sys
import numpy as np
import math
import PyQt5.QtGui
import Windows.Plot_s
import __def__.trajectory as trag
from math import pi, exp, cos, sin, log10
plot1 = Windows.Plot_s.Plot1()

ai = [
    0.940306193319157, 0.954130733952570,
    0.966193987895793, 0.976461070265884,
    0.984902269883832, 0.991493145379124,
    0.996214604271025, 0.999052964757309,
    1.0,
    0.999052964757309, 0.996214604271025,
    0.991493145379124, 0.984902269883832,
    0.976461070265884, 0.966193987895793,
    0.954130733952570, 0.940306193319157,
]
hamming = [
0.0800000000000000,0.115015415044808,
0.214730880654188,0.363965621112059,
0.540000000000000,0.716034378887941,
0.865269119345812,0.964984584955192,
1.0,
0.964984584955192,0.865269119345812,
0.716034378887941,0.540000000000000,
0.363965621112059,0.214730880654188,
0.115015415044808,0.0800000000000000
]
win = hamming
betta = 1
h = 10000
N = 17

class Dialog_traj(QWidget):
    print('Dialog_traj')
    def __init__(self):
        super().__init__()
        self.resize(1500, 600)                         # Размеры окна.
        self.center()
        self.setWindowTitle('Траектория')              # Нидпись в заголовке.
        # self.setWindowIcon(QIcon('./Icon/edit1'))    # Иконка прложения.
        self.grid()

    def grid(self):
        self.gride = QGridLayout()
        #self.gride.addWidget(TabDemo())
        self.lsd()
        self.sld_n()
        self.sld_tuning()
        self.bt_kaiser   = QPushButton('Kaiser:0')
        self.bt_blackman = QPushButton('Blackman:1')
        self.bt_hamming  = QPushButton('Hamming:2')
        self.bt_hanning  = QPushButton('Hanning:3')
        self.bt_bartlett = QPushButton('Bartlett:4')
        self.gride.addWidget(self.bt_kaiser, *(0,3))
        self.gride.addWidget(self.bt_blackman,*(0,4))
        self.gride.addWidget(self.bt_hamming,*(0,5))
        self.gride.addWidget(self.bt_hanning,*(0,6))
        self.gride.addWidget(self.bt_bartlett,*(0,7))
        self.gride.addWidget(plot1, *(1,3,18,5))
        self.lb  = QLabel('Потери:')
        self.tx  = QLineEdit()
        self.tx1 = QLineEdit()
        self.tx2 = QLineEdit()
        self.tx3 = QLineEdit()
        self.gride.addWidget(self.lb,  *(19,3,1,1))
        self.gride.addWidget(self.tx,  *(19,4,1,1))
        self.gride.addWidget(self.tx1, *(19,5,1,1))
        self.gride.addWidget(self.tx2, *(19,6,1,1))
        self.gride.addWidget(self.tx3, *(19,7,1,1))
        self.setLayout(self.gride)
        self.bt_kaiser.clicked.connect(self.update_bt_kaiser_0)
        self.bt_blackman.clicked.connect(self.update_bt_blackman_1)
        self.bt_hamming.clicked.connect(self.update_bt_hamming_2)
        self.bt_hanning.clicked.connect(self.update_bt_hanning_3)
        self.bt_bartlett.clicked.connect(self.update_bt_bartlett_4)
        win = self.win(N)
        self.poteri_max(win)

    def update_bt_kaiser_0(self):
        print('Kaiser')
        betta = 4.92
        win = list(np.kaiser(N,betta))
        self.poteri_max(win)
        for win,sld_ in zip(win,self.spisok_sld):
            sld_.setValue(int(win*h))
        self.sld_3.setValue(int(betta*h))
        self.sld_3.sliderMoved.connect(self.update_kaiser)

    def update_kaiser(self):
        betta = self.sld_3.value()
        betta = betta/10000
        print(betta)
        win = list(np.kaiser(N,betta))
        self.poteri_max(win)
        self.sld_3.setMaximum(h*10)
        for w,sld in zip(win, self.spisok_sld):
            sld.setValue(int(w*h))

    def update_bt_blackman_1(self):
        print('Blackman')
        win = list(np.blackman(N))
        self.poteri_max(win)
        for win,sld_ in zip(win,self.spisok_sld):
            sld_.setValue(int(win*h))

    def update_bt_hamming_2(self):
        print('Hamming')
        win = list(np.hamming(N))
        self.poteri_max(win)
        for win,sld_ in zip(win,self.spisok_sld):
            sld_.setValue(int(win*h))
        self.sld_1.sliderMoved.connect(self.update_ham)
        self.sld_2.sliderMoved.connect(self.update_ham)

    def update_bt_hanning_3(self):
        print('Hanning')
        win = list(np.hanning(N))
        self.poteri_max(win)
        for win,sld_ in zip(win,self.spisok_sld):
            sld_.setValue(int(win*h))

    def update_bt_bartlett_4(self):
        print('Bartlett')
        win = list(np.bartlett(N))
        self.poteri_max(win)
        for win,sld_ in zip(win,self.spisok_sld):
            sld_.setValue(int(win*h))

    def sld_tuning(self):
        for pos,lcd in zip(self.pos_lb,self.spisok_lcd):
            self.lb = QLabel('#' + str(pos[0]))
            self.gride.addWidget(lcd, *pos)
            self.gride.addWidget(self.lb, *pos)
        win1 = self.win(N)
        win = win1
        win1.append(1)
        win1.append(2)
        win1.append(3)
        pos_sld = [(j,2) for j in range(N+3)]
        for pos,sld_,lcd,w in zip(pos_sld,self.spisok_sld,self.spisok_lcd, win1):
            sld_.sliderMoved.connect(self.update)
            #sld_.setFocusPolicy(Qt.NoFocus)
            sld_.setGeometry(30, 40, 100, 30)
            sld_.valueChanged.connect(lcd.display)
            sld_.setMinimum(0)
            sld_.setMaximum(h)
            sld_.setFocusPolicy(Qt.StrongFocus)
            sld_.setTickPosition(QSlider.TicksBelow)
            sld_.setTickInterval(100)
            sld_.setValue(int(w*h))
            self.gride.addWidget(sld_, *pos)

    def ham(self):
        a = 0.54; b = 1.0 - a
        hamming = self.f_hamming(a,b,N)
        hamming.append(a); hamming.append(b)
        hamming.append(h)
        self.sld_1.sliderMoved.connect(self.update_ham)
        self.sld_2.sliderMoved.connect(self.update_ham)

    def update_ham(self):
        print('update_ham')
        self.value_1 = self.sld_1.value()
        self.value_2 = self.sld_2.value()
        a = self.value_1/h
        b = 1.0 - a
        hamming = self.f_hamming(a,b,N)
        for ham,sld in zip(hamming, self.spisok_sld):
            sld.setValue(int(ham*h))
        self.update()

    def update(self):
        print('update')
        self.sld_value()
        self.ai = []
        for value in self.str_value[:N]:
            value = value/h
            self.ai.append(value)
        self.poteri_max(self.ai)

    def poteri_max(self, list):
        sum_ = sum(list)
        self.tx.setText(str(sum_/N))
        plot1.my_signal_plot.emit(list)
        data_test = trag.traj(list, N)
        data_test1 = data_test[:,0]
        data_test2 = data_test[:,1]
        data_test3 = data_test[:,2]
        x_max = []
        max1 = np.max(data_test3)
        for y,x in zip(data_test3,np.arange(1000.0,0.0,-1.0)):
            if -3.2<y[0][0][0]<-2.8:
                x_max.append(x)
            if y[0]==max1:
                self.tx3.setText('max3:' + '2pi/'+str(int(x)))
        max_x = max(x_max)
        min_x = min(x_max)
        self.tx1.setText('2pi/' + str(min_x))
        self.tx2.setText('2pi/' + str(max_x))

    def lsd(self):
        self.pos_lb = [(j,0) for j in range(N+3)]
        self.lcd_1 = QLCDNumber()
        self.lcd_2 = QLCDNumber()
        self.lcd_3 = QLCDNumber()
        self.lcd1 = QLCDNumber()
        self.lcd2 = QLCDNumber()
        self.lcd3 = QLCDNumber()
        self.lcd4 = QLCDNumber()
        self.lcd5 = QLCDNumber()
        self.lcd6 = QLCDNumber()
        self.lcd7 = QLCDNumber()
        self.lcd8 = QLCDNumber()
        self.lcd9 = QLCDNumber()
        self.lcd10 = QLCDNumber()
        self.lcd11 = QLCDNumber()
        self.lcd12 = QLCDNumber()
        self.lcd13 = QLCDNumber()
        self.lcd14 = QLCDNumber()
        self.lcd15 = QLCDNumber()
        self.lcd16 = QLCDNumber()
        self.lcd17 = QLCDNumber()
        self.spisok_lcd = [self.lcd1 ,self.lcd2 ,self.lcd3 ,self.lcd4 ,self.lcd5 ,self.lcd6 ,self.lcd7,
                           self.lcd8,self.lcd9,self.lcd10, self.lcd11,self.lcd12,self.lcd13,self.lcd14,
                           self.lcd15,self.lcd16,self.lcd17,self.lcd_1,self.lcd_2,self.lcd_3]

    def sld_n(self):
        self.sld_1 = QSlider(Qt.Horizontal)
        self.sld_2 = QSlider(Qt.Horizontal)
        self.sld_3 = QSlider(Qt.Horizontal)
        self.sld1 = QSlider(Qt.Horizontal)
        self.sld2 = QSlider(Qt.Horizontal)
        self.sld3 = QSlider(Qt.Horizontal)
        self.sld4 = QSlider(Qt.Horizontal)
        self.sld5 = QSlider(Qt.Horizontal)
        self.sld6 = QSlider(Qt.Horizontal)
        self.sld7 = QSlider(Qt.Horizontal)
        self.sld8 = QSlider(Qt.Horizontal)
        self.sld9 = QSlider(Qt.Horizontal)
        self.sld10 = QSlider(Qt.Horizontal)
        self.sld11 = QSlider(Qt.Horizontal)
        self.sld12 = QSlider(Qt.Horizontal)
        self.sld13 = QSlider(Qt.Horizontal)
        self.sld14 = QSlider(Qt.Horizontal)
        self.sld15 = QSlider(Qt.Horizontal)
        self.sld16 = QSlider(Qt.Horizontal)
        self.sld17 = QSlider(Qt.Horizontal)
        self.spisok_sld = [self.sld1,self.sld2,self.sld3,self.sld4,self.sld5,self.sld6,self.sld7,
                           self.sld8,self.sld9,self.sld10,self.sld11,self.sld12,self.sld13,self.sld14,
                           self.sld15,self.sld16,self.sld17,self.sld_1,self.sld_2, self.sld_3]

    def sld_value(self):
        self.value_1 = self.sld_1.value()
        self.value_2 = self.sld_2.value()
        self.value_3 = self.sld_3.value()
        self.value1 = self.sld1.value()
        self.value2 = self.sld2.value()
        self.value3 = self.sld3.value()
        self.value4 = self.sld4.value()
        self.value5 = self.sld5.value()
        self.value6 = self.sld6.value()
        self.value7 = self.sld7.value()
        self.value8 = self.sld8.value()
        self.value9 = self.sld9.value()
        self.value10 = self.sld10.value()
        self.value11 = self.sld11.value()
        self.value12 = self.sld12.value()
        self.value13 = self.sld13.value()
        self.value14 = self.sld14.value()
        self.value15 = self.sld15.value()
        self.value16 = self.sld16.value()
        self.value17 = self.sld17.value()
        self.str_value = [self.value1,self.value2,self.value3,self.value4,self.value5,self.value6,
                          self.value7,self.value8,self.value9, self.value10,self.value11,
                          self.value12,self.value13,self.value14,self.value15, self.value16,self.value17,
                          self.value_1, self.value_2, self.value_3]

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def close(self):
        self.close()

    def keyPressEvent(self, e):
        if e.key() == Qt.Key_Escape:
            self.close()
            print('END')
        if e.key() == Qt.Key_O:
            self.FileDialog1()
        if e.key() == Qt.Key_F5:
            print('ai:', self.ai)

    def f_hamming(self,a,b,N):
        ham = [a - b * cos(2*pi*n/(N-1)) for n in range(N)]
        return ham

    def win(self,N):
        kais = np.kaiser(N,0.6)
        kais1 = np.kaiser(N,4.92)
        win = list(kais)
        return win

'''
win = [0.5*(exp(pi)*(sin(((N-1)*pi))/sin(1/2*2*pi)))+0.25*(exp(pi-2*pi/(N-1))*(sin(((N-1)*pi)-2*pi/(N-1))/sin(1/2*2*pi-2*pi/(N-1)))
                                    +exp(pi+2*pi/(N-1))*(sin(((N-1)*pi)+2*pi/(N-1))/sin(1/2*2*pi+2*pi/(N-1)))) for n in range(N)]

win_rimasa = [0.42323 - 0.49755*cos(2.0*pi*n/(N-1))+ 0.07922*cos(4.0*pi*n/(N-1)) for n in range(N)]

win_gaussa = [exp(-0.5*(1*n/N)**2) for n in range(N)]
                                     '''