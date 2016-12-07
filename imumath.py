# -*- coding: utf-8 -*-
"""
Created on Tue Dec  6 15:50:15 2016

@author: Louis
"""

import math

def amagnitude(components):
    """ This function calculates the magnitude of the acceleration. """
    
    return int(math.sqrt(components[0]**2 + components[1]**2 + components[2]**2))
    
def asample(imu, timer):
    """ This function should take multiple readings of acceleration and average them out. """
    
    timer.init(freq=400)
    