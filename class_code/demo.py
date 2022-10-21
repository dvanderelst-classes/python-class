#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 20 14:08:10 2022

@author: dieter
"""

import stats # for this to work, you have to put the stats.py file in the same directory
import pandas
import math

link = 'http://tinyurl.com/y8ummdf9'
data = pandas.read_csv(link,index_col=0)


# Grouping
data['young'] = data.age < 3
result1 = stats.group(data, ['age', 'pop'], 'mean')

table = result1.pivot(index = 'Pop', columns='age', values = 'taill')

########### Exercise 1

url = 'https://raw.githubusercontent.com/dvanderelst-python-class/python-class/fall2022/11_Pandas_Statistics/data/pizzasize.csv'
data = pandas.read_csv(url)
# Write code that creates a dataframe (table) that lists for 
# each store and each CrustDescription, the average pizza diameter.


results = stats.group(data, ['store', 'CrustDescription'], 'mean')

grp = data.groupby(['Store', 'CrustDescription'])
results = grp.Diameter.mean() # or results = grp['Diameter'].mean() 
results = results.reset_index()

########### Exercise 2

grp = data.groupby(['Store', 'CrustDescription'])
results2 = grp.Diameter.max() # or results = grp['Diameter'].mean() 
results2 = results2.reset_index()

########### Exercise 3

data['Area'] = (data['Diameter'] / 2) ** 2 * math.pi
grp = data.groupby(['Store', 'CrustDescription'])
results3 = grp.Area.mean()
results3 = results3.reset_index()

table = results3.pivot(index = 'Store', columns = 'CrustDescription', values='Area')



