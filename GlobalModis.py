import pathlib
from PyQt5 import QtCore
import numpy as np
import os
from pyhdf.SD import SD, SDC



class GlobalMODIS :
    ns = 1320
    nl = 700
    starts = 1080
    startl = 700
    deg_per_pixel = 0.05
    filename = ''
    pathname = ''
    year = 2000
    month = 1
    nyears = 20
    stackyears=[]
    scale_factor = 1.
    file_loaded = QtCore.pyqtSignal()

    def __init__(self):
        print ('starting line is ', self.startl)
        ns2 = int(self.ns / 2)
        nl2 = int(self.nl / 2)
        cent_x, cent_y = self.xy_to_lonlat(ns2,nl2)

        print ("center  lon lat", cent_x, "  ", cent_y)

    def xy_to_lonlat(self, x, y):
        ## given the x and y coordinate locations return the lat and lon
        xloc = self.starts + x
        yloc = self.startl + y

        latval = 90. - (yloc * self.deg_per_pixel)
        lonval = -180. + (xloc * self.deg_per_pixel)
        return lonval,latval

    def lonlat_to_xy (self, lon, lat) :
        xloc = int((lon + 180.) / self.deg_per_pixel )
        yloc = int((90 - latval) / self.deg_per_pixel)
        return xloc,yloc

    def parse_filename (self) :
        self.pathname = str(pathlib.Path(self.filename).parent)
        pos = self.filename.index ('.A20')
        yearstring = self.filename[pos+2:pos+6]
        self.year = int(yearstring)
        daystring = self.filename[pos+6:pos+9]
        self.month = int((int(daystring)+5)/30)
        print ('Path of file is : ',self.pathname)
        print ("Year : ", self.year)
        print ("Month : ", self.month)



    def getfileinfo (self):
        return self.filename, self.year, self.month


    def get_datasets (self, modfile) :
        ## this method is used for convenience to list the datasets and optionally the attributes for
        # the dataset
        file = SD(modfile, SDC.READ)
        print (file.info())
        datasets_dic = file.datasets()

        for idx, sds in enumerate(datasets_dic.keys()):
            print(idx, sds)

        #sds_obj = file.select('CMG 0.05 Deg Monthly NDVI')  # select sds
        sds_obj = file.select (0)
        data = sds_obj.get()  # get sds data
        attrs = sds_obj.attributes()

        # for idx,sds in enumerate(attrs.keys()) :
        #     print(idx,sds)
        for key,val in attrs.items() :
            if (key=='scale_factor') :
                print (key, ':', val)


gc = GlobalMODIS()
gc.get_datasets('/Users/hg1/data/MOD13/001/MOD13C2.A2001001.061.2020061230446.hdf')
