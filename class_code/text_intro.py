#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  2 14:41:01 2021

@author: dieter
"""

my_string = """It was the best of times, it was the worst of times, it was the age of wisdom, 
it was the age of foolishness, it was the epoch of belief, it was the epoch of incredulity,  it was the season of Light,
it was the season of Darkness, it was the spring of hope, it was the winter of despair,
we had everything before us, we had nothing before us, we were all going direct to Heaven, we were all going direct the other way – in short, the period was so far like the present period,
that some of its noisiest authorities insisted on its being received, for good or for evil,
in the superlative degree of comparison only."""

l = len(my_string)
print(l)

c = my_string.count('e')
print(c)

number = 5

z = number - 1
drink = 'soda'

line = 'x bottles of y on the wall. x bottles of y. If one of those bottles should happen to fall, z bottles of y on the wall.'

line = line.replace('x', str(number))
line = line.replace('y', drink)
line = line.replace('z', str(z))

print(line)