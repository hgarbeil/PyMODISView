# MODISView 

MODIS MOD11 and MOD13 Global MODIS Monthly Global Analysis Software

## Description

This program will allow a user to read in a MOD11 land surface temperature (LST) hdf global monthly file or a MOD13 normalized difference vegetation index (NDVI) hdf global monthly file. The program has been set to extract a region of interest of the continental United States. Both of these datasets are products from the NASA MODIS Land Science Teams. 

## Requirements

### Installation

This program is built with python 3.9 and pyhdf. The easiest method to install is to first download and install anaconda from anaconda.com.
    
  * HDF 4.2.15
    * https://support.hdfgroup.org/release4/obtain.html
    
 
### Data
The program is designed to read in global NDVI (MOD13 and MOD11) datasets. These files are available via the NASA data portals for MODIS land data products. In addition to the MOD11 and / or MOD13 files that the user would like to analyze, the program uses cube files which consist of the MOD11 night and day LST data for continental USA and MOD13 NDVI data for the same area with each band or slice of the cube being a year starting at 2001 and ending in 2021. These file cubes were constructed from the 2001 - 2021 MOD11 and MOD13 global .05 degree hdf files.  


## Current Status
This program is under construction. Documentation is lagging behind the program status. Documentation for data directory format and an example dataset will be constructed and added. Also would like to add some screenshots. Basic capabilities for data access and visualization are in a skeleton framework at this point. Better data visualization and analysis are required. Although python programs exist to build the file stack these have not been placed in the repository. This will be forthcoming.

