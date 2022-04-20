#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 19 10:30:42 2022

@author: hg1
"""

from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow,QApplication,QPushButton,QTextEdit,QMenu,QAction
from PyQt5.QtWidgets import QFileDialog
from MOD11 import *
import sys


class UI (QMainWindow):
    def __init__(self) :
        super (UI, self).__init__() 
        self.ui = uic.loadUi("mainwindow.ui", self)
        self.ui.actionOpen.triggered.connect (self.file_open)
        self.ui.actionExit.triggered.connect (self.closeup)
        self.show()
        self.m11 = 0

    def file_open (self) :
        fname = QFileDialog.getOpenFileName(self,"",'/Users/hg1/data/')
        print(fname)
        self.m11 = MOD11(fname[0])
        self.ui.image_widget.create_qimage (self.m11.data_night)

    def closeup (self):
        sys.exit(0)



        
def main() :
    app = QApplication (sys.argv)
    window = UI()
    app.exec_()


if __name__ == "__main__":
	main() 
