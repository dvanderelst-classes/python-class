#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  6 14:06:06 2022

@author: dieter
"""
import time

v1 = 'donald'
v2 = 'duck'
v3 = v1 + ' ' + v2
print(v3)
print()
v1_caps_a = str.capitalize(v1)
v1_caps_b = v1.capitalize()


v2_caps_a = str.capitalize(v2)
v2_caps_b = v2.capitalize()

v3_caps = v1_caps_b + ' ' + v2_caps_b

print((v3_caps + ' ') * 10 )
print()
# madness
all_upper = str.upper(v3_caps)
print(all_upper)

# like a normal human bing
all_upper = v3_caps.upper()
print(all_upper)

current_time = 'current time is ' + time.asctime()
print(current_time)


tale_of_two_cities = 'It was the best of times, it was the worst of times, it was the age of wisdom, it was the age of foolishness, it was the epoch of belief, it was the epoch of incredulity, it was the season of Light, it was the season of Darkness, it was the spring of hope, it was the winter of despair, we had everything before us, we had nothing before us, we were all going direct to Heaven, we were all going direct the other way – in short, the period was so far like the present period, that some of its noisiest authorities insisted on its being received, for good or for evil, in the superlative degree of comparison only.'
length_of_the_string = len(tale_of_two_cities)
print(length_of_the_string)
number_of_es = tale_of_two_cities.count('times')


lst = [1,2,3,4,5,6,8, 'elephant']
lst[1:3] = ['bear', 'penguin', 'tiger',  'ct']

















