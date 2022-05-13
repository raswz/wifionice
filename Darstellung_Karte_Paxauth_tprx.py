import numpy as np
import plotly.express as px
import pandas as pd

#data = pd.read_csv(r'c:\users\Ronja\Documents\20171212_wifionice\wifionice.csv', sep=';', low_memory=False) #Importiert die WifionIce.parquet-Datei
data_raw = pd.read_feather(r'c:\Users\Ronja\Documents\GitHub\wifionice\wifionice.feather') #Importiert die WifionIce.parquet-Datei

data_raw['pax_auth'] = data_raw['pax_auth'].replace(np.nan, 0)

data = data_raw[data_raw["gps_v"] <= 95] #Filtert die Daten auf die gewünschte Downloadgeschwindigkeit
#data = data[data['link_id'] == 101] #Filtert die Daten auf die gewünschte Link-ID
data = data[data['pax_auth'] > 0] #Filtert Datenpunkte ohne registriertes Gerät

#data = data[data['sid'] >= 245000000]
#data = data[data['sid'] <= 260000000]
#data = data[data["created"] >= ]
#data = data[data["gps_breite"] >= 48.97]
#data = data[data["gps_breite"] <= 49.04]
#data = data[data["gps_laenge"] >= 8.35]
#data = data[data["gps_laenge"] <= 8.52]

#print(data.describe())



a = 30 # Jeder wievielte Datenpunkt in der Darstellung genutzt werden soll

c = data["tprx"][::a]
s = data["pax_auth"][::a]

fig = px.scatter_mapbox(data, lat=data["gps_breite"][::a], lon=data["gps_laenge"][::a], hover_name=data["created"][::a], color=c, size=s,
                        color_continuous_scale="Aggrnyl" , range_color=(0, 4000000), opacity=0.35, size_max=12, zoom=5.3, center={"lat":51.086161, "lon":10.386435},
                        mapbox_style="open-street-map", title="WifiOnIce 2017 - Farbskala zeigt die gemessene Downloadgeschwindigkeit in byte/s, Größe der Punkte die Anzahl der mit dem Internet verbunden Geräte")

fig.update_layout(font_family="Comic Sans MS")
fig.update_layout(font_size=15)


#fig.show()
fig.write_html(r'c:\Users\Ronja\Documents\GitHub\wifionice\wifionice_tprx_pathaux.html')