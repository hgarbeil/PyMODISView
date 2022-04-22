#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 21 07:06:19 2022

@author: hg1
"""

from os import listdir
from os.path import isfile,join
from os import walk
import numpy as np
import fnmatch
from pyhdf.SD import SD, SDC

indir = '/Users/hg1/data/MOD11'


for root,dirs,files in walk(indir):
    for name in dirs :
        sub1 = join(root,name)
        print (sub1)
        
        # go into each month directory and get the file names
        for root0,dirs0,files0 in walk(sub1) :
            nfiles = len(files0)
            if nfiles < 1 :
                break 
            filecount = 0 
            for name0 in files0 :
                if fnmatch.fnmatch(name0, "outarr*") :
                    continue 
                filecount = filecount+1

            curdir = root0
            outarr = join(root0,"outarr_day")
            count = 0
            
            darray = np.zeros([filecount,700,1320], dtype=np.uint16)
        #     #print (files0)
            for name0 in files0 :
        #         print(join(root0,name0))
                if fnmatch.fnmatch(name0,"outarr*") :
                    continue  
        
                file_name = join(root0,name0) 
                print ('hdf file is ',file_name)
                file=SD(file_name,SDC.READ)
                print (file.info())
                sds_obj = file.select('LST_Day_CMG')
                data = sds_obj.get()
                dsub=data[700:1400,1080:2400]
                darray[count,:,:]=dsub.copy()
                count=count+1
            darray.tofile(outarr)
