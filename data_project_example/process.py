
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 28 13:09:54 2021

@author: dieter
"""

import numpy
from matplotlib import pyplot
from mpl_toolkits.basemap import Basemap
import pandas

whales_to_plot = 100

data = pandas.read_csv('data.csv', na_values='NaN')

# make working with the data easier
data['id'] = data['individual-local-identifier']
data['long']=data['location-long']
data['lat']=data['location-lat']
data['error'] = data['argos:error-radius'] / 1000
data['outlier'] = -data['manually-marked-outlier'].isnull()

# remove data with errors > 25 km, and outliers 
data = data.query('error < 25 and not outlier')


##
# Here I create a map showing the whale trajectories.
# This kind of 'advanced' plotting is not exspected. But would be appreciated :)
##

# Get the range of the lat/long, and the range of the map we want to plot
min_lon = data.long.min() - 0
max_lon = data.long.max() + 3
min_lat = data.lat.min() - 3
max_lat = data.lat.max() + 3

mn_lon = data.long.mean()
mn_lat = data.lat.mean()


# Get the id labels of the whales
ids = data['id'].unique()
print(ids)


# Plot a map of the West coast
pyplot.figure(figsize=(10,10))
m = Basemap(llcrnrlon=min_lon,llcrnrlat=min_lat,urcrnrlon=max_lon,urcrnrlat=max_lat,lat_0=mn_lat,lon_0=mn_lon, projection='lcc', resolution='l')
m.fillcontinents(color='#ECE2C7')
m.drawmapboundary(fill_color='#D8EFF5')
m.drawcoastlines()
m.drawparallels(numpy.arange(20,45,5),labels=[1,1,1,1,1])
m.drawmeridians(numpy.arange(-120,-110,5),labels=[1,1])

# Add a nice scale bar
m.drawmapscale(mn_lon+1,mn_lat+5, mn_lon, min_lat,500, barstyle='fancy')

# Plot the trajectory of every whale on the map (transformed from coorindates to x,y's)
counter = 1
labels = []
for x in ids:
    print(x)
    individual_data = data.query('id == @x')
    x, y = m(individual_data.long.values, individual_data.lat.values)
    m.plot(x, y)
    labels.append('whale ' + str(counter))
    counter = counter + 1
    if counter > whales_to_plot: break

# Add some labels and show our piece of art
pyplot.legend(labels)
pyplot.title('Blue and fin whales trajectories')
#pyplot.tight_layout()
pyplot.savefig('map.png',dpi=150)
pyplot.show()

#%%
#
# End of creation of map
#

## Where along the West coast are you most likely to spot a whale?
## Lets look at the raw distribution of the whale location
## This will show us where along the coast I should go to see whales
pyplot.subplot(1,2,1)
pyplot.hist(data['long'], bins=100)
pyplot.title('Longitude')
pyplot.xlabel('Longitude (deg.)')
pyplot.ylabel('Counts')
pyplot.subplot(1,2,2)
pyplot.hist(data['lat'], bins=100)
pyplot.title('Latitude')
pyplot.xlabel('Latitude (deg.)')
pyplot.ylabel('Counts')
pyplot.tight_layout()
pyplot.savefig('histograms.png',dpi=150)

## The distributions above are biased as whale with more data points influence the distribution more
# Here we look at where every whale hangs out, on average.
## Get mean lat/long per whale
grp = data.groupby('id')
mns = grp.mean()
mns = mns.reset_index()
mns.loc[:,('long','lat')]

pyplot.figure()
pyplot.scatter(mns.long, mns.lat)
pyplot.xlim(min_lon,max_lon)
pyplot.ylim(min_lat,max_lat)
pyplot.grid()

pyplot.title('Mean Longitude and Latitude, per whale')
pyplot.xlabel('Longitude (deg.)')
pyplot.ylabel('Latitude (deg.)')

ax = pyplot.gca()
ax.set_aspect('equal')
pyplot.savefig('means.png',dpi=150)





