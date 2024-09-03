# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

from pandas import DataFrame
import pandas as pd

# Load From a CSV
september_dataframe = pd.read_csv('./data/september_data.csv',names=['station_id','bikes','spaces','total_docks','timestamp']) ## read CSV assumes header

# <codecell>

import json
import requests

# Load from the Web (and Json

url = 'http://divvybikes.com/stations/json'
resp = requests.get(url)

data = json.loads(resp.text)
stations_metadata = data['stationBeanList']
stations_dataFrame = DataFrame(stations_metadata)

# <codecell>

# A quick cleaning example - Sorting

september_dataframe.sort_index(by='timestamp')



# <codecell>

# Quick Calculation Example - Mean
avg_bikes = september_dataframe['bikes'].mean()
avg_docks = september_dataframe['spaces'].mean()
avg_combo = september_dataframe['total_docks'].mean()

print "The Average Number of Bikes were %s" % (avg_bikes)
print "The Average Number of Docks were %s" % (avg_docks)
print "The Average Number of Combination was %s" % (avg_combo)

# <codecell>


