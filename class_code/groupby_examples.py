#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 19 14:07:15 2021

@author: dieter
"""
import pandas
link = 'http://tinyurl.com/y8ummdf9'
data = pandas.read_csv(link,index_col=0)
data.head()


# Quick descr. of numericals
d  = data.describe()
print(d['age'])

# counting cat. variables
pop_var = data['Pop']
pop_var_count = pop_var.value_counts()


# using groupby- example 1

data['juvenile'] = data['age'] <= 2

#Step 1: telling pandas how to group
grp = data.groupby('juvenile')
# Step 2: get the statistics
means = grp.mean()
vrs = grp.var()
# Step: reseting index
means = means.reset_index()
vrs = vrs.reset_index()

#filter
j = means.query('juvenile == True')


# using groupby- example 2


#Step 1: telling pandas how to group
grp = data.groupby(['juvenile', 'Pop'])
# Step 2: get the statistics
means = grp.mean()
vrs = grp.var()
# Step: reseting index
means = means.reset_index()
vrs = vrs.reset_index()


print('-------------------------')
table = means.pivot(index='Pop', columns='juvenile', values='taill')
table = table.round(2)
print(table)


writer = pandas.ExcelWriter('output.xlsx', engine = 'xlsxwriter')
table.to_excel(writer, sheet_name = 'table1')
means.to_excel(writer, sheet_name = 'means')
writer.save()
writer.close()




