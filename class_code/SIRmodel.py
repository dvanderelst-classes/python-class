#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 29 13:57:27 2022

@author: dieter
"""
from matplotlib import pyplot

susceptible = 1000000
infected = 10
recovered = 0

N = susceptible + infected + recovered

beta = 0.5
gamma = 1/10

track_I = []
track_S = []
track_R = []

for day in range(100):

    delta_S =  - (beta * infected * susceptible) / N
    delta_I = ((beta * infected * susceptible) / N) - gamma * infected
    delta_R = gamma * infected
    
    susceptible = susceptible + delta_S
    infected = infected + delta_I
    recovered = recovered + delta_R
    
    track_S.append(susceptible)
    track_I.append(infected)
    track_R.append(recovered)
    

pyplot.figure()    
pyplot.plot(track_S)
pyplot.plot(track_I)
pyplot.plot(track_R)