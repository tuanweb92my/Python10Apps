import folium

map = folium.Map(location=[38.58,-99.09], zoom_start=6, tiles="Mapbox Bright")

fg = folium.FeatureGroup(name="My Map")

# step1:  map.add_child(folium.Marker(location=[38.2,-99.1],popup="Hi I am a Marker",icon=folium.Icon(color='green')))

#step2 : fg.add_child(folium.Marker(location=[38.2,-99.1],popup="Hi I am a Marker",icon=folium.Icon(color='green')))
#step2 : fg.add_child(folium.Marker(location=[37.2,-97.1],popup="Hi I am a Marker",icon=folium.Icon(color='red')))

for coordinates in [[38.2,-99.1],[37.2,-97.1]]:
    fg.add_child(folium.Marker(location=coordinates,popup="Hi I am a Marker",icon=folium.Icon(color='green')))


map.add_child(fg)

map.save("Map1.html")
