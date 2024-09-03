# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

## Load the Data
from pandas import DataFrame
import pandas as pd
import json
import requests
# Load From a CSV
september_dataframe = pd.read_csv('./data/september_data.csv',
                                  names=['station_id','bikes',
                                         'spaces','total_docks',
                                         'timestamp']) ## read CSV assumes header

# <codecell>

# The Web/Location Data
url = 'http://divvybikes.com/stations/json'
resp = requests.get(url)

data = json.loads(resp.text)
ldata =  data['stationBeanList']


# <codecell>

mergeset = pd.merge(september_dataframe,DataFrame(ldata),
                    left_on='station_id',right_on='id')
mergeset.head

# <codecell>

mergeset.describe()

# <codecell>

# However this gives me a bunch of things I don't want, ie, the timestamp, avaliableBikes
# So let's just get what we want, location and id

limited_data = []
for station in ldata:
    val = {'id':int(station['id']),'latitude':station['latitude'],'longitude':station['longitude'],'location':station['location']}
    limited_data.append(val)

# and convert it to a DataFrame
limited_data = DataFrame(limited_data)

# <codecell>

#Merge Time
correct_mergeset = pd.merge(september_dataframe,limited_data,left_on='station_id',right_on='id')
correct_mergeset.keys()

# <codecell>

# Now Watch -
avg_lat = correct_mergeset['latitude'].mean()
avg_long = correct_mergeset['longtude'].mean()


