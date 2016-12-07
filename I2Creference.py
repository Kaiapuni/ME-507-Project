# -*- coding: utf-8 -*-
"""
Created on Fri Dec  2 16:03:38 2016

@author: Louis
"""

"""
This file will be used as a reference to create functions which
interact with the IMU.
"""

# 0x19 = 25 = 0b0011001 = the address of the accelerometer
# 0x1E = 30 = 0b0011110 = the address of the magnetometer
# 0x6B = 107 = 0b110101 = the address of the gyroscope

from pyb import I2C

# This line creates the i2c object, makes the pyboard the master, and chooses i2c port 2, which our case corresponds to the backup imu breakout.
imu = I2C(2, I2C.MASTER)

# This line initializes imu with a baudrate of 1000000
imu.init(I2C.MASTER, baudrate=100000)

# This line returns a list of the addresses of devices communicating on i2c in decimal
imu.scan()

# This line writes 0b01111111 to register 0x20 of the accelerometer which should enable it in low power mode. Also times out after 1 second.
# This is also where you can set the accelerometer to low-power mode, which lowers the resolution but consumes less current.
# The high resolution enable bit in control register 4 needs to be off in order for low power mode to work.
imu.mem_write(0b01111111, 0x19, 0x20, timeout=1000)

# This line reads one byte from the accelerometer starting at address 0x20.
# Returns ASCII by default for some reason.
imu.mem_read(1, 0x19, 0x20)

# This line converts an ASCII string to a decimal number
ord('abc')

# This line converst a number from the ord() function into a binary string
bin(ord('abc'))

# This line should configure the output mode to stream by writing to FIFO_CTRL_REG_A, or 0x2E.
imu.mem_write(0b10000000, 0x19, 0x2E, timeout=1000)

# This line should enable FIFO by writing to control register 5 on the accelerometer, which should hopefully let it send data.
imu.mem_write(0b01000000, 0x19, 0x24)

# This line probably does nothing, but something similar shows up in an arduino library. I think it's meant to make 2 bytes readable at once.
imu.mem_write(0x80, 0x19, 0x28)

# This function turns things into integers.
int('0b111')


