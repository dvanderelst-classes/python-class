#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 14 14:10:09 2021

@author: dieter
"""
import pandas
from matplotlib import pyplot

# Exercise 1

data = pandas.read_csv('http://tinyurl.com/ybbw5gwg', index_col=0, na_values='nan')
fist_lines = data.head(10)
print(fist_lines)
print(data.columns)

#Calculate the difference in mpg on the highway and the city, add this difference as a new variable to the data frame.

data['MPG.diff'] = data['MPG.highway'] - data['MPG.city']


# Exercise 2

data = pandas.read_csv('http://tinyurl.com/y6orr2bg', index_col=0, na_values='nan')
data['diff'] = data['mnum'] - data['fnum']
data['pay'] = 100 * (data['mwage'] - data['fwage']) / data['fwage']

pyplot.plot(data['age'], data['pay'])
pyplot.show()

pyplot.plot(data['age'], data['diff'])
pyplot.show()


