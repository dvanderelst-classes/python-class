#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  8 14:19:28 2022

@author: dieter
"""

import math

my_list = ['donald duck', 3, math.pi]

#option 1 
my_list.append(True)
#option 2
my_list = my_list + [True]

#option 1 
my_list.insert(0, True)
#option 2
my_list =  [True] + my_list

long_list = range(1000, 2501)
long_list = list(long_list)

print(len(long_list))
popped_number = long_list.pop(1000)
print(len(long_list))