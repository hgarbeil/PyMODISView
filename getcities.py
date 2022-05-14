import pandas as pd
import numpy as np

class getcities ():
    infile = '/Users/hg1/pydev/PyMODISView/uscities.csv'

    def __init__(self):
        self.mycities = pd.read_csv (self.infile)


    def parse_lonlat (self):
        ### return a dict of name, lat, lon,
        #packed = [l0,l1,l2]
        #print (packed[0:1][10])
        dfnew = self.mycities[['city','state_id','lng','lat']]
        newl = dfnew.to_dict('series')
        return newl



g = getcities()
