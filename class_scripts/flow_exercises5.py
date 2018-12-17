#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 27 15:04:39 2018

@author: dieter
"""

import random
n = random.randint(0,21)

guess = n + 1
nr_guess = 0
while guess!=n:
    guess = input('guess:')
    guess = int(guess)
    if guess < n: print('too low')
    if guess > n: print('too high')
    nr_guess = nr_guess + 1

print('correct', nr_guess)
    