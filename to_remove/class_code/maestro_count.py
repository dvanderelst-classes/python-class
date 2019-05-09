#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 28 11:12:38 2019

@author: dieter
"""

from course import board
b = board.Board()
import time
count = 0
threshold = 0.7
while True:
    value = b.get_photo()
    b.set_servo2(value)
    time.sleep(0.1)