# boot.py -- run on boot-up
# can run arbitrary Python, but best to keep it minimal

import machine
import pyb
import imureader
import math
from ws2812 import WS2812
import time
#pyb.main('main.py') # main script to run after this one
#pyb.usb_mode('CDC+MSC') # act as a serial and a storage device
#pyb.usb_mode('CDC+HID') # act as a serial device and a mouse

imu = pyb.I2C(2, pyb.I2C.MASTER)
imu.init(pyb.I2C.MASTER, baudrate=100000)
imureader.accelquickstart(imu)
imureader.maginit(imu)
LED_strip = WS2812(spi_bus = 2, led_count = 29)
rgb_data = [(0, 0, 0)]*29
gps = pyb.UART(6, 9600)