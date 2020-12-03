import folium
import pandas as pd

V = pd.read_csv("Volcanoes.csv")









map_item = folium.Map()

fg = folium.FeatureGroup(name="My Map")

for i in range(len(V)):
    if V["ELEV"][i] > 3000:
        fg.add_child(folium.Marker(location=[V['LAT'][i], V['LON'][i]], popup=V['NAME'][i], icon=folium.Icon(color='red')))
        continue

    if V["ELEV"][i]> 2000:
        fg.add_child(folium.Marker(location=[V['LAT'][i], V['LON'][i]], popup=V['NAME'][i], icon=folium.Icon(color='orange')))
        continue

    if V["ELEV"][i] >1000: 
        fg.add_child(folium.Marker(location=[V['LAT'][i], V['LON'][i]], popup=V['NAME'][i], icon=folium.Icon(color='darkblue')))
        continue
    
    fg.add_child(folium.Marker(location=[V['LAT'][i], V['LON'][i]], popup=V['NAME'][i], icon=folium.Icon(color='lightblue')))

    


map_item.add_child(fg)

map_item.save("map1.html")