# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

		
import requests
from matplotlib import pyplot

api_key = 'eb85b0a4df49360254aad7a547a0de9b'

lat = '39'
lon = '-84'
url = "https://api.openweathermap.org/data/2.5/onecall?lat="+lat+"&lon="+lon+"&appid="+api_key

# Get the data from the web
response = requests.get(url) 
data = response.json()

# create list with selected data
hourly = data['hourly']
selected_data = []
for data_point in hourly:
    selected_data.append(data_point['temp'])

pyplot.plot(selected_data)