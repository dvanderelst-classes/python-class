#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 25 14:16:06 2021

@author: dieter
"""
import pandas
from matplotlib import pyplot
import numpy 

data = pandas.read_csv('https://tinyurl.com/2wtcmakj',sep='\t')


data = data.query('age < 75 and age > 17 and accuracy <=100 and accuracy >=0')
data = data.query('country in ["US","GB","CA"]')

grp = data.groupby('country')
mns = grp.mean()
mns = mns.reset_index()

pyplot.plot(mns.country,mns.age, marker='s')

data['future'] = data.Q1 + data.Q2 - data.Q3 - data.Q4
data['age_group'] = 5 * numpy.floor(data.age/5)

grp = data.groupby(['country','age_group'])
mns = grp.mean()
mns = mns.reset_index()

us = mns.query('country=="US"')
ca = mns.query('country=="CA"')
gb = mns.query('country=="GB"')

pyplot.figure()
pyplot.plot(us.age_group, us.future)
pyplot.plot(ca.age_group, ca.future)
pyplot.plot(gb.age_group, gb.future)
pyplot.legend(['US','CA','GB'])


# Eample of bar plot

pyplot.figure()
pyplot.bar(mns.country, mns.age)
pyplot.ylim(68, 75)

pyplot.figure()
pyplot.bar(range(4), [1,2,2,4])


pyplot.figure()
pyplot.barh(range(4), [1,2,2,4])