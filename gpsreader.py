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
        if packet[i] != '$' and packet[i] != ',' and packet[i] != '*':
            check = check ^ ord(packet[i])
            print(check)
        if packet[i] == '*':
            return check
        i += 1
    return check
    
def readsum(packet):
    """ This function should read the checksum on incoming packets. """
    
    i = 0
    check = ''
    star = False
    while i < len(packet):
        if star == True:
            if packet[i] != '<':
                check += packet[i]
            else:
                break
        if packet[i] == '*':
            star = True
        i += 1
    high = int('0x' + packet[i-2])
    low = int('0x' + packet[i-1])
    return high<<4 | low