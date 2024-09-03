# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

## Remember, the September Dataframe is awesome. Let's make a plot, by time, over the average number of bikes
## First, we need to load the data
from pandas import DataFrame
import pandas as pd

# Load From a CSV
september_dataframe = pd.read_csv('./data/september_data.csv',names=['station_id','bikes','spaces','total_docks','timestamp'],
                                  parse_dates=[4]) ## read CSV assumes header

# <codecell>

import dateutil

## Wait, timestamp is a string, let's convert to a datetime with a map
print september_dataframe['timestamp']
september_dataframe['timestamp'] = september_dataframe['timestamp'].apply(lambda t: pd.to_datetime(t))
print september_dataframe.describe

# <codecell>

# Set the Time Zone to Central 
#timezone = 'US/Central'
#september_dataframe = september_dataframe['timestamp'].tz_localize('UTC').tz_convert(timezone)

# <codecell>

# Group by minute value (i.e. how many minutes have occured since midnight)
#september_dataframe.
station_monthly_groups = september_dataframe.groupby\
(september_dataframe['timestamp'].map(lambda t: 60*t.hour + t.minute))

# <codecell>

# Take the mean over each minute-since-midnight group
station_monthly_averages = station_monthly_groups.mean()
station_monthly_std = station_monthly_groups["bikes"].std()

# <codecell>

# Takes the converted minute value and displays it as a readable time
    def minute_into_hour(x):
        if x % 60 in range(0,10):
            return str(x // 60) + ":0" + str(x % 60)
        else:
            return str(x // 60) + ":" + str(x % 60)
    
    times = station_monthly_averages.index.map(minute_into_hour)
    times_std = station_monthly_std.index.map(minute_into_hour)

# <codecell>

# Add these new time values into our dataframe
station_monthly_averages["timestamp"] = times
station_monthly_averages["bikes_available_std"] = station_monthly_std

station_monthly_averages.describe()

# <codecell>

# Libaries
import matplotlib.pyplot as plt
import matplotlib.dates as dates

#print station_monthly_averages.describe

# <codecell>


grid_size = (1,1)
count = 1
nb_plots_per_page = 1
ax = plt.subplot2grid(grid_size, (count % nb_plots_per_page,0))
t = pd.to_datetime(station_monthly_averages['timestamp'])
mu1 = station_montly_averages['bikes']
#sigma1 = station_monthly_averages['bikes_available_std']
ax.plot(t, mu1)

# <codecell>


