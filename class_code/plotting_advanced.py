#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov  1 13:59:56 2022

@author: dieter
"""

import pandas
from matplotlib import pyplot

data = pandas.read_csv('cfcs.csv',sep='\t')
data = data.query('age < 60')

grp = data.groupby('age')
mns = grp.mean()
mns = mns.reset_index()

pyplot.plot(mns.age, mns.Q5)