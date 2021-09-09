#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  9 14:05:39 2021

@author: dieter
"""

import random
import math

r = range(0,11)
r = list(r)
r.remove(3)
r.remove(5)
r.remove(8)

s = random.choice(r)
print(s)

s = random.sample(r, 1)
print(s)

#--------------------------------------

txt = "The first day of classes for the fall semester at the University of Cincinnati starts Monday, Aug. 23, and more than 46,700 students are expected to begin instruction with a more traditional fall term, focusing on in-person instruction and activities. "
txt = txt.replace('day', 'night')
txt = txt.replace('semester', 'term')
txt = txt.lower()
print(txt)

#------------------------
lst1 = ['elephant','monkey','turtle']
lst2 = [1,2,3,4]

animal_name = random.choice(lst1)
number = random.choice(lst2)

#-----------------------------------

p = 500 #this is the capital
r = 10 #rate, in percent
y = 5 #years or duration

interest = p * (r/100) * y
interest = p * (1 + (r/100))**y

print(interest)

#-------------------------------------
angle = 40 # in degrees
speed = 7
g = 10

angle_radians = math.radians(angle)

flight_time = 2 * speed *  math.sin(angle_radians) / g
distance = speed ** 2 * math.sin(2 * angle_radians) / g

print(flight_time, distance)


#--------------------------
# Quick example of data processing
import pandas
from matplotlib import pyplot
pyplot.style.use('ggplot')

url = 'https://raw.githubusercontent.com/dvanderelst-python-class/python-class/fall2021/scenarios/scenario_AdolescentBirthRate/birth.csv'
data = pandas.read_csv(url, index_col=0)

for region in ['Europe', 'Americas']:

    selected_region = data.query('region==@region')
    grp = selected_region.groupby('income_levels')
    mns = grp.mean()
    mns = mns.reset_index()
    
    pyplot.bar(mns.income_levels, mns.infant)

    us = data.query('country =="United States of America"')
    
    pyplot.bar(us.income_levels,us.infant, alpha=0.25)
    pyplot.savefig(region + '.pdf')
    
    pyplot.show()



