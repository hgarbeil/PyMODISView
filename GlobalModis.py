import pathlib
from PyQt5 import QtCore

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
    file_loaded = QtCore.pyqtSignal()

    def __init__(self):
        print ('starting line is ', self.startl)
        ns2 = self.ns / 2
        nl2 = self.nl / 2
        cent_x, cent_y = self.xy_to_latlon(ns2,nl2)
        print ("center lat lon ", cent_x, "  ", cent_y)

    def xy_to_latlon(self, x, y):
        ## given the x and y coordinate locations return the lat and lon
        xloc = self.starts + x
        yloc = self.startl + y

        latval = 90. - (yloc * self.deg_per_pixel)
        lonval = -180. + (xloc * self.deg_per_pixel)
        return lonval,latval

    def latlon_to_xy (self, lon, lat) :
        xloc = int((lon + 180.) / self.deg_per_pixel )
        yloc = int((90 - latval) / self.deg_per_pixel)

    def parse_filename (self) :
        self.pathname = pathlib.Path(self.filename).parent
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