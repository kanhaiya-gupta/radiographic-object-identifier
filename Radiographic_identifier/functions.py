"""
File: functions.py
Author: Kanhaiya Gupta
Date: 2023-08-29
Description: A Python script for round off the values & 
conversion to base 57 number.

"""

from module_list import *

# Round the values according to resolution

def roundPartial (value, resolution_value):
    if resolution_value != -999.:
        return np.round (value / resolution_value) * resolution_value
    else:
        return value

def roundPartial_vol(value, resolution_value):
    if resolution_value != -999.:
        value_dv = 3**value*resolution_value*((4*np.pi)/(3*value))**(1/3)
        value_dv = np.round(value_dv)
        return np.round (value / value_dv) * value_dv
    else:
        return value


# Conversion table of remainders to
# Base57 decimal equivalent
conversion_table = {0: '0', 1: '1', 2: '2', 3: '3', 4: '4',
                    5: '5', 6: '6', 7: '7', 8: '8', 9: '9', 10: 'A', 11: 'B', 12: 'C',
                    13: 'D', 14: 'E', 15: 'F', 16: 'G', 17: 'H', 18: 'J', 19: 'K', 20: 'L',
                    21: 'M', 22: 'N', 23: 'P', 24: 'Q', 25: 'R', 26: 'S', 27: 'T', 28: 'U',
                    29: 'V', 30: 'W', 31: 'X', 32: 'Y', 33: 'Z',
                    34: 'a', 35: 'b', 36: 'c', 37: 'd', 38: 'e', 39: 'f', 40: 'g', 41: 'h', 
                    42: 'j', 43: 'k', 44: 'm', 45: 'n', 46: 'p', 47: 'q', 48: 'r', 49: 's',
                    50: 't', 51: 'u', 52: 'v', 53: 'w', 54: 'x', 55: 'y', 56: 'z', }


# function which converts decimal value
# to base 57 value
def decimalToBase57decimal(decimal):
    base57decimal = ''
    while(decimal > 0):
        remainder = decimal % 57
        base57decimal = conversion_table[remainder] + base57decimal
        decimal = decimal // 57

    return base57decimal

