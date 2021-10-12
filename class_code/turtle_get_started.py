#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 23 14:42:12 2021

@author: dieter
"""

import turtle # import the turtle
turtle.bye()        # close existing screens, if any
my_turtle = turtle.Turtle()    # make a variable called my_turtle
my_turtle.shape('turtle')


n = 5

for i in range(n): 
    my_turtle.forward(15)
    my_turtle.right(360/n)
