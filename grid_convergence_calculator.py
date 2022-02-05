#!/usr/bin/env python3
__author__ = 'Gerry Gabrisch (geraldg@lummi-nsn.gov)'
__date__ = 'February 2022'
'''calculates grid convergences for common projected coordinate reference systems for the Pacific NW.'''

import sys
import traceback


try:
    
    #Zone central longitudes
    
    
    NAD83UTM10N = -123
    #EPSG:2285 NAD83 / Washington North (ftUS)    
    
    NAD83WaSPn = -120.89
    
    #EPSG:2286  NAD83 / Washington South (ftUS)    
    NAD83WaSPs = -120.2982
    
    
    gc = arctan [tan (long - cm) × sin lat]
    
    where
    
    gc is grid convergence,
    cm is longitude of UTM zone's central meridian,
    lat, long are latitude, longitude of point in question   
    
    
  
 
    

    print('\nFinished without error')
except:
    tb = sys.exc_info()[2]
    tbinfo = traceback.format_tb(tb)[0]
    print ("PYTHON ERRORS:\nTraceback info:\n" + tbinfo + "\nError Info:\n" + str(sys.exc_info()[1]))
