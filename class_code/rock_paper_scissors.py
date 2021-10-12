#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 23 14:04:46 2021

@author: dieter
"""

# some_variable = 1000000

import random

winner = 'computer'

score_user = 0
score_computer = 0

while score_user < 3 and score_computer < 3:
    computer_choice = random.choice(['R','P', 'S'])
    user_choice = input('your choice:')
    

    if computer_choice == 'R' and user_choice == 'P':
        winner = 'user'
        
    if computer_choice == 'P' and user_choice == 'S':
        winner = 'user'
        
    if computer_choice == 'S' and user_choice == 'R':
        winner = 'user'
        
    if computer_choice == user_choice:
        winner = 'draw'
        
    if winner == 'user': score_user = score_user + 1
    if winner == 'computer': score_computer = score_computer + 1
        
    print(winner)