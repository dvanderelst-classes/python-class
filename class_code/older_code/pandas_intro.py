#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 12 14:21:42 2019

@author: dieter
"""

import pandas

data = pandas.read_csv('https://tinyurl.com/y894ft6g',index_col=0,na_values='NA')
print(data.head(5))

data['Months'] = data['Age'] * 12