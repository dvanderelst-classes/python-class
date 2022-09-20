#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  8 14:04:56 2022

@author: dieter
"""

number = 5
drink='soda'

txt = 'x bottles of y on the wall. x bottles of y. If one of those bottles should happen to fall, z bottles of y on the wall.'

number_as_string = str(number)
txt = txt.replace('x', number_as_string)

txt = txt.replace('y', drink)

new_number_as_string = str(number - 1)
txt = txt.replace('z', new_number_as_string)


print(txt)