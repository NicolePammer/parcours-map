from collections import namedtuple
import pandas as pd
import folium


map = folium.Map(location=[47.5, 13.11], zoom_start = 8, tiles = "Stamen Terrain")
fg = folium.FeatureGroup(name="My Archery Map")

data = pd.read_csv("15_web-map/archery_parcours.txt", sep=",")

parcour_name = list(data['parcour_name'])
parcour_location = list(data['parcour_location'])
website = list(data['website'])
parcour_level = list(data['parcour_level'])
lat = list(data['lat'])
lon = list(data['lon'])

html = """
%s (%s)<br>
<a href="%s" target="external">Visit website</a><br>
"""

for name, location, web, lvl, lt, ln in zip(parcour_name, parcour_location, website, parcour_level, lat, lon):
    if lvl==3:
        color_lvl = 'blue'
    elif lvl==2:
        color_lvl = 'green'
    elif lvl==1:
        color_lvl = 'lightgreen'
    else:
        color_lvl = 'gray'

    iframe = folium.IFrame(html = html % (name,location, web), width=300, height=100)

    fg.add_child(folium.Marker(location=[lt, ln], popup=folium.Popup(iframe), icon=folium.Icon(color=color_lvl)))

map.add_child(fg)

map.save("15_web-map/my-archery-map.html")