#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 21 11:18:15 2019

@author: dieter
"""

def calc_tip1(a):
    result = a * 0.2
    return result

# tax is in percentage
def calc_tip2(meal, tax_pct, tip_pct):
    tax_amount = meal * tax_pct / 100
    total_meal = meal + tax_amount
    tip_amount = total_meal* tip_pct / 100
    total_amount = tip_amount + total_meal
    return tax_amount, tip_amount, total_amount


def print_report(tax_amount, tip_amount, total_amount):
    print('tax:', tax_amount)
    print('tip:', tip_amount)
    print('total:', total_amount)
    
    
    
a,b,c = calc_tip2(100,10,20)
d = print_report(a,b,c)

    