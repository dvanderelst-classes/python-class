#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 28 14:17:40 2021

@author: dieter
"""


import turtle # import the turtle
turtle.bye()        # close existing screens, if any
my_turtle = turtle.Turtle()    # make a variable called my_turtle
my_turtle.shape('turtle')

x = [1,2,3,4,5,6,7,8,9,10,11,12]
y = [1,2,10,20,25,30,25,20,15,10,25,12]

scale_x = 20
scale_y = 8

n = len(x)

my_turtle.forward(max(x) * scale_x)
my_turtle.backward(max(x) * scale_x)
my_turtle.left(90)
my_turtle.forward(max(y) * scale_y)
my_turtle.backward(max(y) * scale_y)
my_turtle.right(90)

for i in range(n):
    current_x_value = x[i] * scale_x
    current_y_value = y[i] * scale_y
    
    my_turtle.setposition(current_x_value, current_y_value)
    my_turtle.stamp()
    

