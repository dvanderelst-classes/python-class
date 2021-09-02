#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  5 15:02:25 2019

@author: dieter
"""
import math

phi = 45
speed = 5
g = 9.98

radians = math.radians(phi)

t = 2 * speed * math.sin(radians) / g
d = (speed **2 / g)* math.sin(2 * radians)

print(t)
print(d)