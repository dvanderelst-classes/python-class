#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 19 15:00:40 2019

@author: dieter
"""
import math
import pandas
data = pandas.read_csv('pizzasize.csv')

data['area'] = math.pi * (data['Diameter'] / 2)**2

### The Tree Lines
grp = data.groupby(['Store', 'CrustDescription'])
mns = grp.mean()
mns = mns.reset_index()