#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  2 14:58:14 2018

@author: dieter
"""

def is_even(x):
    even = x%2==0
    return even


def is_odd(x):
    return not is_even(x)


def sum_odd(n):
    sm = 0
    for x in range(0,n):
        if is_odd(x):
            sm = sm + x
    return sm

y = sum_odd(10)
print(y)        
        
    
    
