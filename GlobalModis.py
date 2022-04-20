
class GlobalMODIS :
    ns = 1320
    nl = 700
    starts = 1080
    startl = 700
    deg_per_pixel = 0.05 ;
    filename = ''
    pathname = ''

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
