"""
・Get latitude and longitude(highest and lowest) of each prefecture
"""

import pandas as pd

data = pd.read_csv("../data/address/address-data.csv", index_col=0)
prefecture = [] # prefecture name
max_lat, min_lat = [], []  # latitude
max_lon, min_lon = [], []  # longitude

df = pd.DataFrame()
for i in range(1, 47+1):
    tmp = data[data["都道府県コード"]==i]
    prefecture.append(tmp.iloc[0, 1])
    lat = tmp['緯度'].to_list()
    lon = tmp['経度'].to_list()
    lat.sort()
    lon.sort()
    
    max_lat.append(max(lat))
    min_lat.append(min(lat))
    max_lon.append(max(lon))
    min_lon.append(min(lon))    
    
df['prefecture'] = prefecture
df['max_lat'] = max_lat
df['min_lat'] = min_lat
df['max_lon'] = max_lon
df['min_lon'] = min_lon

df.to_csv('../data/address/address-data2.csv')