#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 12 11:57:35 2019

@author: dieter
"""
import random
number_to_guess = random.randint(1,20) 
guess = -100
number_of_guesses = 0
while not guess == number_to_guess:
    guess = int(input('What isyour guess?:'))
    if guess > number_to_guess: print('too high')
    if guess < number_to_guess: print('too low')
    number_of_guesses = number_of_guesses + 1
print(number_of_guesses)