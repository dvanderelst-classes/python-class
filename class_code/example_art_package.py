#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 30 13:12:15 2022

@author: dieter
"""

import art

result = art.text2art('This is art')
print(result)

result = art.text2art('ABC', font = 'block')
print(result)