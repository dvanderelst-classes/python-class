#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 17 14:41:23 2019

@author: dieter
"""

import pandas

url = 'http://tinyurl.com/ybbw5gwg'
data = pandas.read_csv(url, index_col=0)


# Select all cars with at least 25 mpg in the city.
data['city'] = data["MPG.city"]
over_25 = data.query('city >= 25')
over_25.city.hist()

# Select all BMW's
all_bmws = data.query('Manufacturer == "BMW"')
all_fords = data.query('Manufacturer == "Ford"')


both = data.query('Manufacturer == "BMW" or Manufacturer == "Ford"')

makes = data.query('Manufacturer in ["BMW", "Ford", "Acura"]')
# Are there any Large cars with more than 25 mpg in the city?
econ_over_25 = data.query('city >= 25 and Type == "Large"')

econ_over_25 = over_25.query('Type == "Large"')
# Which cars use over 50% more fuel on the highway than they do in the city?
data['gpm_city'] = 1 / data['MPG.city'] 
data['gpm_highway'] = 1 / data['MPG.highway'] 

data['increase'] =  100 * (data['gpm_highway'] - data['gpm_city']) / data['gpm_city']
selected = data.query('increase >= 150')


