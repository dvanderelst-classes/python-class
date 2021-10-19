#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 19 14:56:53 2021

@author: dieter
"""
import pandas

data = pandas.read_csv('pizzasize.csv', index_col=0)

#Exercise 1
#Write code that creates a dataframe (table) that lists for each store and each CrustDescription, the average pizza diameter.

grp = data.groupby(['Store', 'CrustDescription'])
means = grp.mean()
means = means.reset_index()

#Exercise 2
#Write code that creates a dataframe (table) that lists for each store and each CrustDescription, the maximum pizza diameter.

grp = data.groupby(['Store', 'CrustDescription'])
maxes = grp.max()
maxes = maxes.reset_index()

#Exercises 3
#Write code that creates a dataframe (table) that lists for each store and each CrustDescription, 
#the average pizza area. 
#Reorganize the table to have CrustDescription as rows and store as columns.


grp = data.groupby(['Store', 'CrustDescription'])
means = grp.mean()
means = means.reset_index()

table = means.pivot(columns='Store',index='CrustDescription', values='Diameter')
print(table)