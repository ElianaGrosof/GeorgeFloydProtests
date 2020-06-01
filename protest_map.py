'''
This program makes a map of anti-racist protests in response
 to the murder of George Floyd by Minneapolis police officers that
 took place in the United States on the weekend of May 30th 2020.

 It depends on protest_data.py to create the .csv file with the correct data
 and uses plot.ly to make the graph.

from https://plotly.com/python/scatter-plots-on-maps/
'''
import pandas as pd

import plotly.graph_objects as go
import plotly

df = pd.read_csv("data/protest_city_info.csv")

df['citystate'] = df['city_ascii'] + ', ' + df['state_id']

fig = go.Figure(data=go.Scattergeo(
        lon = df['lng'],
        lat = df['lat'],
        text = df['citystate'],
        hoverinfo='text',
        marker_color='coral'
        ))
fig.update_layout(
        #title = 'George Floyd Protests',
        title={
                'text': "George Floyd Protests",
                'y': 0.9,
                'x': 0.5,
                'xanchor': 'center',
                'yanchor': 'top'},
        geo_scope = 'usa',
    )

plotly.offline.plot(fig, filename="/Users/Eliana/Documents/_csprojects/Protest_map/protest_cities.html")
                    #include_plotlyjs=False, output_type='div')