#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 13 19:34:22 2017

@author: dieter
"""

word = 'python'
guesses = 0
tried = []
while 1:
    guesses = guesses + 1
    letter = 'r'
    letter = input('guess >')
    print(letter)
    tried.append(letter)
    
    masked = word[:]
    
    for x in masked:
        if x not in tried: masked =masked.replace(x, '*')
    print(masked)
    
    if '*' not in masked: 
        print('Your win')
        break
    if guesses > 10:
        print('Your loose')
        break
    
    
    