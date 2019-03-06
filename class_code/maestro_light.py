#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 28 11:12:38 2019

@author: dieter
"""

from course import board
b = board.Board()
import time
while True:
    value = b.get_photo()
    if value < 0.7: 
        print('who turned the lights off', value)
        b.set_led1(True)
    else:
        b.set_led1(False)
    time.sleep(0.25)