#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 31 14:45:24 2021

@author: dieter
"""
import time
import math

start = time.time()

((math.pi * math.pi) ** 0.25) ** (12 + 123)

completed = time.time()
duration = (completed - start) * 1000 #Take the difference and convert to milliseconds (1/1000th of a second)
print('This took me', duration, 'milliseconds') 