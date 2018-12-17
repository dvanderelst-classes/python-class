#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  2 14:17:33 2018

@author: dieter
"""

for x in range(1,51):
    if x%3==0 and x%5!=0: 
        print('Fizz')
    if x%5==0 and x%3!=0:
        print('Buzz')
    if x%5==0 and x%3==0: 
        print('FizzBuzz')
    if x%5!=0 and x%3!=0:
        print(x)
        
        
dictionary = {}
f = open('minions.txt')
lines = f.readlines()
for x in lines:
    x = x.replace('\n','')
    entry = x.split(',')
    dictionary[entry[1]] = entry[0]
    
    
text = 'i want three broken bomb'
text = text.split(' ')
translated_text = ''
keys = dictionary.keys()
for word in text:
    if word in keys: translated = dictionary[word]
    if word not in keys: translated = word
    translated_text = translated_text + translated + ' '
print(translated_text)


