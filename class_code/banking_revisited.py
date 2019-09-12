#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  5 14:35:49 2019

@author: dieter
"""

p = 100
r = 1
y = 10.345322

r = r/ 100

interest = p * (1 + r)**y - p
total = p + interest

year_round = round(y, 2)
rate_round = round(r * 100, 2)
captital_round = round(p, 2)
interest_round = round(interest, 2)
total_round = round(total, 2)

header = 'Simulation for ' + str(year_round) + ' years'

captital_line = 'Capital: $' + str(captital_round) 
interest_line = 'Interest: $' + str(interest_round) 

print(header)
print(captital_line)
print(interest_line)

# fancy way of doing this

total_txt = "$%.2f" % (total) 
print('total:'.ljust(20) + total_txt)

interst_txt = "$%.2f" % (interest) 
print('interest:'.ljust(20) + interst_txt)