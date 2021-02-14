import folium

mapp=folium.Map(loaction=[38.58,-99.99],zoom_start=6,tiles="Stamen Terrain")

mapp.add_child(folium.Marker(location=[38.58,-99.99],popup="hi i am marker !",icon=folium.Icon(color="orange")))

mapp.save("map4.html")