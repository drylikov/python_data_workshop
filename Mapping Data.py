# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

# Let's place the Divvy Stations on a map
#Load the data
import requests
import json
from pandas import DataFrame
import pandas as pd

url = 'http://divvybikes.com/stations/json'
resp = requests.get(url)

data = json.loads(resp.text)
stations_metadata = data['stationBeanList']
stations_dataframe = DataFrame(stations_metadata)

# <codecell>

# now, importing the basemap
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt

# <codecell>

def basic_map(ax=None,lllat=41.75,urlat=42,
              lllon=-88,urlon=-87.5):
    ##create polor sterographic Basemap instance
    m = Basemap(ax=ax, projection='stere',
                lon_0=(urlon + lllon) / 2,
                lat_0=(urlat + lllat) / 2,
                llcrnrlat = lllat, urcrnrlat=urlat,
                llcrnrlon = lllon, urcrnrlon = urlon,
                resolution = 'f')
    m.drawcoastlines()
    m.drawstates()
    m.drawcountries()
    return m
m = basic_map()


# <codecell>

#stations_dataframe.describe
for index, row in stations_dataframe.iterrows():
    x,y = m(row['longitude'], row['latitude'])
    m.plot(x,y,'k.',alpha=1,color='blue')

# Thisis cool, but doesn't overlay anything interesting
shapefile = ('./data/illinois-latest/illinois-latest')
m.readshapefile(shapefile, 'roads')

# <codecell>

# Thisis cool, but doesn't overlay anything interesting
shapefile = ('./data/illinois-latest/illinois-latest')
m.readshapefile(shapefile, 'roads')

# <codecell>


