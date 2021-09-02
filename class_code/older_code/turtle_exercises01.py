#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  2 13:50:47 2021

@author: dieter
"""

import turtle				# import the turtle module
turtle.bye()				# close existing screens, if any

my_turtle = turtle.Turtle()	# make a variable called robot
my_turtle.shape('turtle')		# set the shape of the robot to ‘turtle’


for i in range(10, 300, 3):
    my_turtle.circle(i, 30)
    my_turtle.stamp()


#turtle.bye() 			# Closes the turtle screen	