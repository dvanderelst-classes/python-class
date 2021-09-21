#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 21 13:56:20 2021

@author: dieter
"""
import random
import math
#Write a program to print the numbers from 1 to 10.

r = range(1,11)
r = list(r) #<- this is not necessary
for elephant in r:
    print(elephant)
    
# Write a program that prints the multiplication table for a number. For example, for n=5, the program would print,

table_num = 5
multipliers = range(0, 10)
multipliers = list(multipliers) #<- this is not necessary
for multi in multipliers:
    result =  multi * table_num
    print(multi, 'X', table_num, '=', result)
    

# Write a number guessing game (option 1).
# secret_number = random.randint(0, 101)
# guess = -100

# while guess != secret_number:   

#     guess = input('Guess:')
#     guess = int(guess)
    
#     if guess > secret_number:
#         print('Too high')
        
#     if guess < secret_number:
#         print('Too low')

# print('Well done, you!')


# Write a number guessing game (option 2).
# secret_number = random.randint(0, 101)

# while True:   

#     guess = input('Guess:')
#     guess = int(guess)
    
#     if guess > secret_number:
#         print('Too high')
        
#     if guess < secret_number:
#         print('Too low')
        
#     if guess == secret_number:
#         break

# print('Well done, you!')


#Write a program that gets the `x` and `y` coordinates of projectile for a range of times `t`
from matplotlib import pyplot


time_points = range(0,2500) # milliseconds
time_points = list(time_points) #<- this is not necessary

v = 10
g = 10
angle = math.radians(45)

x_coordinates = []
y_coordinates = []

for t in time_points:
    x = v * t/ 1000 * math.cos(angle)
    y = v * t/ 1000 * math.sin(angle) - 0.5  * g * (t/1000)**2
    print(x, y)
    x_coordinates.append(x)
    y_coordinates.append(y)

pyplot.plot(x_coordinates, y_coordinates)
pyplot.grid()
pyplot.show()



















