from PyQt5 import QtWidgets, QtGui, QtCore
import pyqtgraph as pg
import numpy as np

class myplotwidget (pg.PlotWidget) :

    def __init__(self, parent):
        pg.setConfigOption('background', (90,90,90))
        pg.PlotWidget.__init__(self, parent)
        self.setLabel('bottom',"YEAR")
        self.setLabel('left', "VALUE")
        self.setLabel('top',"ScatterPlot")

    def testplot (self) :
        x = np.arange (0,10)+2000
        y = np.arange (0,10)*4.

        self.plot(x,y, pen='y', title='Test Plot')

    def plot_data (self, x, y):
        self.plot(x,y)

    def set_plot_data (self, xarr, yarr):
        self.xarr = xarr
        self.yarr = yarr