import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import folium

mpl.style.use('ggplot')

# df_san = pd.read_csv('https://cocl.us/sanfran_crime_dataset') # Full data
df_san = pd.read_csv('policecrime.csv') # Partial data

df_sum = df_san.groupby('PdDistrict')[['PdDistrict']].count()
df_sum.rename(columns={'PdDistrict' : 'Count'}, inplace=True)
df_sum.reset_index(inplace = True)
df_sum.rename(columns={'PdDistrict' : 'Neighborhood'}, inplace=True)

world_geo = r'san-francisco.geojson'

latitude = 37.77
longitude = -122.42

world_map = folium.Map(location=[latitude, longitude], zoom_start=12)

folium.Choropleth(
    geo_data=world_geo,
    data=df_sum,
    columns=['Neighborhood', 'Count'],
    key_on='feature.properties.DISTRICT',
    fill_color='YlOrRd',
    fill_opacity=0.7,
    line_opacity=0.2,
    legend_name='Crime Rate in San Francisco'
).add_to(world_map)

world_map.save('map.html')