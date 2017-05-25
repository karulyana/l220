from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5 import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure
from matplotlib.ticker import MultipleLocator, FormatStrFormatter, FixedLocator,AutoMinorLocator, NullFormatter
from matplotlib import rcParams
import matplotlib.pyplot as plt
from PyQt5.Qt import pyqtSignal
import __def__._0_read as r
import numpy as np
import math
import __def__.trajectory as trag
from math import pi, exp, cos, sin, log10

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

kaiser = np.kaiser(17,2)


class PlotCanvasData(FigureCanvas):
    my_signal_plot = pyqtSignal(list)

    def __init__(self, data = []):
        print('plot')
        self.N = 17
        #print('PlotCanvasData')
        self.fig = Figure()
        FigureCanvas.__init__(self, self.fig)
        self.fig.set_facecolor('white')
        self.ax = self.fig.add_subplot(111, frameon=True)
        FigureCanvas.updateGeometry(self)
        self.ax.legend()
        self.ax.hold(False)
        self.navig_toolbar = NavigationToolbar(self, self)
        self.my_signal_plot.connect(self.update_plot)
        data_test = trag.traj(ai, self.N)
        data_test1 = data_test[:,0]
        data_test2 = data_test[:,1]
        data_test3 = data_test[:,2]
        max = np.max(data_test3)
        x_max = []
        for y,x in zip(data_test3,np.arange(1000.0,0.0,-1.0)):
            if -3.2<y[0][0][0]<-2.8:
                x_max.append(x)
            if y[0]==max:
                print(y,x)
        #max_x = max(x_max)
        #min_x = min(x_max)
        #d = 2*pi/(max_x - min_x)
        #print(max_x,min_x)
        self.ax.plot(data_test1, 'b-', data_test2, 'r-', data_test3, 'y')
        self.white()


    def my_slot_update(self, data):
        print(data, flush=True)
        self.update_plot()

    def white(self):
        print('white')
        xlabels = self.ax.xaxis.get_ticklabels()
        xlines = self.ax.xaxis.get_ticklines()
        for label in xlines:
            label.set_color('black')
        for label in xlabels:
            label.set_color('black')
        ylabels = self.ax.yaxis.get_ticklabels()
        ylines = self.ax.yaxis.get_ticklines()
        for label in ylines:
            label.set_color('black')
        for label in ylabels:
            label.set_color('black')
        self.ax.patch.set_facecolor('white')
        #self.ax.grid(True, color='black', alpha = 0.5 )
        xax = self.ax.xaxis
        yax = self.ax.yaxis
        majorLocatorX  = FixedLocator(np.arange(1000,0, -50))
        majorFormatterX = FormatStrFormatter('%i')
        minorLocator   = FixedLocator(np.arange(1000,0, -10))
        xax.set_major_locator(majorLocatorX)
        xax.set_major_formatter(majorFormatterX)
        xax.set_minor_locator(minorLocator)
        xax.set_minor_formatter(NullFormatter())
        minorLocator   = MultipleLocator(2.5)
        majorFormatter = FormatStrFormatter('%i')
        majorLocator   = FixedLocator(range(-3,-200,-10))
        yax.set_major_locator(majorLocator)
        yax.set_major_formatter(majorFormatter)
        yax.set_minor_locator(minorLocator)
        yax.set_minor_formatter(NullFormatter())
        self.ax.grid(True, which='major', color='k', linestyle='solid')
        self.ax.grid(True, which='minor', color='grey', linestyle='dashed', alpha=0.5)

    def update_plot(self, data=[]):
        pass

class Plot1(PlotCanvasData):

    def update_plot(self, data=[]):
        print('plot_update1')
        data_test = trag.traj(data, self.N)
        data1 = data_test[:,0]
        data2 = data_test[:,1]
        data3 = data_test[:,2]

        self.ax.plot(data1, 'b-', data2, 'r-', data3, 'y')
        self.white()
        self.draw()
        print('res_plot_1')


class Plot2(PlotCanvasData):

    def update_plot(self, data=[]):
        print('plot_update2')
        data1 = data[0]
        data2 = data[1]
        self.ax.plot(data1, 'b-', data2, 'r-')
        self.white()
        self.draw()
        print('res_plot_2')

class Plot3(PlotCanvasData):

    def update_plot(self, data=[]):
        print('plot_update3')
        data1 = data[0]
        data2 = data[1]
        self.ax.plot(data1, 'b->')#, data2, 'r-')
        self.white()
        self.draw()
        print('res_plot_3')

class Plot4(PlotCanvasData):

    def update_plot(self, data=[]):
        print('plot_update4')
        data1 = data[0]
        data2 = data[1]
        self.ax.plot(data1, 'b-', data2, 'r-')
        self.white()
        self.draw()
        print('res_plot_4')