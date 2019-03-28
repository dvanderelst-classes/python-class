#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 28 11:11:17 2019

@author: dieter
"""

import pandas
data = pandas.read_csv('films.dat', sep='\t')

# Question 1

selection = data.query('Year > 1979 and Year < 1991')
selection = data.query('Year >= 1980 and Year <= 1990')

# Question 2

selection = data.query('Rating == 1')

# Question 3

search_year = 1000
lower_bound = search_year - 5
selection = data.query('Year > @lower_bound and Year <= @search_year')
number_found = selection.shape[0]
if number_found == 0: print('nothing found')

# Question 4
ratio = data['Cast'] / data['Length'] 
data['ratio'] = data['Cast'] / data['Length'] 
selection = data.query('ratio >=0.1')

