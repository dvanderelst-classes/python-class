# -*- coding: utf-8 -*-
"""
Created on Sat Jul  9 09:01:03 2016
 
@author: dieter
"""
import urllib.request
import json
import os.path
from matplotlib import pyplot
from matplotlib import dates
import matplotlib.dates as mdates
from datetime import datetime
from dateutil import tz


def utc2local(utc, tpe='s'):
    # METHOD 2: Auto-detect zones:
    utc = datetime.utcfromtimestamp(utc)
    from_zone = tz.tzutc()
    to_zone = tz.tzlocal()
    utc = utc.replace(tzinfo=from_zone)
    local = utc.astimezone(to_zone)
    if tpe == 's': local = local.strftime("%c")
    return local


def get_icon(icon):
    file_name = icon + '.png'
    file_on_disk = 'icons/' + file_name
    if not os.path.isfile(file_on_disk):
        url = 'http://openweathermap.org/img/w/' + file_name
        print(url)
        conn = urllib.request.urlopen(url)
        data = conn.read()
        f = open(file_on_disk, 'wb')
        f.write(data)
        f.close
    return file_on_disk


def get_data(query, call='c'):
    key = '&appid=eb85b0a4df49360254aad7a547a0de9b'
    metric = '&units=metric'
    http = 'http://'
    weather = 'api.openweathermap.org/data/2.5/weather?q='
    forecast = 'api.openweathermap.org/data/2.5/forecast?q='

    if call == 'c': url = http + weather + query + metric + key
    if call == 'f': url = http + forecast + query + metric + key
    print(url)

    conn = urllib.request.urlopen(url)
    data = conn.read()
    data = json.loads(data)
    data['url'] = url
    return data


# The rain field is a bit special...
def get_rain_field(data):
    keys = data.keys()
    if 'rain' not in keys:
        return 0
    if 'rain' in keys:
        rain = data['rain']
        rain_keys = rain.keys()
        if len(rain_keys) == 0: return 0
        if len(rain_keys) > 0: return rain[list(rain_keys)[0]]


def process_data(data):
    new = {}
    new['dte'] = utc2local(data['dt'], 's')
    new['dtn'] = utc2local(data['dt'], 'n')
    new['tmp'] = data['main']['temp']
    new['tmn'] = data['main']['temp_min']
    new['tmx'] = data['main']['temp_max']
    new['hum'] = data['main']['humidity']
    new['des'] = str(data['weather'][0]['description'])
    new['ico'] = data['weather'][0]['icon']
    new['deg'] = data['wind']['deg']
    new['spd'] = data['wind']['speed']
    new['rain'] = get_rain_field(data)
    new['org'] = data
    return new


def current(query):
    data = get_data(query, 'c')
    return process_data(data)


def get_prediction(query):
    data = get_data(query, 'f')
    prediction = data['list']
    new = process_data(prediction[0])
    fields = new.keys()
    new = {}
    new['org'] = data
    for field in fields:
        lst = []
        for data in prediction:
            point = process_data(data)
            lst.append(point[field])
        new[field] = lst
    new['seq'] = dates.date2num(new['dtn'])
    return new


def capitalize_list(lst):
    new = []
    for x in lst: new.append(x.capitalize())
    return new


def plot_graph(cities, field):
    pyplot.style.use('ggplot')
    formatter = mdates.DateFormatter('%Hh %d-%m')
    hours = mdates.HourLocator(interval=6)

    fig = pyplot.figure(figsize=(10, 5))

    for city in cities:
        result = get_prediction(city)
        print(result)
        print(result.keys())
        pyplot.plot_date(result['dtn'], result[field], '-')

    ax = pyplot.gca()
    ax.xaxis_date()
    ax.xaxis.set_major_locator(hours)
    ax.xaxis.set_major_formatter(formatter)
    ax.grid()

    pyplot.xlabel('Time')
    pyplot.ylabel(field)
    pyplot.legend(capitalize_list(cities))

    fig.autofmt_xdate()
    pyplot.show()


if __name__ == "__main__":
    plot_graph(['cincinnati, US', 'san francisco, US', 'new york, US'], 'tmp')
