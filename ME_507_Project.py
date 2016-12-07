# -*- coding: utf-8 -*-
"""
Created on Mon Nov 14 12:37:05 2016

@author: Louis
"""
# Because I know I'm going to forget:
    # 0x19 = 25 = 0b0011001 = the address of the accelerometer
    # 0x1E = 30 = 0b0011110 = the address of the magnetometer
    # 0x6B = 107 = 0b110101 = the address of the gyroscope

import pyb
import math
from ws2812 import WS2812
import time
import machine

LED_strip = WS2812(spi_bus = 2, led_count = 29)
rgb_data = [(0, 0, 0)]*29
gps = pyb.UART(6, 9600)
