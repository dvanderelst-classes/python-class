#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 11 14:43:58 2021

@author: dieter
"""

# Titanic

import pandas
data = pandas.read_csv('https://tinyurl.com/y894ft6g',index_col=0,na_values='NA')

selection1 = data.query('Age > 25 and Survived == 1 and SexCode == 0')
count = selection1.shape[0]

selection2 = data.query('SexCode == 0 and PClass == "1st"')
count = selection2.shape[0]

selection3 = data.query('SexCode == 0 and Survived == 1')
count_survived = selection3.shape[0]

selection3 = data.query('SexCode == 0')
count_all = selection3.shape[0]

print(count_survived/count_all)

# car data

link = 'https://tinyurl.com/yc5pxn7f'
cars = pandas.read_csv(link,index_col=0)

cars['pct_diff'] = 100 * (cars['MPG.highway'] - cars['MPG.city']) / cars['MPG.city']
selected_cars = cars.query('pct_diff > 25') 
print(selected_cars.head())