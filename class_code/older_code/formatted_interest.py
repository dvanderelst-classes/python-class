#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 21 14:49:26 2021

@author: dieter
"""

captial = 2500
rate = 0.02
duration = 5

interest = captial * (1 + rate) ** duration
total = interest + captial

#print(interest)
#print(interest + captial)

title = str(float(duration)) 
title = title + ' YEAR PROJECTION'
title = title.center(40, '+')
print(title)


print()
print('interest'.ljust(15, ' ')+ '$'+str(interest))
print('captital'.ljust(15, ' ') + '$'+str(captial))
print('total'.ljust(15, ' ') + '$'+str(total))




 
