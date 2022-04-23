#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 19 10:47:59 2022

@author: hg1
"""

from PyQt5.QtWidgets import QWidget
from PyQt5 import QtGui, QtCore
import numpy as np

class imwidget (QWidget):
    mouse_clicked = QtCore.pyqtSignal (int, int)

    def __init__(self, parent) :
        QWidget.__init__(self,parent)
        self.load_image = False
        self.qimage = 0
        w = self.width()
        h = self.height()
        self.xloc = 660
        self.yloc = 325


    def scale_to_byte (self, indat, minval, maxval) :
        w = np.where (indat < minval)
        s = indat.shape
        outdat = np.zeros (s,dtype=np.uint8)
        scaleval = 254. / (maxval - minval)
        outdat = ((indat - minval) * scaleval).astype(np.uint8)
        outdat[w] = 0
        return outdat


    def create_qimage_gray (self, indata) :
        ## Given a grayscale uint16 array, create the grayscale qimage
        outdat = self.scale_to_byte (indata, 2600, 17000)
        self.qimage = QtGui.QImage (outdat,  outdat.shape[1], outdat.shape[0], QtGui.QImage.Format_Grayscale8)
        self.load_image = True
        self.repaint()



    def paintEvent (self, event):
        painter = QtGui.QPainter(self)
        w = self.width()
        h = self.height()
        painter.drawLine (0,0, w, h)
        painter.drawLine (w,0,0,h)

        if self.load_image == False :
            return

        painter.drawImage(0,0,self.qimage, 0, 0, w, h)
        painter.setPen (QtCore.Qt.yellow)
        painter.drawRect (QtCore.QRect(self.xloc-2, self.yloc-2, 5, 5))


    def mousePressEvent (self, event) :
        self.xloc = event.pos().x()
        self.yloc = event.pos().y()
        print ("X  Y : ", self.xloc, self.yloc)

        self.mouse_clicked.emit (self.xloc, self.yloc)
        self.update()


