

from GlobalModis import *

indir = '/Users/hg1/data/MOD11'

class MOD11(GlobalMODIS):
    # ns = 1320
    # nl = 700
    # starts = 1080
    # startl = 700

# TODO : Populate years list with list in years.txt in the data directories.
    def __init__(self, fname=None):
        super(MOD11,self).__init__()

        self.filename = fname
        self.read_data()
        #self.stacked_day = np.zeros((1,1))
        #self.stacked_night = np.zeros((1,1))


    def read_data(self):
        file = SD(self.filename, SDC.READ)
        print(file.info())
        sds_obj = file.select('LST_Day_CMG')
        data = sds_obj.get()
        attrs = sds_obj.attributes()
        # for idx,sds in enumerate(attrs.keys()) :
        #     print(idx,sds)
        for key, val in attrs.items():
            if (key == 'scale_factor'):
                print('SCALE_FACTOR   : ', key, ':', val)
                self.scale_factor = val
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
        yfile = os.path.join(self.pathname,'years.txt')
        nbytes = os.path.getsize(sfile)
        self.nyears = int(nbytes / (self.ns * self.nl * 2))
        print("number of years in outarr is ", self.nyears)
        self.stacked_night = np.fromfile (sfile, dtype=np.uint16).reshape(self.nyears, self.nl, self.ns)
        sfile = os.path.join(self.pathname, 'outarr_day')
        self.stacked_day = np.fromfile(sfile, dtype=np.uint16).reshape(self.nyears, self.nl, self.ns)
        f = open (yfile,'r')
        allyears = f.readlines()
        for l in allyears :
            self.stackyears.append(int(l))



    def get_time_series (self, x, y) :
        myprof0 = self.stacked_night[:,y,x]*self.scale_factor
        myprof1 = self.stacked_day[:,y,x]*self.scale_factor
        newarr=[myprof0 , myprof1]
        return newarr
