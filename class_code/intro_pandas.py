#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  9 14:20:26 2021

@author: dieter
"""

import pandas
data = pandas.read_csv('https://tinyurl.com/y894ft6g',index_col=0,na_values='NA')
print(data.head())

data['Months'] = data['Age'] * 12
data['Kids'] = data['Months'] < 15

# Exercise 1

# Read in the cars.txt file (download it or read it in from http://tinyurl.com/ybbw5gwg)
data = pandas.read_csv('http://tinyurl.com/ybbw5gwg',index_col=0,na_values='NA')
# Print the first lines of the data
print(data.head(7))
# Print the column names
print(data.dtypes)
print(data.columns)
# Calculate the difference in mpg on the highway and the city, add this difference as a new variable to the data frame.
data['MGP.diff'] =  data['MPG.highway'] - data['MPG.city']

# Exercise 2

from matplotlib import pyplot
# Read in data
data = pandas.read_csv('http://tinyurl.com/y6orr2bg',index_col=0)
# Add new variable
data['dnum'] = data['mnum'] - data['fnum']
# Add diffpct
data['diff_pct'] = 100 * (data['mwage'] - data['fwage']) / data['fwage']

pyplot.plot(data['age'], data['diff_pct'])
pyplot.plot(data['age'], data['dnum'])
