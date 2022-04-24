##
# getyears.pro
# looks at each of the month directories to determine which years are present. In several cases, a year from the
# dataset download was omitted, probably due to technical issues during the download
##

from os import listdir, walk
from os.path import isfile, join
import fnmatch

indir = '/Users/hg1/data/MOD11'

for root, dirs, files in walk(indir):
    for name in dirs:
        sub1 = join(root, name)
        # get files in the month file

        # get the files in month directory, figure out the year and write to outfile
        outfile = join(sub1, 'years.txt')
        f = open(outfile, 'w')
        for root0, dirs0, files0 in walk(sub1):
            for name in files0:
                mstring = '*.A20*'
                if (fnmatch.fnmatch(name, mstring)):
                    pos = name.find('.A20')
                    yearstring = name[pos + 2:pos + 6]
                    print(yearstring)
                    f.write(yearstring + '\n')
        f.close()
