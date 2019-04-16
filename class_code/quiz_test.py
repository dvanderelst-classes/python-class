#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 16 11:48:53 2019

@author: dieter
"""

import pandas
from matplotlib import pyplot
import seaborn
from course import stats
data = pandas.read_csv('Wages.csv')

# Get average wage per level of schooling
grp = data.groupby(['school'])
mns = grp.mean()
mns = mns.reset_index()

# Create a graph that plots the average wage as a 
# function of the years of schooling. 
# Add labels to the axes.
pyplot.plot(mns.school, mns.wage, '.-')
pyplot.xlabel('Years of schooling')
pyplot.ylabel('Average Wage')
pyplot.show()

# The same but using seaborn
seaborn.lineplot(x='school', y='wage', hue = 'sex', data= data)

# Run  a linear regression with years of schooling 
# as the independent variable  and wage as dependent 
# variable. Print the summary to the screen.
pyplot.figure()
result = stats.simple_regression('wage', 'school', data)
print(result['summary'])

#
# Question 2
#
result = stats.linear_regression('wage ~ school + exper', data)
print(result['summary'])

#also test for gender

result = stats.linear_regression('wage ~ school + exper * C(sex)', data)
print(result['summary'])

