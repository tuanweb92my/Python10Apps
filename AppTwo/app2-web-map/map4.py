import folium
import pandas
from geopy.geocoders import Nominatim
nom = Nominatim()


map = folium.Map(location=[38.58,-99.09], zoom_start=1, tiles="Mapbox Bright")


#
# step1:  map.add_child(folium.Marker(location=[38.2,-99.1],popup="Hi I am a Marker",icon=folium.Icon(color='green')))
#step2 : fg.add_child(folium.Marker(location=[38.2,-99.1],popup="Hi I am a Marker",icon=folium.Icon(color='green')))
#step2 : fg.add_child(folium.Marker(location=[37.2,-97.1],popup="Hi I am a Marker",icon=folium.Icon(color='red')))
#fgv = folium.FeatureGroup(name="Volcanoes")
#for lt,ln,el,n in zip(lat,lon,elev,name):
#step3  : for coordinates in [[38.2,-99.1],[37.2,-97.1]]:
    #step 4 : fg.add_child(folium.Marker(location=[lt,ln],popup="Hi I am a Marker",icon=folium.Icon(color='green')))
    #iframe = folium.IFrame(html=html % (n , n , str(el) ), width=200, height=100 )
    # fg.add_child(folium.Marker(location=[lt,ln],popup=n + " : " + str(el)+ " m",icon=folium.Icon(color='green')))
    #fg.add_child(folium.Marker(location=[lt,ln],popup=folium.Popup(iframe),icon=folium.Icon(color='green')))
    #fgv.add_child(folium.CircleMarker(location=[lt,ln],radius= 6, popup=folium.Popup(iframe),fill_color=color_producer(el),color='grey',fill_opacity=0.7))
# fg.add_child(folium.GeoJson(data=(open('world.json','r',encoding='utf-8-sig').read())))
#fgp = folium.FeatureGroup(name="Population")
#fgp.add_child(folium.GeoJson(data=open('world.json', 'r', encoding='utf-8-sig').read(),style_function= lambda x : {'fillColor':'yellow' if x['properties']['POP2005']  < 10000000 else 'green' if 10000000 <= x['properties']['POP2005'] <= 20000000 else 'red' } ) )

#lctuan = nom.geocode("793 Tran Xuan Soan St,Ho Chi Minh,VN")
#lchuy = nom.geocode("San Francisco, USA")


fghuy = folium.FeatureGroup(name="Big bro Huy house")
fghuy.add_child(folium.CircleMarker(location=[37.7792808, -122.4192363],radius= 20, popup="Hi , Big bro Huy is here",fill_color='yellow',color='yellow',fill_opacity=0.7))
fgtuan = folium.FeatureGroup(name="Tuan house")
fgtuan.add_child(folium.CircleMarker(location=[10.7553865, 106.7210507],radius= 20, popup="Hi I am Tuan",fill_color='pink',color='pink',fill_opacity=0.7))

#map.add_child(fgv)
#map.add_child(fgp)

map.add_child(fghuy)
map.add_child(fgtuan)

map.add_child(folium.LayerControl())

#fg.add_child(folium.GeoJson(data=open('world.json', 'r', encoding='utf-8-sig').read(),style_function=lambda x: {'fillColor':'yellow'}))
#fg.add_child(folium.GeoJson(data=open('world.json', 'r', encoding='utf-8-sig').read(),style_function=lambda x: {'fillColor':'yellow'}))
# map.add_child(fg)

map.save("SanFrancisco_HCM.html")
