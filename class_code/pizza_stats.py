#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 18 14:58:23 2021

@author: dieter
"""

import pandas
import math
data = pandas.read_csv('pizzasize.csv', index_col=0)

#Step 1: group data
grp = data.groupby(['Store', 'CrustDescription'])
#Step 2: get the statistics
mns = grp.mean()
#Step 3: reset index
mns = mns.reset_index()
mns['surf'] = (mns['Diameter']/2)**2 * math.pi