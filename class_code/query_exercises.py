#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 12:05:41 2019

@author: dieter
"""

# Let's read in some data to work with
import pandas
file_location = 'https://tinyurl.com/y894ft6g'
data = pandas.read_csv(file_location,index_col=0,na_values='NA')
data.head()

# how many >25 males?
selection = data.query('Sex == "male" and Age > 25')
print(selection.shape)

# 1st female
selection = data.query('Sex == "female" and PClass == "1st"')
print(selection.shape)

# 1st female, survived
selection = data.query('Sex == "female" and PClass == "1st" and Survived == 1')
print(selection.shape)


