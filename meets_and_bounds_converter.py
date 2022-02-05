#!/usr/bin/env python3
__author__ = 'Gerry Gabrisch (geraldg@lummi-nsn.gov)'
__date__ = 'February 2022'
'''Converts meets and bounds to compass azimuth.'''

import sys
import traceback


try:

    meets_and_bounds = 's152637e'
    #meets_and_bounds = input('enter direction: ')
    
    orientation = meets_and_bounds[0]
    degrees = meets_and_bounds[1:3]
    minutes = meets_and_bounds[3:5]
    seconds = meets_and_bounds[5:7]
    direction = meets_and_bounds[-1:]
    
    #this is the difference between grid north and true north.
    angle_of_convergence = 0
    
    
    def get_start_direction(orientation, direction):
        if orientation.upper() == 'N' and direction.upper() == 'E':
            start_direction = 0
        if orientation.upper() == 'N' and direction.upper() == 'W':
                start_direction = 360           
        if orientation.upper() == 'S':
                start_direction = 180             
        return start_direction
    
    
    def make_decimal_degrees(degrees, minutes, seconds):
        return float(degrees) + float(minutes)/60.0 + float(seconds)/3600.0
    
    
    
    
    
    
    def get_angle(start_direction, decimal_degrees, direction):
        if orientation.upper() == 'N' and direction.upper() == 'E':
            angle = decimal_degrees
        if orientation.upper() == 'N' and direction.upper() == 'W':
            angle = -1.0 * decimal_degrees
        if orientation.upper() == 'S' and direction.upper() == 'E':
            angle = -1.0 * decimal_degrees 
        if orientation.upper() == 'S' and direction.upper() == 'W':
            angle = decimal_degrees         
        return angle
    
    
    
        
    
    start_direction = get_start_direction(orientation, direction)
    decimal_degrees = make_decimal_degrees(degrees, minutes, seconds) - angle_of_convergence
    azimuth = start_direction + get_angle(start_direction, decimal_degrees, direction)
    
    
    
    print('azimuth = ', round(azimuth,7))
    

    print('\nFinished without error')
except:
    tb = sys.exc_info()[2]
    tbinfo = traceback.format_tb(tb)[0]
    print ("PYTHON ERRORS:\nTraceback info:\n" + tbinfo + "\nError Info:\n" + str(sys.exc_info()[1]))
