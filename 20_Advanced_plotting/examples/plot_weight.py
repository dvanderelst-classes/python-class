#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 21 14:09:22 2017

@author: dieter
"""
from matplotlib import pyplot
import numpy
data = numpy.loadtxt('body.txt',delimiter='\t')
print(data[0:3,:])

age = data[:,0]
weight = data[:,1]
height = data[:,2]
gender = data[:,3]

women = data[gender==0,:]
men = data[gender==1,:]

## Get the data for men and women
hm = men[:,2]
wm = men[:,1]
hw = women[:,2]
ww = women[:,1]
#
## Define the colors
red = "#cc0000"
blue = "#6666ff"
#
## Set the style and the figure size
pyplot.style.use('bmh')
pyplot.figure(figsize=(15, 7))
#
##Let's try this later.
##pyplot.xkcd()
#
## We'll make a figure with three panels panels
pyplot.subplot2grid((2,2), (0, 0), rowspan=2)
#
## fit a regression line to the men data
x = [numpy.min(hm),numpy.max(hm)]
z = numpy.polyfit(hm, wm, 1)
pm = numpy.poly1d(z)
#
## Plot the data for the men
pyplot.scatter(hm,wm,color=red, alpha=0.5)
pyplot.plot(x,pm(x),'-',color=red)
#
## fit a regression line to the women data
x = [numpy.min(hw),numpy.max(hw)]
z = numpy.polyfit(hw, ww, 1)
pw = numpy.poly1d(z)
#
## Plot the women data
pyplot.scatter(hw,ww,color=blue, alpha=0.5)
pyplot.plot(x,pw(x),'-',color=blue)
#
## Add a legend 
pyplot.legend(['Men','Women'])
#
## Add the axis labels
pyplot.xlabel('Height (cm)')
pyplot.ylabel('Weight (kg)')
#
#pyplot.text(142,125,'(a)',fontsize=12)
#
## Now start the second panel
pyplot.subplot2grid((2,2), (0, 1),rowspan=1)
#
xrange = numpy.arange(150,200,1)
ym = pm(xrange)
yw = pw(xrange)
diff = ym - yw
pyplot.plot(xrange, diff,color='k')
pyplot.xlabel('Height (cm)')
pyplot.ylabel('Weight Difference (kg)')
pyplot.text(150,12,'(b)',fontsize=12)
#
## Now start the third panel
pyplot.subplot2grid((2,2), (1, 1))
settings = pyplot.hist(men[:,0],alpha=0.5,color=red)
#
## Reuse the bins used for the men in plotting the women
bins_men = settings[1]
pyplot.hist(women[:,0],alpha=0.5,color=blue,bins=bins_men)
pyplot.xlabel('Age')
pyplot.ylabel('Count')
pyplot.text(10,70,'(c)',fontsize=12)
