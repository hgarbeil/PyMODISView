


import numpy as np
from pyhdf.SD import SD, SDC
from GlobalModis import *

indir = '/Users/hg1/data/MOD11'

class MOD11(GlobalMODIS):
    # ns = 1320
    # nl = 700
    # starts = 1080
    # startl = 700

    def __init__(self, fname):
        super(MOD11,self).__init__()
        file = SD(fname, SDC.READ)
        print(file.info())
        sds_obj = file.select('LST_Day_CMG')
        data = sds_obj.get()
        self.data_day = data[self.startl:self.startl+self.nl, self.starts:self.starts+self.ns]
        sds_obj = file.select('LST_Night_CMG')
        data = sds_obj.get()
        self.data_night = data[self.startl:self.startl + self.nl, self.starts:self.starts + self.ns]

        SD.end(file)
        print ("Number of samples is ", self.ns)






