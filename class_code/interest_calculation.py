#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  1 14:03:21 2022

@author: dieter
"""

capital = 100
rate = 0.1
duration = 10

interest = capital * rate * duration
interest = capital * (1 + rate)**duration
print('I get', interest, 'dollars as interesst')