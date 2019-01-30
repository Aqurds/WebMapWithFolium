# Importing folium
import folium

#importing pandas & loading the volcanoes data
import pandas as pd
df = pd.read_csv('volcanoes.txt')
df.head(2)

lat_mean = df['LAT'].mean()
lon_mean = df['LON'].mean()


# creating a function to get all the column values in different list
def makeList(data):
    listName = list(data.columns)
    sdata = []
    for item in listName:
        item = list(data[item])
        sdata.append(item)
    return sdata
    print(list(data.columns))


sdata = makeList(df)


volcano = folium.Map([lat_mean, lon_mean], zoom_start=5)
"""volcano.add_child(folium.CircleMarker(location=[lat_mean, lon_mean],
                             popup='Center',
                             tooltip='This is the center area of total volcanic data',
                             color='brown',
                            fill_color='red',
                                     radius=5,
                                      fill_opacity=1
                                     ))"""
for lat, lon, name, location, typ, status, elev in zip(sdata[8], sdata[9], sdata[2], sdata[3], sdata[6], sdata[4], sdata[5]):
            def colorGenerator(ev):
                color = ''
                if ev <=1000:
                    color = 'green'
                elif ev <=2000:
                    color = 'orange'
                elif ev >= 3000:
                    color = 'black'
                else:
                    color = 'red'
                return color
            volcano.add_child(folium.CircleMarker(location=[lat, lon],
                                                    popup='Name:' + name +
                                                        '; Location:' + location +
                                                        '; type:' + typ +
                                                        '; Status:' + status,
                                                    tooltip='Status:' + status + '; Elev:' + str(elev) + 'm',
                                                    color=colorGenerator(elev),
                                                    fill_color=colorGenerator(elev),
                                                    radius=7,
                                                    fill_opacity=1
                                                    #icon = folium.Icon(color=colorGenerator(elev))
                                                 ))


volcano.add_child(folium.GeoJson(data=open('world.json', 'r', encoding='utf-8-sig').read()))
volcano.save('volcano.html')
