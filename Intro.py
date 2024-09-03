# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

from pandas import Series, DataFrame
import pandas as pd

## There are two fundamental Data Structures in Pandas, the series and the dataframe

## The Series
s = Series([4, 5, 'a', "some thing"]) #without labeled index
s2 = Series([4,5,6,'a string'],index=['a','b','c','d']) #with labeled index

## And the Dataframe
data = {'building':['Ryerson','Ryerson','Pick', 'Harper'],
              'room':[251,276,532,140],
              'capacity':[153,54,15,96]}
df = DataFrame(data)

# <codecell>

df

# <codecell>

## You can access the data contained in both

print s.index
print s2.index ##what should this print?

# <codecell>


print df
print '\n'
print df['capacity']


