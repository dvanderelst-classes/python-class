#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  2 14:10:59 2021

@author: dieter
"""
import pandas
import seaborn
from matplotlib import pyplot


colors = ['Sunset Orange', 'Inchworm']
my_colors = seaborn.crayon_palette(colors)

seaborn.palplot(my_colors)

data = pandas.read_csv('https://tinyurl.com/ib5wvbqc') # Data is available in the 'data' folder.
data.head() 

data['Sex'] = 'Female'
data['Sex'][data.Gender==1] = 'Male'

seaborn.lmplot(x='ChestDepth', y='Forearm', data=data,)

seaborn.lmplot(x='ChestDepth', y='Forearm', hue ='Sex', data=data,)

seaborn.lmplot(x='ChestDepth', y='Forearm',col='Sex', data=data, palette=my_colors)
pyplot.ylabel('The length of the forearm')

pyplot.figure()

data['Group'] = data.Age < 25

pyplot.figure()
seaborn.barplot(x='Group', y='Weight', hue='Gender', data=data, palette=my_colors)

pyplot.figure()
seaborn.boxplot(x='Group', y='Weight', hue='Gender', data=data, palette=my_colors)

pyplot.figure()
seaborn.catplot(x='Group', y='Weight', hue='Gender', data=data, palette=my_colors, kind='point')


pyplot.figure()
seaborn.catplot(x='Group', y='Weight', hue='Gender', data=data, palette=my_colors, kind='swarm')

pyplot.figure()
seaborn.catplot(x='Group', y='Weight', hue='Gender', data=data, palette=my_colors, kind='violin')