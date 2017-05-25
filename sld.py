import sys
import numpy
import PyQt5.QtGui
from PyQt5.QtCore import Qt
#import PyQt5.Qt
from PyQt5.Qt import pyqtSignal
from PyQt5.QtWidgets import *


class widget_sld(QTabWidget):
    print('widget_sld')

    def __init__(self, parent=None):
        super(widget_sld, self).__init__(parent)
        n = 0
        v = 1
        for i in spisok_sld:
            self.addTab(i,'sld' + str(n))
            if n<9:
                i.setValue(v)
                v += 1250
            elif n==9:
                v = 10000
                i.setValue(v)
            else:
                v -=1250
                i.setValue(v)
            n+=1

class sld(QSlider):
    my_signal = pyqtSignal(list)

    def __init__(self, data = []):
        super(sld, self).__init__(Qt.Horizontal)
        self.setMinimum(1)
        self.setMaximum(10000)
        self.lcd = QLCDNumber(self)
        self.valueChanged.connect(self.lcd.display)
        self.valueChanged.connect(self.update_sld)
        self.my_signal.connect(self.update_sld)

    def update_sld(self, data=[]):
        pass

class cl_sld1(sld):

    def update_sld(self, data = []):
        self.sld_value = self.value()
        self.sld_value = self.sld_value/10000
        #print(self.sld_value)
        return self.sld_value


sld1 = cl_sld1()
sld2 = cl_sld1()
sld3 = cl_sld1()
sld4 = cl_sld1()
sld5 = cl_sld1()
sld6 = cl_sld1()
sld7 = cl_sld1()
sld8 = cl_sld1()
sld9 = cl_sld1()
sld10 = cl_sld1()
sld11 = cl_sld1()
sld12 = cl_sld1()
sld13 = cl_sld1()
sld14 = cl_sld1()
sld15 = cl_sld1()
sld16 = cl_sld1()
sld17 = cl_sld1()

spisok_sld = [sld1,sld1,sld3,sld4,sld5,sld6,
              sld6,sld7,sld8,sld9,sld10,sld11,
              sld12,sld13,sld14,sld15,sld16,sld17]
'''
self.sld1 = cl_sld1()
self.sld2 = cl_sld1()
self.sld3 = cl_sld1()
self.sld4 = cl_sld1()
self.sld5 = cl_sld1()
self.sld6 = cl_sld1()
self.sld7 = cl_sld1()
self.sld8 = cl_sld1()
self.sld9 = cl_sld1()
self.sld10 = cl_sld1()
self.sld11 = cl_sld1()
self.sld12 = cl_sld1()
self.sld13 = cl_sld1()
self.sld14 = cl_sld1()
self.sld15 = cl_sld1()
self.sld16 = cl_sld1()
self.sld17 = cl_sld1()

spisok_sld = [self.sld1,self.sld1,self.sld3,self.sld4,self.sld5,self.sld6,
              self.sld6,self.sld7,self.sld8,self.sld9,self.sld10,self.sld11,
              self.sld12,self.sld13,self.sld14,self.sld15,self.sld16,self.sld17]

value1 = float()
value2 = float()
value3 = float()
value4 = float()
value5 = float()
value6 = float()
value7 = float()
value8 = float()
value9 = float()
value10 = float()
value11 = float()
value12 = float()
value13 = float()
value14 = float()
value15 = float()
value16 = float()
value17 = float()

str_value = {'1':value1,'2':value2,'3':value3,'4':value4,'5':value5,'6':value6,
             '7':value7,'8':value8,'9':value9, '10':value10, '11':value11,
             '12':value12,'13':value13,'14':value14,'15':value15, '16': value16,
             '17':value17}

str_value = [value1,value2,value3,value4,value5,value6,
             value7,value8,value9, value10, value11,
             value12,value13,value14,value15, value16,
             value17]
'''