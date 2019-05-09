#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 12 11:47:27 2019

@author: dieter
"""

for x in range(1,50):
    if x%3==0 and x%5==0: print('FizzBuzz')
    if x%3==0 and not x%5==0: print('Fizz')
    if not x%3==0 and x%5==0: print('Buzz')
    if not x%3==0 and not x%5==0: print(x)
        