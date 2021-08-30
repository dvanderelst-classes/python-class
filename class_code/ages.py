#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 17 14:08:54 2019

@author: dieter
"""
import pandas

url = 'http://tinyurl.com/y6orr2bg'

data = pandas.read_csv(url, index_col=0)

data['difference'] = data.mnum - data.fnum
data['difference'] = data['fnum'] - data['mnum']

data['gap'] = 100 * (data['mwage'] - data['fwage']) / data['fwage'] 

data.gap.plot()