#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 31 14:59:32 2021

@author: dieter
"""

captial = 15855
rate = 1
duration = 25

#interest = captial * (rate / 100) * duration
interest = captial * (1 + (rate / 100))** duration

print('The client gets', interest, 'dollars from us.')

output = 'The client gets ' + str(int(interest)) + ' dollars from us.'

f = open('output.txt', 'w')
f.write(output)
f.close()

print(output)