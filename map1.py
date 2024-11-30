import folium
import pandas

data = pandas.read_csv("Volcanoes.txt")
lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])
name = list(data["NAME"])

#Function for icon colors
def color_producer(elevation):
    if elevation < 1000:
        return 'green'
    elif 1000 <= elevation < 3000:
        return 'orange'
    else: 
        return 'red'

html = """<h4>Volcano information:</h4>
<b>Height:</b> %s m<br>
<b>Name:</b> %s<br>
<b>Link:</b> <a href="https://www.google.com/search?q=%%22%s%%22" target="_blank">%s</a><br>
"""

map = folium.Map(location=[38.58, -99.09], zoom_start=6, tiles="OpenStreetMap")

fgv = folium.FeatureGroup(name="Volcanoes")

for lt, ln, el, nm in zip(lat, lon, elev, name):
    iframe = folium.IFrame(html=html % (el, nm, nm, nm), width=250, height=100)
    fgv.add_child(folium.Marker(location=[lt, ln], popup=folium.Popup(iframe), icon=folium.Icon(color=color_producer(el))))

fgp = folium.FeatureGroup(name="Population")
#Method that creates GeoJSON object
fgp.add_child(folium.GeoJson(data=open('world.json', 'r', encoding='utf-8-sig').read(), 
style_function=lambda x:{'fillColor': 'green' if x['properties']['POP2005'] < 10000000
else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000 else 'red'}))

#Adding groups to map
map.add_child(fgv)
map.add_child(fgp)

#Adding a Layer Control Panel
map.add_child(folium.LayerControl())

map.save("Map1.html")
