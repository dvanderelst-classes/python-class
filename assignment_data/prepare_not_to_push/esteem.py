#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 20 15:31:58 2021

@author: dieter
"""

import pandas
from matplotlib import pyplot

data =pandas.read_csv('../self_esteem.csv', sep='\t')


for cnt in ['GB', 'US']:
    selection = data.query('country == @cnt and age > 0 and age < 50')

    grp = selection.groupby('age')
    mns = grp.mean()
    mns = mns.reset_index()
    pyplot.plot(mns.age, mns.Q1)

