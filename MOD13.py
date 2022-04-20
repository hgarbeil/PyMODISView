


import numpy as np
from pyhdf.SD import SD, SDC
from GlobalModis import *

indir = '/Users/hg1/data/MOD13'

class MOD13(GlobalMODIS):
    # ns = 1320
    # nl = 700
    # starts = 1080
    # startl = 700

    def __init__(self, fname):
        super(MOD11,self).__init__()
        file = SD(fname, SDC.READ)
        print(file.info())
        sds_obj = file.select('CMG 0.05 Deg Monthly NDVI')
        data = sds_obj.get()
        self.data_ndvi = data[self.startl:self.startl+self.nl, self.starts:self.starts+self.ns]
        SD.end(file)
        print ("Number of samples is ", self.ns)






