#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 20 14:01:48 2022

@author: dieter
"""
import random

###################################################################

my_string = 'zebras-are-cool-animals'
result = my_string.split('-')
print(result)

##################################################################

var1 = "This is the way the world ends. This is the way the world ends. This is the way the world ends. Not with a bang but a whimper."
result = var1.replace('ends', 'smurfs')
print(result)

names = ['Murugan Ansel', 'Ha-o-zinne Medb', 'Zacharias Wilheard', 'Leyla Gamila', 'Saska Katriona']
occupations = ['horticulturalist', 'magician', 'literary agent', 'locksmith', 'chimney sweep']
foods = ['camembert', 'avocado', 'cranberry sauce', 'chicken tikka masala', 'zebra']

random_name = random.choice(names)
random_occupation = random.choice(occupations)
random_food = random.choice(foods)

template = 'Hi my name is, %s. I am a %s and my favorite food is %s!' %(random_name, random_occupation, random_food)
print()
print(template)

name_bit = 'Hi my name is, ' + random_name + '. '
occ_bit = 'I am a ' + random_occupation + ' '
food_bit = 'and my favorite food is ' + random_food + '!'
all_of_it = name_bit + occ_bit + food_bit
print()
print(all_of_it)

################################################################

just_a_list = list(range(0,1001))
random.shuffle(just_a_list)
start = just_a_list[0]
last_one = just_a_list[-1]

################################################################

distance = 1
distance_in_feet = distance * 5280
distance_in_yards = distance * 1760
distance_in_inch = distance * 63360
distance_in_zebras = distance_in_inch / 90
print('A distance of', distance, 'miles is')
print(distance_in_feet, 'feet')
print(distance_in_yards, 'yards')
print(distance_in_inch, 'inch')
print(distance_in_zebras, 'zebras')

another_way = str(distance) + ' miles is'
print(another_way)

################################################################

word_to_check = 'racecar'
forward = list(word_to_check)
backward = list(word_to_check)
backward.reverse()
print(forward == backward)




