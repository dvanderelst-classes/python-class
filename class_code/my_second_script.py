#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 30 15:15:26 2022

@author: dieter

Write a script that assigns a radius to a variable.
Next, the script uses this radius to calculate 
the surface area or the volume of sphere, using math.pi. 
Print the result to the screen.
"""
import math

radius = 16543
surface = radius ** 2 * math.pi
volume = 4/3 * math.pi * radius**3

print('radius is:', radius) 
print('surface is:', surface)  
print('volume is:', volume)  