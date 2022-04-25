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
        self.pen0 = pg.mkPen('r', width=1.5)
        self.pen1 = pg.mkPen('g', width=1.5)



        x = np.arange (0,10)+2000
        y = np.arange (0,10)*4.
        #self.plot(x, y, pen='y', title='Test Plot')


    def set_y (self, yvals):
        self.clear()


        npts = yvals[0].size
        x = np.arange(npts) + 2000
        self.plot(x,yvals[0],pen=self.pen0)
        self.plot(x,yvals[1],pen=self.pen1)
        #self.plot(x,yvals[0],QtGui.QPen(QtCore.Qt.red))
        #self.plot(x,yvals[1],QtGui.QPen(QtCore.Qt.yellow))

    def set_xy (self, xvals, yvals) :
        self.clear()
        self.plot(xvals, yvals[0], pen=self.pen0)
        self.plot(xvals, yvals[1], pen=self.pen1)

    # self.plot(x,yvals[0],QtGui.QPen(QtCore.Qt.red))
    # self.plot(x,yvals[1],QtGui.QPen(QtCore.Qt.yellow))




    def plot_data (self, x, y):
        self.plot(x,y)

    def set_plot_data (self, xarr, yarr):
        self.xarr = xarr
        self.yarr = yarr

    def add_points(self, year, val0, val1):
        #self.clear()
        xvals = [2000,year]
        yvals = [val0, val1]

        #self.addPoints(xvals,yvals,symbol='t1')
        #self.plot(xvals,yvals,pen=self.pen0)
        self.plot([year,], [val0,], pen=self.pen0, symbol='t1', symbolSize=10)
        self.plot([year, ], [val1, ], pen=self.pen1, symbol='t1', symbolSize=10)
        #self.plot([year], [val1], symbol='o')

