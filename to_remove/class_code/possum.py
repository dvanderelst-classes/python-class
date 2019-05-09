#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 28 11:57:36 2019

@author: dieter
"""

import pandas
link = 'http://tinyurl.com/y8ummdf9'
data = pandas.read_csv(link,index_col=0)
data.head()

stats = data.describe()
print(stats)

print(data.age.sem())

print(data.Pop.value_counts())