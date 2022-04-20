#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 19 10:47:59 2022

@author: hg1
"""

from PyQt5.QtWidgets import QWidget
from PyQt5 import QtGui

class imwidget (QWidget):
    def __init__(self, parent) :
        QWidget.__init__(self,parent)

    def paintEvent (self, event):
        painter = QtGui.QPainter(self)
        w = self.width()
        h = self.height()
        painter.drawLine (0,0, w, h)
        painter.drawLine (w,0,0,h)