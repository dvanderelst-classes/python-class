#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  5 14:35:49 2019

@author: dieter
"""

p = 100
r = 1
y = 10


r = r/ 100

interest = p * r * y
compounded = p * (1 + r)**y - p

print('Interest......' + str(interest))
print('compounded Interest......' + str(compounded))