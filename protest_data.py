'''
This program makes a .csv file of city, state, latitude, and longitude
 of anti-racist protests in response to the murder of George Floyd
 by Minneapolis police officers that took place in the United States on the weekend of May 30th 2020.
'''

import pandas as pd
import numpy as np

protest_cities = pd.read_csv("data/protest_cities.csv")
all_cities = pd.read_csv("../shapefiles/uscities/uscities.csv")
mod_all_cities = all_cities[["city_ascii", "state_id", "lat", "lng"]]
#mod_all_cities.rename(columns={"city_ascii" : "city", "state_id" : "state"})
all_cities = mod_all_cities

protest_city_info = pd.DataFrame(columns=["city_ascii", "state_id", "lat", "lng"])

#clean data a little bit
cities = protest_cities["City"].str.replace(r'[^\w\s]+', '')
cities = cities.str.strip()

states = protest_cities["State"].str.replace(r'[^\w\s]+', '')
states = states.str.strip()

#find each city in all_cities, and make a new df containing only the cities in protest_cities
citystates = [cities, states]
i = 0
num_cities = len(cities)
for i in range(num_cities):
    city = citystates[0][i]
    state = citystates[1][i]
    df = all_cities[(all_cities["city_ascii"] == city) & (all_cities["state_id"] == state)]
    if df.empty:
        print(city, state)
    protest_city_info = protest_city_info.append(df,ignore_index = True)

protest_city_info.to_csv("/Users/Eliana/Documents/_csprojects/Protest_map/data/protest_city_info.csv", index=False, header=True)


