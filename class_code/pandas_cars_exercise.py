#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 12 15:01:48 2019

@author: dieter
"""

import pandas

url = 'http://tinyurl.com/ybbw5gwg'
data = pandas.read_csv(url, index_col=0)

file = 'cars93.csv'
data = pandas.read_csv(url, index_col=0)

print(data.head())

a = data.columns
print(a)

data['difference'] = data['MPG.city'] - data['MPG.highway']