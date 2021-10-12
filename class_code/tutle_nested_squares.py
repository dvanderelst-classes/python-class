#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 28 14:30:39 2021

@author: dieter
"""

import turtle # import the turtle
turtle.bye()        # close existing screens, if any
my_turtle = turtle.Turtle()    # make a variable called my_turtle
my_turtle.shape('turtle')

n = 4
my_turtle.left(90)

start_edge_length = 50
for j in range(36):
    # this bit draws 1 square
    for i in range(n): 
        my_turtle.forward(start_edge_length)
        my_turtle.right(360/n)
    #for the next square, change the edgelength
    start_edge_length = start_edge_length + 10
    my_turtle.left(10)
    
    
