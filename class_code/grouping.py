#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr  2 11:12:57 2019

@author: dieter
"""
import numpy
from matplotlib import pyplot

def polar2cart(r, angle):
    angle = numpy.deg2rad(angle)
    x = r * numpy.cos(angle)
    y = r * numpy.sin(angle)
    return x, y

# Plot arcs
angles = numpy.linspace(0,180,1000)
distances = [25, 50, 75, 100, 125, 150, 175, 200]

for distance in distances:
    x, y = polar2cart(distance, angles)
    pyplot.plot(x,y,color='black')
    
# Plot Lines
mx = max(distances)
distances = numpy.linspace(0, mx, 1000)
angles = [0, 30, 60, 90, 120, 150, 180]

for angle in angles:
    x, y = polar2cart(distances, angle)
    pyplot.plot(x,y,color='black')
    



pyplot.grid()
pyplot.xlabel('X coordinate (cm)')
pyplot.ylabel('Y coordinate (cm)')
ax = pyplot.gca()
ax.set_aspect('equal', 'box')
pyplot.show()

