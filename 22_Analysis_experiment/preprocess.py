#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 26 15:12:18 2018

@author: dieter
"""
import pandas
data_file = 'data/data.csv'

f = open(data_file, 'r')
lines = f.readlines()
lines.pop(0)
f.close()

all_data = pandas.DataFrame()

for line in lines:
    line = line.rstrip(',\n')
    line = line.split(',')
    participant_gender = line[1]
    participant_name = line[2]
    participant_file = line[3]
    if len(participant_file) > 5: 
        data = pandas.read_csv('data/' + participant_file, header=None, sep='\s+')        
        n = len(data.columns)
        data[n] = participant_name
        data[n+1] = participant_gender        
        all_data = pandas.concat([all_data,data],ignore_index=True)
     
print(all_data.head)
names =['experiment', 'stimulus', 'response', 'color', 'tablerow', 'key', 'status', 'rt', 'name', 'gender']
all_data.columns = names
all_data.to_csv('data.csv', index=False)

##

correct = all_data.query('status==1 and rt < 1000')
grp = correct.groupby(['stimulus', 'response'])
mns = grp.mean()
print(mns)




