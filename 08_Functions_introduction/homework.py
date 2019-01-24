# -*- coding: utf-8 -*-
"""
Created on Mon Nov 21 12:18:32 2016

@author: dieter
"""
import itertools
import numpy
import copy


def get_permutations():
    rg = [0, 1, 2, 4, 5, 6, 7, 8, 9]
    perms = itertools.permutations(rg)
    return perms


def count_consecutive(numbers):
    numbers = numpy.array(numbers)
    numbers.sort()
    diff = numpy.diff(numbers)
    selected = numpy.where(diff == 1)[0]
    count = numpy.size(selected) + 1
    return count


def convert(numbers):
    numbers = numpy.array(numbers)
    powers = numpy.logspace(0,len(numbers)-1,len(numbers))
    sm = numbers*powers
    sm = numpy.sum(sm)
    return sm

permutations = get_permutations()
counter = 0
for sequence in permutations:
    counter += 1
    #if counter > 1000000: break
    four_digit = sequence[0:4]
    five_digit = sequence[4:9]
    n1 = convert(four_digit)
    n2 = convert(five_digit)

    c0 = n1 * 3 == n2
    c1 = count_consecutive(four_digit) == 3
    if c0 and c1: print(n1,n2,n1*3)
