#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 23 14:27:58 2021

@author: dieter
"""
import pandas
from matplotlib import pyplot


data = pandas.read_csv('https://tinyurl.com/ib5wvbqc') # Data is available in the 'data' folder.
data.head() 

data = data.query('Age < 40')

pyplot.plot(data.Height, data.Weight, marker='o', linestyle='None', color='#66c2a5')
pyplot.xlabel('Height (cm)')
pyplot.ylabel('Weight (kg)')
pyplot.title('Weight as a function of height')


women = data.query('Gender==0') 
men = data.query('Gender==1')
men.head()

# Start new figure
pyplot.figure()

pyplot.plot(women.Height, women.Weight, marker='o', linestyle='None', color='#66c2a5', alpha=0.5)
pyplot.plot(men.Height, men.Weight, marker='s', linestyle='None', color='red', alpha=0.5)
pyplot.xlabel('Height (cm)')
pyplot.ylabel('Weight (kg)')
pyplot.title('Weight as a function of height')

pyplot.legend(['Women', 'Men'])
pyplot.savefig('my_plot.png', dpi=300)
pyplot.savefig('my_plot.pdf')

# Exercise 1
import numpy 

data['age_band'] = numpy.floor((data['Age'] / 5)) * 5
grp = data.groupby('age_band')
mns = grp.mean()
mns = mns.reset_index()

pyplot.figure()
pyplot.plot(mns['age_band'], mns['Height'], marker='s')