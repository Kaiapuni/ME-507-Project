# -*- coding: utf-8 -*-
"""
Created on Sat Dec  3 14:07:49 2016

@author: Louis
"""

""" This module facilitates communicating with
    the Adafruit 9DOF LSM303 and L3DG20 IMU """


def accelenable(imu, rate):
    """ This function sets the accelerometer power mode and data rate. """
    
    current = ord(imu.mem_read(1, 0x19, 0x20))
    
    if rate == 0:
        out = current & 0b00001111 | 0b00000000
        imu.mem_write(out, 0x19, 0x20, timeout=1000)
        print('\n' + 'accelerometer powered down.' + '\n')
    elif rate == 1:
        out = current & 0b00001111 | 0b00010000
        imu.mem_write(out, 0x19, 0x20, timeout=1000)
        print('\n' + 'accelerometer powered on, configured at 1 Hz.' + '\n')
    elif rate == 10:
        out = current & 0b00001111 | 0b00100000
        imu.mem_write(out, 0x19, 0x20, timeout=1000)
        print('\n' + 'accelerometer on, configured at 10 Hz.' + '\n')
    elif rate == 25:
        out = current & 0b00001111 | 0b00110000
        imu.mem_write(out, 0x19, 0x20, timeout=1000)
        print('\n' + 'accelerometer on, configured at 25 Hz.' + '\n')
    elif rate == 50:
        out = current & 0b00001111 | 0b01000000
        imu.mem_write(out, 0x19, 0x20, timeout=1000)
        print('\n' + 'accelerometer on, configured at 50 Hz.' + '\n')
    elif rate == 100:
        out = current & 0b00001111 | 0b01010000
        imu.mem_write(out, 0x19, 0x20, timeout=1000)
        print('\n' + 'accelerometer on, configured at 100 Hz.' + '\n')
    elif rate == 200:
        out = current & 0b00001111 | 0b01100000
        imu.mem_write(out, 0x19, 0x20, timeout=1000)
        print('\n' + 'accelerometer on, configured at 200 Hz.' + '\n')
    elif rate == 400:
        out = current & 0b00001111 | 0b01110000
        imu.mem_write(out, 0x19, 0x20, timeout=1000)
        print('\n' + 'accelerometer on, configured at 400 Hz.' + '\n')
    elif rate == 1620:
        out = current & 0b00001111 | 0b10000000
        imu.mem_write(out, 0x19, 0x20, timeout=1000)
        print('\n' + 'accelerometer on, configured at 1.620 KHz.' + '\n' + 'This configuration is exclusive to low-power mode.' + '\n')
    elif rate == 1344:
        out = current & 0b00001111 | 0b10010000
        imu.mem_write(out, 0x19, 0x20, timeout=1000)
        print('\n' + 'accelerometer on, configured at 1.344 KHz.' + '\n' + 'This configuration is exclusive to normal-power mode.' + '\n')
    elif rate == 5376:
        out = current & 0b00001111 | 0b10010000
        imu.mem_write(out, 0x19, 0x20, timeout=1000)
        print('\n' + 'accelerometer on, configured at 5.376 KHz.' + '\n' + 'This configuration is exclusive to low-power mode.' + '\n')
    else:
        print('\n' + 'invalid input. To power down, enter 0.' + '\n')
        print('valid data rates are as follow:' + '\n')
        print('1' + '\n' + '10' + '\n' + '25' + '\n' + '50' + '\n' + '100' + '\n' + '200' + '\n' + '400' + '\n' + '1620 (low-power only)' + '\n' + '1344 (normal power only)' + '\n' + '5376 (low-power only)' + '\n')
    
def printcontents(imu, device, location):
    """ This function prints a byte of data located within an I2C device. """
    
    current = bin(ord(imu.mem_read(1, device, location)))
    print(current)

def accelaxes(imu, x, y, z):
    """ This function enables or disables the axes of the accelerometer. """
    
    current = ord(imu.mem_read(1, 0x19, 0x20))
    
    if x:
        current = current & 0b11111110 | 0b00000001
    else:
        current = current & 0b11111110
    if y:
        current = current & 0b11111101 | 0b00000010
    else:
        current = current & 0b11111101
    if z:
        current = current & 0b11111011 | 0b00000100
    else:
        current = current & 0b11111011
    imu.mem_write(current, 0x19, 0x20, timeout=1000)
    
def accelp(imu, mode):
    """ This function determines whether the accelerometer operates in low-power mode. """
    
    current = ord(imu.mem_read(1, 0x19, 0x20))
    
    if mode:
        current = current & 0b11110111 | 0b00001000
        print('\n' + 'accelerometer low-power mode enabled.' + '\n')
    else:
        current = current & 0b11110111
        print('\n' + 'accelerometer low-power mode disabled.' + '\n')
    imu.mem_write(current, 0x19, 0x20, timeout=1000)
    
def accelsetup(imu, rate, mode, x, y, z):
    """ This function sets up the IMU CTRL_REG1 in a single step. """
    
    accelenable(imu, rate)
    accelp(imu, mode)
    accelaxes(imu, x, y, z)
    
def accelquickstart(imu):
    """ This function sets up the IMU with the preset configuration I expect to want to use. """
    """ Currently: Enable, 400 Hz, Low-Power, All axes enabled. """
    accelsetup(imu, 5376, 1, 1, 1, 1)
    
def ax(imu):
    """ This function reads the x axis of the accelerometer. """
    
    low = ord(imu.mem_read(1, 0x19, 0x28))
    high = ord(imu.mem_read(1, 0x19, 0x29))
    output = (high<<8) | low
    if output >= 0b1000000000000000:
        output -= 65536
    return output
    
def ay(imu):
    """ This function reads the y axis of the accelerometer. """
    
    low = ord(imu.mem_read(1, 0x19, 0x2A))
    high = ord(imu.mem_read(1, 0x19, 0x2B))
    output = (high<<8) | low
    if output >= 0b1000000000000000:
        output -= 65536
    return output

def az(imu):
    """ This function reads teh z axis of the accelerometer. """
    
    low = ord(imu.mem_read(1, 0x19, 0x2C))
    high = ord(imu.mem_read(1, 0x19, 0x2D))
    output = (high<<8) | low
    if output >= 0b1000000000000000:
        output -= 65536
    return output

def acceleration(imu):
    """ This function returns a list containing each component of acceleration. """
    
    out = []
    out.append(ax(imu))
    out.append(ay(imu))
    out.append(az(imu))
    return out
    
def ax100(imu):
    """ This function exists for testing, and prints x acceleration 100 times. """
    
    for run in range (0, 101):
        print(ax(imu))
        run += 1
        
def ares(imu, hires):
    """ This function controls high resolution mode. """
    
    current = ord(imu.mem_read(1, 0x19, 0x23))
    
    if hires:
        current = current & 0b11110111 | 0b00001000
        print('\n' + 'accelerometer high-resolution enabled.' + '\n')
    else:
        current = current & 0b11110111
        print('\n' + 'accelerometer high-resolution disabled.' + '\n')
    imu.mem_write(current, 0x19, 0x23, timeout=1000)

def maginit(imu):
    """ This function enables readings from the magnetometer. Probably. """
    
    imu.mem_write(0b00000000, 0x1E, 0x02)
    imu.mem_write(0b00011100, 0x1E, 0x00)
    
def magdrdy(imu):
    """ This function checks the bit indicating whether a new set of measurements is available on the magnetometer. """
    
    return ord(imu.mem_read(1, 0x1E, 0x09)) & 0b00000001
    
#def maglock(imu):
#    """ This function should be able to clear the lock bit in the magnetometer, allowing repeated readings. """
#    """ Update: It doesn't work the way I thought it would. Something's up. """
#    current = ord(imu.mem_read(1, 0x1E, 0x09))
#    current = current & 0b11111101
#    imu.mem_write(current, 0x1E, 0x09)
    
def magsingle(imu):
    """ This function configures the magnetometer for a single conversion. """
    
    imu.mem_write(0b00000001, 0x1E, 0x02)
        
def magx(imu):
    """ This function reads the x-axis of the magnetometer. """
    
    low = ord(imu.mem_read(1, 0x1E, 0x04))
    high = ord(imu.mem_read(1, 0x1E, 0x03))
    output = (high<<8) | low
    if output >= 0b1000000000000000:
        output -= 65536
    return output
    
def magy(imu):
    """ This function reads the y-axis of the magnetometer. """
    
    low = ord(imu.mem_read(1, 0x1E, 0x08))
    high = ord(imu.mem_read(1, 0x1E, 0x07))
    output = (high<<8) | low
    if output >= 0b1000000000000000:
        output -= 65536
    return output
    
def magz(imu):
    """ This function reads the z-axis of the magnetometer. """
    
    low = ord(imu.mem_read(1, 0x1E, 0x06))
    high = ord(imu.mem_read(1, 0x1E, 0x05))
    output = (high<<8) | low
    if output >= 0b1000000000000000:
        output -= 65536
    return output

def magx100(imu):
    """ This function prints the x-axis of the magnetometer 100 times for testing purposes. """
    
    for run in range (0, 101):
        magsingle(imu)
        out = magx(imu)
        print(out)