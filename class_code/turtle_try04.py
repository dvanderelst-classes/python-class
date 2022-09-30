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

i = 10000

for i in range(36):
    my_turtle.color("red")
    if i > 17: my_turtle.color("blue")
    my_turtle.backward(200)
    my_turtle.left(5)
    my_turtle.forward(200)
    my_turtle.left(5)
    