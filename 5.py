import folium

map=folium.Map(location=[13.015778943432096, 77.60272672869591],tiles="Stamen Terrain")

for coordinates in [[13.015778943432096, 77.60272672869591],[13.020327000000004, 77.69636549999998]]:
    fg=folium.FeatureGroup(name="My Map")
    fg.add_child(folium.Marker(location=(coordinates),popup="hi i am marker!",icon=folium.Icon(color="orange")))
    map.add_child(fg)

map.save("map6.html")