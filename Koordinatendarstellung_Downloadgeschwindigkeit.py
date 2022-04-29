import plotly.express as px
import pandas as pd

#data = pd.read_csv(r'c:\users\Ronja\Documents\20171212_wifionice\wifionice.csv', sep=';', low_memory=False) #Importiert die WifionIce.parquet-Datei
data_raw = pd.read_parquet(r'c:\Users\Ronja\Documents\GitHub\wifionice\wifionice.parquet') #Importiert die WifionIce.parquet-Datei

data = data_raw[data_raw["gps_v"] <= 95 ]#Filtert die Daten auf die gewünschte Downloadgeschwindigkeit
#data = data[data["created"] >= ]
data = data[data["gps_breite"] >= 48.97 ]
data = data[data["gps_breite"] <= 49.04 ]
data = data[data["gps_laenge"] >= 8.35]
data = data[data["gps_laenge"] <= 8.52]

print(data.describe())

a = 1 # Jeder wievielte Datenpunkt in der Darstellung genutzt werden soll

c = data["tprx"][::a]
s = data["gps_v"][::a]

fig = px.scatter_mapbox(data, lat=data["gps_breite"][::a], lon=data["gps_laenge"][::a], hover_name=data["created"][::a], color=c, size=s,
                        color_continuous_scale="Aggrnyl" , range_color=(0, 4000000), opacity=0.6, size_max=10, zoom=4, center={"lat":51.086161, "lon":10.386435},
                        mapbox_style="open-street-map", title="WifiOnIce - Farbskala ist die gemessene Downloadgeschwindigkeit in byte/s")

fig.update_layout(font_family="Comic Sans MS")
fig.update_layout(font_size=20)


fig.show()
