# -*- coding: utf-8 -*-
"""
Created on Mon Nov 14 12:37:05 2016

@author: Louis
"""
# Because I know I'm going to forget:
    # 0x19 = 25 = 0b0011001 = the address of the accelerometer
    # 0x1E = 30 = 0b0011110 = the address of the magnetometer
    # 0x6B = 107 = 0b110101 = the address of the gyroscope
import gpsreader
import lights
    
def gpstopixels(gps, parser, neopixels, num_leds):
    """ This function should call all the requisite functions to update the neopixels. """
    
    gpsreader.quickupdate(gps, parser)
    course = parser.course
    speed = parser.speed[2]
    rgb = lights.merge(course, speed)
    rgb_data = [rgb]*num_leds
    neopixels.show(rgb_data)
    
def fastgpstopixels(gps, parser, neopixels, num_leds):
    """ This function should call all the requisite functions to update the neopixels without the RMC buffer dump. """
    
    gpsreader.quickerupdate(gps, parser)
    course = parser.course
    speed = parser.speed[2]
    rgb = lights.merge(course, speed)
    rgb_data = [rgb]*num_leds
    neopixels.show(rgb_data)