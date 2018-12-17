#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 11 14:44:14 2018

@author: dieter
"""
import time

first = 'donald'
last = 'duck'
first = first.capitalize()
last = last.capitalize()
full_name = first + ' ' + last

# Alternative

first = 'donald'
last = 'duck'
full_name = full_name.title()
print(full_name)

# Print 10 times, with a space between

new = (first + ' ' + last + ' ') * 10 + '!'
print(new)

# Print the current time is
real_time = 'the current time is ' + time.asctime()
print(real_time)
time.sleep(5) 

