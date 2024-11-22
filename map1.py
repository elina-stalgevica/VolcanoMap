import folium
import pandas

data = pandas.read_csv("Volcanoes.txt")
lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])
name = list(data["NAME"])

html = """<h4>Volcano information:</h4>
<b>Height:</b> %s m<br>
<b>Name:</b> %s<br>
<b>Link:</b> <a href="https://www.google.com/search?q=%%22%s%%22" target="_blank">%s</a><br>
"""

map = folium.Map(location=[38.58, -99.09], zoom_start=6, tiles="OpenStreetMap")

fg = folium.FeatureGroup(name="My Map")

for lt, ln, el, nm in zip(lat, lon, elev, name):
    iframe = folium.IFrame(html=html % (el, nm, nm, nm), width=250, height=100)
    fg.add_child(folium.Marker(location=[lt, ln], popup=folium.Popup(iframe), icon=folium.Icon(color='green')))

map.add_child(fg)

map.save("Map1.html")
