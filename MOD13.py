


from GlobalModis import *

indir = '/Users/hg1/data/MOD13'

class MOD13(GlobalMODIS):
    # ns = 1320
    # nl = 700
    # starts = 1080
    # startl = 700

    def __init__(self, fname):
        super(MOD13,self).__init__()
        self.filename = fname
        self.read_data()

    def read_data(self) :
        file = SD(self.filename, SDC.READ)
        print(file.info())
        sds_obj = file.select('CMG 0.05 Deg Monthly NDVI')
        data = sds_obj.get()
        attrs = sds_obj.attributes()
        for key, val in attrs.items():
            if (key == 'scale_factor'):
                print('SCALE_FACTOR   : ', key, ':', val)
                self.scale_factor = val
        self.data_ndvi = data[self.startl:self.startl+self.nl, self.starts:self.starts+self.ns]
        sds_obj = file.select('CMG 0.05 Deg Monthly EVI')
        data = sds_obj.get()
        attrs = sds_obj.attributes()
        self.data_evi = data[self.startl:self.startl + self.nl, self.starts:self.starts + self.ns]
        SD.end(file)
        self.parse_filename()
        self.read_stacked()

    def read_stacked (self) :
        ## read in the nighttime stacked file
        sfile = os.path.join(self.pathname,'outarr_ndvi')
        yfile = os.path.join(self.pathname,'years.txt')
        nbytes = os.path.getsize(sfile)
        self.nyears = int(nbytes / (self.ns * self.nl * 2))
        print("number of years in outarr is ", self.nyears)
        self.stacked_ndvi = np.fromfile (sfile, dtype=np.int16).reshape(self.nyears, self.nl, self.ns)
        sfile = os.path.join(self.pathname, 'outarr_evi')
        self.stacked_evi = np.fromfile(sfile, dtype=np.int16).reshape(self.nyears, self.nl, self.ns)
        f = open (yfile,'r')
        allyears = f.readlines()
        for l in allyears :
            self.stackyears.append(int(l))

    def get_time_series(self, x, y):
        myprof0 = self.stacked_ndvi[:, y, x] / self.scale_factor
        myprof1 = self.stacked_evi[:, y, x] / self.scale_factor
        newarr = [myprof0, myprof1]
        return newarr

