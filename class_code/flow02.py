#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  7 11:02:56 2019

@author: dieter
"""

import random    

wins_A = 0
wins_B = 0
choices = ['r','p', 's']

while wins_A < 3 and wins_B < 3:
    #choice_A = random.choice(choices)
    choice_A = input('choice:')
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