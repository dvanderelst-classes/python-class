#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  7 11:30:58 2019

@author: dieter
"""

##
## Writes the multiplication table
##

a = 6
for b in range(1,10):
    print(a,'X',b,'=',a * b)
    

##
## Writes the a number pyramid to the screen
##
for b in range(1,10):
    print(str(b) * b)
    
##
## Writes the a number pyramid to the screen, option 2
##
    
for a in range(1,10):
    for b in range(0,a):
        print(a,end='')
    print()

#
# Print out whether letter is vowel
#    
vowels = 'aeuiyo'
word = 'pneumonoultramicroscopicsilicovolcanoconiosis'
for letter in word:
    if letter in vowels:
        print(letter,'is a vowel')
    if not letter in vowels:
        print(letter,'is not a vowel')

#
# Print out whether letter is vowel option 2
#    

vowels = 'aeuiyo'
word = 'pneumonoultramicroscopicsilicovolcanoconiosis'
for letter in word:
    if letter in vowels:
        print(letter,'is a vowel')
    else:
        print(letter,'is not a vowel')
        
        
for x in range(1000,2500):
    #check whether x can divided by 3
    #if so, print x
    
    