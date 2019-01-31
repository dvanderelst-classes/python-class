#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 29 11:40:09 2019

@author: dieter
"""

number = 5
drink = 'soda'

text = "x bottles of y on the wall. x bottles of y. If one of those bottles should happen to fall, z bottles of y on the wall."
text = text.replace('x', str(number))
text = text.replace('y', drink)
text = text.replace('z', str(number-1))


t = 'pythsakweawdkdsaksadksadon'
mid = t[1:-1]
first = t[0]
last = t[-1]
print(last + mid + first)