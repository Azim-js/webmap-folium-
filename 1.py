import folium

# folium creats leaflet aotumatcalliy in the html 
# now using the folium object called .Map()

x=folium.Map(location=[13.015778943432096, 77.60272672869591],zoom_start=50)

#and outputing the map in map2.html 

x.save("map2.html")
