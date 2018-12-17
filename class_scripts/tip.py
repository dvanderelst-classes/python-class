#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  4 14:18:42 2018

@author: dieter
"""
import random

def meal_tip(meal, tip_pct=20, tax_pct=6):
    meal = (meal * tax_pct/100) + meal
    tip = (meal * tip_pct/100)
    total = tip + meal
    return meal, tip, total

ml, tp, tt = meal_tip(100)
#print(ml, tp, tt)
n = 1
while n > 0.1:
    n = random.random()
    print(n)