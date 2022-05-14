import pandas as pd


class getcities ():
    infile = '/Users/hg1/pydev/PyMODISView/uscities.csv'

    def __init__(self):
        mycities = pd.read_csv (self.infile)
        print (mycities.info)

g = getcities()
