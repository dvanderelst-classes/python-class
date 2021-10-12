#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 23 14:04:46 2021

@author: dieter
"""

# some_variable = 1000000

import random
import turtle				# import the turtle module
turtle.bye()		
turtle.clearscreen()		# close existing screens, if any
turtle.bgcolor('green')

winner = 'computer'

score_user = 0
score_computer = 0

steps_per_point = 100
max_points = 3



computer_turtle =  turtle.Turtle()
computer_turtle.shape('circle')

user_turtle =  turtle.Turtle()
user_turtle.shape('turtle')

#
# Draw finishing line
#
computer_turtle.penup()
computer_turtle.pensize(10)
computer_turtle.pencolor('white')
computer_turtle.setposition(0,-100)
computer_turtle.setheading(90)
computer_turtle.pendown()
computer_turtle.forward(200)


computer_turtle.penup()
user_turtle.penup()


user_turtle.setposition(-steps_per_point * max_points,50)
computer_turtle.setposition(-steps_per_point * max_points,-50)

computer_turtle.setheading(0)
user_turtle.setheading(0)


while score_user < max_points and score_computer < max_points:
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
        
    if winner == 'user':
        score_user = score_user + 1
        user_turtle.forward(steps_per_point)
        
    if winner == 'computer':
        score_computer = score_computer + 1
        computer_turtle.forward(steps_per_point)
    
    
        
if score_user > score_computer:
    user_turtle.forward(50)
else:
    computer_turtle.forward(50)
    
