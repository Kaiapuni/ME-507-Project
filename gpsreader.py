# -*- coding: utf-8 -*-
"""
Created on Tue Dec  6 21:50:20 2016

@author: Louis
"""

def checksum(packet):
    """ This function hopefully implements the same XOR checksum as the gps. """
    
    i = 0
    check = 0
    while i < len(packet):
        if packet[i] != '$' and packet[i] != '*':
            check = check ^ ord(packet[i])
        if packet[i] == '*':
            break
        i += 1
    return check
    
def readsum(packet):
    """ This function should read the checksum on incoming packets. """
    
    i = 0
    check = ''
    star = False
    while i < len(packet):
        if star == True:
            if packet[i] != '\r':
                check += packet[i]
            else:
                break
        if packet[i] == '*':
            star = True
        i += 1
    high = int('0x' + packet[i-2])
    low = int('0x' + packet[i-1])
    return high<<4 | low
    
def parse(packet):
    """ This function returns a list containing the separated components of a packet. """
    
    out = packet.split(',') # To start, break a packet up at the commas
    out[len(out)-1] = out[len(out)-1].split('\r')[0] # Remove everything past the checksum from the last index
    out.append(out[len(out)-1].split('*')[1]) # Attach an index containing the checksum
    out[len(out)-2] = out[len(out)-2].split('*')[0] # Replace the second-to-last index with the last piece of data before the checksum
    return out
    
def RMC(gps):
    """ This function searches for and returns a GPRMC sentence from the gps. """
    
    i = 0
    garbage = gps.read(gps.any()) # This line cleans out the buffer so that the function only reads recent data
    while i < 25:
        temp = gps.readline().decode('utf-8')
        if temp.split(',')[0] == '$GPRMC':
            return temp
        i += 1
    return 'fail'