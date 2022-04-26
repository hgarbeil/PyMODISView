## mystats.py
#  python module to return summary statistics given an array or profile
from typing import List, Union, Any

import numpy as np
import scipy
from numpy import ndarray


def summarystats (xarray, array) :
    npts = array.size
    meanval = np.mean(array)
    minval = np.min (array)
    maxval = np.max(array)
    minyear = xarray[np.argmin(array)]
    maxyear = xarray[np.argmax(array)]
    sumstatsd = {'npts':npts, 'mean':meanval, 'min':minval, 'max':maxval, 'min_year':minyear, 'max_year':maxyear}
    #sumstats: list[Union[Union[ndarray, int, float, complex], Any]] = [npts, meanval, minval, maxval, minyear, maxyear]\
    print(sumstatsd['mean'])
    return sumstatsd