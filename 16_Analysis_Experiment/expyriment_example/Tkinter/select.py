#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 15 15:16:38 2017

@author: dieter
"""
import random

f = open('raw.txt','r')
lines = f.readlines()
f.close()

random.shuffle(lines)

short_e = []
long_e = []
short = []
long = []

for x in lines:
    x = x.replace('\n','')
    if x.count('E') < 2:
        long_word = len(x)  > 7
        e_word = x.count('E') == 1
    
        if long_word and e_word: long_e.append(x)
        if long_word and not e_word: long.append(x)

        if not long_word and e_word: short_e.append(x)
        if not long_word and not e_word: short.append(x)

cnt = 15
for x in range(0,cnt): print(short[x],'short','negative')
for x in range(0,cnt): print(short_e[x],'short','positive')

for x in range(0,cnt): print(long[x],'long','negative')
for x in range(0,cnt): print(long_e[x],'long','positive')