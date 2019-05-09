#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 19 11:43:52 2019

@author: dieter
"""
import math 

def even(number):
    result = number%2==0
    return result

def circ(radius):
    result = 2 * math.pi * radius
    return result

def area(radius):
    result = math.pi * radius ** 2
    return result


def circle(radius):
    surface = area(radius)
    circumference = circ(radius)
    return circumference, surface


print(even(1001))