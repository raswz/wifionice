import pandas as pd
import numpy as np
import datetime

data = pd.read_csv(r'c:\Users\Ronja\Documents\GitHub\wifionice\wifionice.csv', sep=';', low_memory=False) #Importiert die wifionice.csv-Datei

data['created'] = pd.to_datetime(data['created'].str.strip(), format='%Y-%m-%d %H:%M:%S')
#data['link_gw_conn'] = data.replace({True: "t", False: "f"})

#data = pd.to_datetime(data['created'], format='%Y-%m-%d %H:%M:%S') #Erstellt ein neues Datum-Feld aus dem Datum-Feld der wifionice.csv-Datei

#print(data.dtypes) #Gibt die Datentypen der Spalten aus
#print(data.head)
#print("1")
data.to_parquet(r'c:\Users\Ronja\Documents\GitHub\wifionice\wifionice1.parquet') #Speichert die wifionice.csv-Datei als parquet-Datei
data.to_feather(r'c:\Users\Ronja\Documents\GitHub\wifionice\wifionice1.feather') #Speichert die wifionice.csv-Datei als feather-Datei