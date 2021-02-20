#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 18 13:54:29 2021

@author: dieter
"""
import pandas
import stats

link = 'http://tinyurl.com/y8ummdf9'
data = pandas.read_csv(link,index_col=0)

data = data.query('skullw < 56')

## Example 1
# Step 1
grp = data.groupby('Pop')

# Step 2
mns = grp.mean()

## Example 2

data['young'] = data.age < 3

# Step 1
grp = data.groupby(['Pop','young', 'site'])

# Step 2
mns = grp.mean()
std = grp.std()
mxs = grp.max()

# Step 3
mns_reset_indices = mns.reset_index()


data['young'] = data.age < 3
grp = data.groupby(['Pop','young'])
table = grp.mean()

## Using stats module

result = stats.group(data, ['Pop','age'], 'mean')

## Pivoting
table = result.pivot(index='age', columns='Pop', values='taill')
print(table)

