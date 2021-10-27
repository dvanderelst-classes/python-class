#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 26 14:04:26 2021

@author: dieter
"""
import pandas
from matplotlib import pyplot

url = 'https://raw.githubusercontent.com/dvanderelst-python-class/python-class/fall2021/13_Matplotlib_Advanced/data/body.csv'
data = pandas.read_csv(url) 

pyplot.scatter(data['Weight'],data['Height'], c=data['Waist'], cmap='hot')
pyplot.colorbar()

#pyplot.plot(data['Weight'],data['Height'], marker='o', linestyle='None')

pyplot.figure()
pyplot.hist(data['Weight'], bins=15, color='red')
pyplot.hist(data['Height'], bins=15, color='green')

pyplot.figure()
women = data.query('Gender == 0')
men = data.query('Gender == 1')

pyplot.hist(men.Bicep,alpha=1, bins=25);
pyplot.hist(women.Bicep,alpha=0.5, bins= 25);
pyplot.legend(['Men', 'Women']);

pyplot.figure()
surf = pyplot.hist2d(data['Height'],data['Weight'], bins=25, cmap='jet');
pyplot.colorbar()
pyplot.xlabel('Height');
pyplot.ylabel('Weight');


pyplot.figure(figsize=(10,2.5))

pyplot.subplot(1,4,1)

pyplot.scatter(data['Weight'],data['Height'], c=data['Waist'], cmap='hot')
pyplot.xlabel('something')
pyplot.ylabel('also something')


pyplot.subplot(1,4,2)
pyplot.hist(men.Bicep,alpha=1, bins=25)
pyplot.xlabel('something')
pyplot.ylabel('also something')

pyplot.subplot(1,4,3)
pyplot.hist2d(data['Height'],data['Weight'], bins=25, cmap='jet')
pyplot.xlabel('something')
pyplot.ylabel('also something')

current_axes = pyplot.gca()
current_axes.annotate('Look at this !', xy=(170, 60), xytext=(160, 90), color='white',
            arrowprops=dict(facecolor='white', shrink=0.1))


pyplot.subplot(1,4,4)
pyplot.hist(data['Height'], bins=15, color='green')
pyplot.xlabel('something')
pyplot.ylabel('also something')


pyplot.tight_layout()
