import folium

map=folium.Map(location=[13.015778943432096, 77.60272672869591],zoom_start=10,tiles="Stamen Terrain")

fg=folium.FeatureGroup(name="My Map")
fg.add_child(folium.Marker(location=[13.015778943432096, 77.60272672869591],popup="hi i am marker!",icon=folium.Icon(color="lightblue")))

map.add_child(fg)

map.save("map5.html")