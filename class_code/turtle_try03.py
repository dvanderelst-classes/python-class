#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 29 14:31:24 2022

@author: dieter
"""

import turtle                # import the turtle

turtle.clearscreen()

n_corners = 4
      
my_turtle = turtle.Turtle()    # make a variable called my_turtle
my_turtle.shape('turtle')       # set the shape of the robot to ‘turtle’

size = 100
for x in range(10):
    for i in range(n_corners):
        my_turtle.forward(size)
        my_turtle.left(360/n_corners)
    size = size + 10

