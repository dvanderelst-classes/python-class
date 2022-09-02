#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  1 14:19:24 2022

@author: dieter
"""

import math

v = 10 #this is the speed
a = 4 #this ithe anglea
#%%
g = 10

angle_radians = math.radians(a)
t_in_air  = (2 * v * math.sin(angle_radians)) / g
distance = (v**2/g) * math.sin(2 * angle_radians) 

print('air time', t_in_air)
print('distance', distance)

