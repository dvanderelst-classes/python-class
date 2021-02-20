#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 20 15:31:58 2021

@author: dieter
"""

import pandas
data =pandas.read_csv('self_esteem.csv', sep='\t')

usa = data.query('country == "US"')