#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov  2 13:59:50 2021

@author: dieter
"""
import pandas
import stats

data = pandas.read_csv('https://tinyurl.com/ib5wvbqc') 

result = stats.simple_regression('Weight','Bicep', data)
print(result['summary'])

formula = 'Weight ~ Age + Bicep + Height'
result = stats.linear_regression(formula, data)
print(result['summary'])

#W = -76 + 0.09 * Age + 2.0 * Bicep + 0.45 * Height

formula = 'Weight ~ Height * C(Gender)'
result = stats.linear_regression(formula, data)
print(result['summary'])
