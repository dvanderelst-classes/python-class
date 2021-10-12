#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  7 14:16:38 2021

@author: dieter
"""

import pandas
data = pandas.read_csv('cars.txt', sep=' ', na_values='*')
print('data size:', data.shape)
print('data type', data.dtypes)
print('column names', data.columns)


data['hpc'] = data['horsepower'] / data['cylinders']
data['low_hpc'] = data['hpc']  < 25

print(data.head(5))