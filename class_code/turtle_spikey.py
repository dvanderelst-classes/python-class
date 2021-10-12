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


for i in range(36):
    my_turtle.forward(100)
    my_turtle.right(10)
    my_turtle.backward(200)
    my_turtle.left(20)
