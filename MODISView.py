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
from MOD13 import *
import sys
from mystats import *

# TODO : used getyears to generate the years.txt file, use this as part of the stack data to correctly plot years
#
class UI (QMainWindow):
    def __init__(self) :
        super (UI, self).__init__() 
        self.ui = uic.loadUi("mainwindow.ui", self)
        self.ui.actionOpen.triggered.connect (self.file_open)
        self.ui.actionExit.triggered.connect (self.closeup)
        self.ui.landtempRB.toggled.connect (self.dataprod_changed)
        self.show()
        self.m11 = 0
        ## dataproduct is 0 for LST 1 for NDVI
        self.dataproduct = 0
        # starting selected cursor location
        self.xloc = 660
        self.yloc = 350
        self.ui.image_widget.mouse_clicked.connect(self.newxy)
        self.lon = 0
        self.lat = 0




    def dataprod_changed (self, buttonstate) :
        if (buttonstate) :
            self.dataproduct = 0
        else :
            self.dataproduct = 1


    def file_open (self) :
        ## depending upon data product, open either the MOD11 or MOD13 file,
        # read in the image data and display
        # LST
        #self.ui.plot_widget.testplot()
        if (self.dataproduct == 0) :
            fname = QFileDialog.getOpenFileName(self,"",'/Users/hg1/data/MOD11')
            print(fname)
            self.m11 = MOD11(fname[0])
            self.ui.image_widget.create_qimage_gray(self.m11.data_night)
        # NDVI
            (fname,year, month) = self.m11.getfileinfo()
        if (self.dataproduct == 1) :
            fname = QFileDialog.getOpenFileName(self,"",'/Users/hg1/data/MOD13')
            print(fname)
            self.m13 = MOD13(fname[0])
            self.ui.image_widget.create_qimage_gray(self.m13.data_ndvi)
            (fname,year,month) = self.m13.getfileinfo()

        self.ui.month_CB.setCurrentIndex(month)
        self.ui.fnameLabel.setText(fname)
        self.ui.yearLE.setText(str(year))

        # get the center profile
        if self.dataproduct == 0 :
            outprofile = self.m11.get_time_series(660,350)
            mystats = summarystats (self.m11.stackyears,np.asarray(outprofile[0]))
            mystats1 = summarystats(self.m11.stackyears, np.asarray(outprofile[1]))
            (self.lon,self.lat)=self.m11.xy_to_lonlat(660,350)
            print (mystats)
        else :
            outprofile = self.m13.get_time_series(660, 350)
            mystats = summarystats(self.m13.stackyears, np.asarray(outprofile[0]))
            mystats1 = summarystats(self.m13.stackyears, np.asarray(outprofile[1]))
            (self.lon,self.lat)=self.m11.xy_to_lonlat(660,350)


        self.ui.plot_widget.set_y(outprofile)
        self.ui.plot_widget0.set_y(outprofile)
        self.displaystats (mystats, mystats1)


    def newxy (self, x, y):
        self.xloc = x
        self.yloc = y
        print ("Main : ",x, y)

        # get lon lat
        if (self.dataproduct==0) :
            lon,lat = self.m11.xy_to_lonlat(x,y)
        else :
            lon,lat = self.m13.xy_to_lonlat(x,y)
        str_lon = "{:.2f}".format(lon)
        str_lat = "{:.2f}".format(lat)
        self.ui.lonLE.setText(str_lon)
        self.ui.latLE.setText(str_lat)

        # get the center profile
        if (self.dataproduct==0) :
            outprofile = self.m11.get_time_series(x,y)
            valday = self.m11.data_day[y,x]*self.m11.scale_factor
            valnight = self.m11.data_night[y,x]*self.m11.scale_factor
            self.ui.plot_widget.set_xy(self.m11.stackyears, outprofile)
            self.ui.plot_widget0.set_xy(self.m11.stackyears, outprofile)
            self.ui.plot_widget.add_points(self.m11.year, valnight, valday)
            self.ui.plot_widget0.add_points(self.m11.year, valnight, valday)
            mystats = summarystats(self.m11.stackyears, np.asarray(outprofile[0]))
            mystats1 = summarystats(self.m11.stackyears, np.asarray(outprofile[1]))
        else :
            outprofile = self.m13.get_time_series(x, y)
            valday = self.m13.data_ndvi[y, x] / self.m13.scale_factor
            valnight = self.m13.data_evi[y, x] / self.m13.scale_factor
            self.ui.plot_widget.set_xy(self.m13.stackyears, outprofile)
            self.ui.plot_widget0.set_xy(self.m13.stackyears, outprofile)
            self.ui.plot_widget.add_points(self.m13.year, valnight, valday)
            self.ui.plot_widget0.add_points(self.m13.year, valnight, valday)
            mystats = summarystats(self.m13.stackyears, np.asarray(outprofile[0]))
            mystats1 = summarystats(self.m13.stackyears, np.asarray(outprofile[1]))

        self.displaystats(mystats,mystats1)
        self.ui.plot_widget.add_meanvalues (mystats['mean'], mystats1['mean'])

        # update plot
        #self.ui.plot_widget.set_y(outprofile)
        #sumstatsd = {'npts': npts, 'mean': meanval, 'min': minval, 'max': maxval, 'min_year': minyear,
        #             'max_year': maxyear}

    def displaystats (self, dict_stats, dict_stats1):
        TE_temp = self.ui.timeseriesResTE
        TE_temp.clear()
        TE_temp.append("Long : {:.2f}\tLat : {:.2f}\n".format(self.lon, self.lat))
        #strarray =[]
        str0 = "Number of Years : {}".format(dict_stats['npts'])
        TE_temp.append(str0)
        str0 = "Mean Value : {:.2f}".format(dict_stats['mean'])
        TE_temp.append(str0)
        str0 = "Median Value : {:.2f}".format(dict_stats['median'])
        TE_temp.append(str0)
        str0 = "Min Value  : {:.2f}\tYear of Min : {}".format(dict_stats['min'], dict_stats['min_year'])
        TE_temp.append(str0)
        str0 = "Max Value  : {:.2f}\tYear of Max : {}".format(dict_stats['max'], dict_stats['max_year'])
        TE_temp.append(str0)
        TE_temp.append ("\nSecond Profile")
        str0 = "Mean Value : {:.2f}".format(dict_stats1['mean'])
        TE_temp.append(str0)
        str0 = "Median Value : {:.2f}".format(dict_stats1['median'])
        TE_temp.append(str0)
        str0 = "Min Value  : {:.2f}\tYear of Min : {}".format(dict_stats1['min'], dict_stats1['min_year'])
        TE_temp.append(str0)
        str0 = "Max Value  : {:.2f}\tYear of Max : {}".format(dict_stats1['max'], dict_stats1['max_year'])
        TE_temp.append(str0)


    def closeup (self):
        sys.exit(0)



        
def main() :
    app = QApplication (sys.argv)
    window = UI()
    app.exec_()


if __name__ == "__main__":
	main() 
