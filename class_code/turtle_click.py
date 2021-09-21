#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 13 20:09:57 2021

@author: dieter
"""

import turtle
turtle.bye()				# close existing screens, if any

my_turtle = turtle.Turtle()	# make a variable called robot
my_turtle.shape('turtle')

def get_mouse_click_coor(x, y):
    print(x, y)

turtle.onscreenclick(get_mouse_click_coor)

turtle.mainloop()