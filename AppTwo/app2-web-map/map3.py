import folium
import pandas

map = folium.Map(location=[38.58,-99.09], zoom_start=6, tiles="Mapbox Bright")


data = pandas.read_csv("Volcanoes.txt")
lat = list(data["LAT"])
lon = list(data["LON"])
name = list(data["NAME"])
elev = list(data["ELEV"])

html = """ <h5> Volcano name : </h5>
<br>
<a href="https://www.google.com/search?q=%%22%s%%22" target="_blank">%s</a><br>

Height : %s m

"""
def color_producer(elevation):
    if elevation < 1000:
        return 'green'
    elif 1000 <= elevation <= 3000:
        return 'orange'
    else:
        return 'red'

data_json = open("world.json", 'r', encoding='utf-8-sig').read()

# step1:  map.add_child(folium.Marker(location=[38.2,-99.1],popup="Hi I am a Marker",icon=folium.Icon(color='green')))
#step2 : fg.add_child(folium.Marker(location=[38.2,-99.1],popup="Hi I am a Marker",icon=folium.Icon(color='green')))
#step2 : fg.add_child(folium.Marker(location=[37.2,-97.1],popup="Hi I am a Marker",icon=folium.Icon(color='red')))
fgv = folium.FeatureGroup(name="Volcanoes")
for lt,ln,el,n in zip(lat,lon,elev,name):
#step3  : for coordinates in [[38.2,-99.1],[37.2,-97.1]]:
    #step 4 : fg.add_child(folium.Marker(location=[lt,ln],popup="Hi I am a Marker",icon=folium.Icon(color='green')))
    iframe = folium.IFrame(html=html % (n , n , str(el) ), width=200, height=100 )
    # fg.add_child(folium.Marker(location=[lt,ln],popup=n + " : " + str(el)+ " m",icon=folium.Icon(color='green')))
    #fg.add_child(folium.Marker(location=[lt,ln],popup=folium.Popup(iframe),icon=folium.Icon(color='green')))
    fgv.add_child(folium.CircleMarker(location=[lt,ln],radius= 6, popup=folium.Popup(iframe),fill_color=color_producer(el),color='grey',fill_opacity=0.7))
# fg.add_child(folium.GeoJson(data=(open('world.json','r',encoding='utf-8-sig').read())))
fgp = folium.FeatureGroup(name="Population")
fgp.add_child(folium.GeoJson(data=open('world.json', 'r', encoding='utf-8-sig').read(),style_function= lambda x : {'fillColor':'yellow' if x['properties']['POP2005']  < 10000000 else 'green' if 10000000 <= x['properties']['POP2005'] <= 20000000 else 'red' } ) )

map.add_child(fgv)
map.add_child(fgp)

map.add_child(folium.LayerControl())

#fg.add_child(folium.GeoJson(data=open('world.json', 'r', encoding='utf-8-sig').read(),style_function=lambda x: {'fillColor':'yellow'}))
#fg.add_child(folium.GeoJson(data=open('world.json', 'r', encoding='utf-8-sig').read(),style_function=lambda x: {'fillColor':'yellow'}))
# map.add_child(fg)

map.save("Map3.html")
map.save("Map3_html_popup_simple.html")
