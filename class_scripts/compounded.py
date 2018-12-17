#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  6 14:45:43 2018

@author: dieter
"""

p = 100
r = 70
y = 3.3

i = p * (1+(r/100))**y
just_the_interest = i - p
print(i)
print(just_the_interest)