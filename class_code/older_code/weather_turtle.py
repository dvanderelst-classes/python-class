# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import turtle			
import requests

api_key = 'eb85b0a4df49360254aad7a547a0de9b'

lat = '39'
lon = '-84'
url = "https://api.openweathermap.org/data/2.5/onecall?lat="+lat+"&lon="+lon+"&appid="+api_key

turtle.bye()			# close existing screens, if any

my_turtle = turtle.Turtle()	# make a variable called robot
my_turtle.shape('turtle')	# set the shape of the robot to ‘turtle’

response = requests.get(url) 
data = response.json()

hourly = data['hourly']
temperature = []
for data_point in hourly:
    temperature.append(data_point['temp'])

n = len(temperature)
x_values = range(-n*7,n*7,14)
min_t = min(temperature)
max_t = max(temperature)

counter = 0
for x,t in zip(x_values, temperature):
    t = t - min_t
    t = 5000*(t/max_t)
    if counter == 0: my_turtle.penup()
    my_turtle.setx(x)
    my_turtle.sety(t)
    my_turtle.pendown()
    counter = counter + 1