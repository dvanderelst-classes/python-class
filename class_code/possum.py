#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 19 14:20:17 2019

@author: dieter
"""

import pandas
link = 'http://tinyurl.com/y8ummdf9'
data = pandas.read_csv(link,index_col=0)
data.head()


data = data.query('Pop == "Vic"')

# Longest animal
length = data['totlngth']
m = length.max()
std = length.std()


txt = "The animals had a mean length of %.2f cm and a standard devication of %.2f" %(m, std)
print(txt)

data['young'] = data.age < 3


grp = data.groupby(['Pop','young'])
table = grp.mean()
table = table.reset_index()
