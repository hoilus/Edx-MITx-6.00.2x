# -*- coding: utf-8 -*-
"""
Created on Sat Nov 26 18:37:08 2016

@author: hoilus
""
import math

def stdDevOfLengths(L):
    """
    L: a list of strings

    returns: float, the standard deviation of the lengths of the strings,
      or NaN if L is empty.
    """
    mean = 0
    std = 0
    if len(L) == 0:
        return 'NaN'
    else:
        for i in L:
            mean = mean + len(i)
        mean = mean/len(L)
        for i in L:
            std = std + (len(i)-mean)*(len(i)-mean)
        std = math.sqrt(std/len(L))
        return std
