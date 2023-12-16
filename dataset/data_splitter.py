# Splits the `traffic.csv` files by city

import pandas as pd
import os

# Read the data
traffic = pd.read_csv('dataset/traffic.csv', low_memory=False)

# Split the data by city
cities = traffic['city'].unique()

for city in cities:
    print(f'Creating {city}.csv')
    city_data = traffic[traffic['city'] == city]
    city_data.to_csv(f'dataset/{city}.csv', index=False)
    print(f'{city}.csv created successfully')

print('All files created successfully')