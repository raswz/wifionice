import plotly.express as px
import pandas as pd

#Done

#data = pd.read_csv(r'c:\users\Ronja\Documents\20171212_wifionice\wifionice.csv', sep=';', low_memory=False) #Importiert die WifionIce.parquet-Datei
data_raw = pd.read_parquet(r'c:\Users\Ronja\Documents\GitHub\wifionice\wifionice.parquet') #Importiert die WifionIce.parquet-Datei

data = data_raw[data_raw["link_ping"] <= 5000]
 #Filtert die Daten auf Höhenangaben zwischen 0 und 1000m

a = 100

fig = px.scatter_mapbox(data, lat=data["gps_breite"][::a], lon=data["gps_laenge"][::a], color=data["link_ping"][::a],
                        color_discrete_sequence=["fuchsia"], size_max=10, zoom=4, center={"lat":51.086161, "lon":10.386435}, mapbox_style="open-street-map", title="WifiOnIce - Größe der Punkte ist GPS Höhe und Farbskala der gemessene Ping")



fig.show()
