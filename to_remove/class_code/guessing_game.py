#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 14 11:30:10 2019

@author: dieter
"""

import random
incorrect = True
number_of_guesses = 0
lowest = 0
highest = 20
while incorrect:
    #guess = random.randint(lowest,highest)
    guess = int((lowest + highest)/2)
    print('I guessed', guess)
    feedback = input('too high, too low or correct:')
    
    if feedback == 'h': highest = guess - 1
    if feedback == 'l': highest = guess + 1
    if feedback == 'c': incorrect = False
