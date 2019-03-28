#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 28 11:53:07 2019

@author: dieter
"""
import pandas
data = pandas.read_csv('films.dat', sep='\t')
selection = data.query('Year >= 1980 and Year <= 1990')

search_year = 1990
selection = data.query('Year <= @search_year')

data['ratio'] = data['Cast'] / data['Length']

print(data.describe())