# PyMODISView 

MODIS MOD11 and MOD13 Global MODIS Monthly Global Analysis Software

![GitHub Logo](/imgs/Plot_PyMODISView.png)

## Description

This program will allow a user to read in a MOD11 land surface temperature (LST) hdf global monthly file or a MOD13 normalized difference vegetation index (NDVI) hdf global monthly file. The program has been set to extract a region of interest of the continental United States. Both of these datasets are products from the NASA MODIS Land Science Teams. Program is written in Python with the Qt GUI framework provided by the PyQt5 module. 

## Requirements

### Installation

This program is built with python 3.9 and pyhdf. The easiest method to install is to first download and install anaconda from anaconda.com. The pyqt, pyhdf modules and plotting module pyqtgraph can be put into a python virtual environment after the anaconda install via the terminal with the following commands


conda create --name qt_hdf4_35 python=3.5 pyhdf pyqt pyqtgraph scipy
conda activate qt_hdf4_35 
python3 PyMODISView.py

    
 
### Data
The program is designed to read in global NDVI (MOD13 and MOD11) datasets. These files are available via the NASA data portals for MODIS land data products. In addition to the MOD11 and / or MOD13 files that the user would like to analyze, the program uses cube files which consist of the MOD11 night and day LST data for continental USA and MOD13 NDVI data for the same area with each band or slice of the cube being a year starting at 2001 and ending in 2021. These file cubes were constructed from the 2001 - 2021 MOD11 and MOD13 global .05 degree hdf files. A text file resides with the data which contains the years represented in that directory. The directory structure is described below.

The directory containing the MOD11 and MOD13 files can be organized such that the program can find both the requested image and the file containing all of the LST or NDVI files for that month for all of the years which are represented in the directory. The image below shows the directory organization and a typical month of files (MOD11 January for years 2000 to 2022). Anyone wishing the full dataset can contact the developer to obtain a compressed tar file of the two datasets which would allow for easy operation of the program.

![GitHub Logo](/imgs/datatree.png)

## Current Status
Actively being developed. Albeit in the background.

## Contact
Anyone wishing the dataset can contact me at hgarbeilAThawaii.edu

