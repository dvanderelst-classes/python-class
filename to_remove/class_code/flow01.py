#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  5 11:00:04 2019

@author: dieter
"""

a = 12
if a > 10:
    print('a is larger than 10')
    
    
############################
# What will ernie do ? - version 1
############################
    
temperature = 165
weekend = True

if temperature > 90:
    if weekend == True:
        print('outside')
    if weekend == False:
        print('work')

if temperature <= 90:
    if weekend == True:
        print('bed')
    if weekend == False:
        print('work')
        
############################
# What will ernie do ? - version 2
############################      

if weekend:
    if temperature > 90: 
        print('outside')
    if temperature<=90:
        print('bed')
    
if not weekend:
    print('goto work')
    
    
############################
# What will ernie do ? - version 3
############################      

if weekend:
    if temperature > 90: 
        print('outside')
    else:
        print('bed')
else:
    print('goto work')
    
    
####################### 
import random    

wins_A = 0
wins_B = 0
choices = ['r','p', 's']
choice_A = random.choice(choices)
choice_B = random.choice(choices)

if choice_A == 'r' and choice_B == 's': 
    wins_A = wins_A + 1
    
if choice_A == 'r' and choice_B == 'p': 
    wins_B = wins_B + 1
    
if choice_A == 'p' and choice_B == 's': 
    wins_B = wins_B + 1
    
if choice_A == 'p' and choice_B == 'r': 
    wins_A = wins_A + 1
    
if choice_A == 's' and choice_B == 'r': 
    wins_B = wins_B + 1
    
if choice_A == 's' and choice_B == 'p': 
    wins_A = wins_A + 1
    
print(wins_A, wins_B, choice_A, choice_B)