#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 14:17:12 2019

@author: dieter
"""
import time
## simple stuff

first_name = 'dieter'
last_name = 'vanderelst'
first_name = first_name.capitalize()
last_name = last_name.capitalize()

full = first_name + ' ' + last_name
multi = (full + ' ') * 10
multi = multi.rstrip(' ')
print(multi)

time_string = time.asctime()
print('Current time is ' + time_string)