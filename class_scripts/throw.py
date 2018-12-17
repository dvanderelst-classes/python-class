#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  6 14:14:59 2018

@author: dieter
"""

import random
import math 

angle_degrees = random.uniform(30,45)
speed = random.uniform(5,10)

angle = math.radians(angle_degrees)


d = (speed ** 2) / 9.81 * math.sin(2 * angle)
t = 2 * speed * math.sin(angle) / 9.81

print(d)
print(t)