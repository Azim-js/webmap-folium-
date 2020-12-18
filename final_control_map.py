import folium
import pandas
import json

data=pandas.read_csv("volcanoes.txt")
lt=list(data["LAT"])
ln=list(data["LON"])
el=list(data["ELEV"])
name=list(data["NAME"])

html=""" <h4> volocanoes : <a href="https://www.google.com/search?=%s">%s</a> height %s m"""

mapp=folium.Map(location=[38.58,-99.99],zoom_start=6,tiles="Stamen Terrain")

def color_prod(x):
    if x<2000:
        return "green"
    elif x>=2000 and x<=3000:
        return "black"
    else:
        return "red"
fgv=folium.FeatureGroup(name="Volcanoes")
for lt,ln,el,name in zip(lt,ln,el,name):
    iframe=folium.IFrame(html=html %(name,name,str(el)),width=200,height=100) 
    fgv.add_child(folium.CircleMarker(location=[lt,ln],radius=10,popup=folium.Popup(iframe),color="grey",fill_color=color_prod(el),fill_opacity=0.8))
    mapp.add_child(fgv)
fgp=folium.FeatureGroup(name="population")
fgp.add_child(folium.GeoJson(data=open("world.json","r",encoding="utf-8-sig").read(),
style_function=lambda x: {'fillColor':'green' if x['properties']['POP2005']<10000000 else 'orange' if 1000000<= x['properties']['POP2005']<20000000 else 'red'}))

mapp.add_child(fgv)
mapp.add_child(fgp)
mapp.add_child(folium.LayerControl())
mapp.save("final_control_map.html")