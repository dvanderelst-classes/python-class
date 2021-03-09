#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  2 14:10:59 2021

@author: dieter
"""
import pandas
import seaborn
from matplotlib import pyplot

# Running the pearson correlation
from scipy.stats import pearsonr
from scipy.stats import ttest_ind
from scipy.stats import kruskal


data = pandas.read_csv('https://tinyurl.com/ib5wvbqc') # Data is available in the 'data' folder.
data.head() 

result = pearsonr(data.Bicep, data.Weight)
print(result)

#
women = data.query('Gender==0')
men = data.query('Gender==1')

result = ttest_ind(women.Weight, men.Weight)
print(result)

result = kruskal(women.Weight, men.Weight)
print(result)

seaborn.histplot(hue='Gender', x='Weight', data=data, bins=25)