# Import folium library to create interactive web map
import folium
import pandas as pd


html = """
Volcano name:<br>
<a href="https://www.google.com/search?q=%%22%s%%22" target="_blank">%s</a><br>
Height: %s m
"""

# Read the volcanoes txt file
df = pd.read_csv(f".//sources//Volcanoes.txt")
# Convert Latitudes and Longitudes list
latitudes = list(df["LAT"])
longitudes = list(df["LON"])
elevation = list(df['ELEV'])
names = list(df['NAME'])


def color_producer(elevation):
    """
    Function to decide the icon color
    """
    if elevation <= 1000:
        return 'green'
    elif elevation <= 3000:
        return 'orange'
        pass
    else:
        return 'red'


# Create a map method
map = folium.Map(location=[38.58, -99.09], zoom_start=6)
fg = folium.FeatureGroup(name="Volcanoes")

for lat, lon, elev, name in zip(latitudes, longitudes, elevation, names):
    iframe = folium.IFrame(html=html % (
        name, name, elev), width=200, height=100)

    fg.add_child(folium.CircleMarker(location=[lat, lon], radius=6,
                 popup=folium.Popup(iframe), fill_color=color_producer(elev), color='grey', fill_opacity=0.7))

fgp = folium.FeatureGroup(name="Population")
# Color countries by the population as of 2025
fgp.add_child(folium.GeoJson(
    data=open('.//sources//world.json', 'r', encoding='utf-8-sig').read(),
    style_function=lambda x: {'fillColor': 'green' if x['properties']['POP2005'] < 10000000
                              else 'orange' if 10000000 <= x['properties']['POP2005'] < 50000000 else 'red'}))

map.add_child(fg)
map.add_child(fgp)
# Layer control allows to show one child at a time
map.add_child(folium.LayerControl())
map.save("Volcanoes and Population with Folium.html")
