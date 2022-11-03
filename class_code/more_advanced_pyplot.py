#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  3 13:54:14 2022

@author: dieter
"""

import pandas
from matplotlib import pyplot

#url = 'https://raw.githubusercontent.com/dvanderelst-python-class/python-class/8ca1259f94c29e3772a4977b93824b6e1fe5a5a7/14_Matplotlib_Advanced/data/body.csv'
#data = pandas.read_csv(url)

# pyplot.figure(figsize=(8, 3))
# pyplot.subplot(1,3,1)
# pyplot.hist(data.Weight)

# pyplot.subplot(1,3,2)
# pyplot.scatter(data.Age, data.Height)

# pyplot.subplot(1,3,3)
# pyplot.scatter(data.Age, data.ChestDia)

# pyplot.tight_layout()
# pyplot.savefig('my_figure.png', dpi=300)


#######
pyplot.style.use('default')
pyplot.style.use('ggplot')

y1_values = [12,34,56,12,34]
x1_values = [0,2,4,6,8]

y2_values = [12,20,5,30,14]
x2_values = [0.8,2.8,4.8,6.8,8.8]

pyplot.figure()
pyplot.bar(x1_values, y1_values)
pyplot.bar(x2_values, y2_values)

labels = ['elk', 'moose', 'deer', 'caribou', 'reindeer']
pyplot.xticks([0.4,2.4,4.4, 6.4, 8.4], labels)

pyplot.legend(['male', 'female'])
pyplot.ylabel('tapdance ability')


###
# pyplot.figure()
# s = pyplot.hist2d(data.Height, data.Weight, cmap='cool', bins=10)
# pyplot.colorbar()

# pyplot.figure()
# pyplot.contourf(s[0], cmap='hot')
# pyplot.colorbar()







