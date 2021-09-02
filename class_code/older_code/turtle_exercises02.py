#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  2 14:41:49 2021

@author: dieter
"""

import turtle				# import the turtle module
turtle.bye()				# close existing screens, if any

my_turtle = turtle.Turtle()	# make a variable called robot
my_turtle.shape('turtle')	

for i in range(10):
    my_turtle.pendown()
    my_turtle.circle(i * 10)    
    position = my_turtle.ycor()
    my_turtle.penup()
    my_turtle.sety(position - 10)