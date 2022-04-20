


import numpy as np
from pyhdf.SD import SD, SDC
from GlobalModis import *
import os

indir = '/Users/hg1/data/MOD11'

class MOD11(GlobalMODIS):
    # ns = 1320
    # nl = 700
    # starts = 1080
    # startl = 700

    def __init__(self, fname):
        super(MOD11,self).__init__()
        self.filename = fname
        self.read_data()
        self.stacked_day = ""
        self.stacked_night = ""

    def read_data(self):
        file = SD(self.filename, SDC.READ)
        print(file.info())
        sds_obj = file.select('LST_Day_CMG')
        data = sds_obj.get()
        self.data_day = data[self.startl:self.startl+self.nl, self.starts:self.starts+self.ns]
        sds_obj = file.select('LST_Night_CMG')
        data = sds_obj.get()
        self.data_night = data[self.startl:self.startl + self.nl, self.starts:self.starts + self.ns]

        SD.end(file)
        print ("Number of samples is ", self.ns)
        super().parse_filename ()
        self.read_stacked()




    def read_stacked (self) :
        ## read in the nighttime stacked file
        sfile = os.path.join(self.pathname,'outarr')
        nbytes = os.path.getsize(sfile)
        self.nyears = int(nbytes / (self.ns * self.nl * 2))
        print("number of years in outarr is ", self.nyears)
        outarr_night = np.fromfile (sfile, dtype=np.uint16).reshape(self.nyears, self.nl, self.ns)
