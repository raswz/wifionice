import numpy as np
import pandas as pd
import plotly.express as px

data_raw = pd.read_parquet(r'c:\Users\Ronja\Documents\GitHub\wifionice\wifionice.parquet') #Importiert die WifionIce.parquet-Datei

# data_raw = data_raw['sid'].astype(int) #Konvertiert die Spalte sid in einen Integer

# data_raw = data_raw[data_raw['sid'] <= 50000000] #Filtert die Daten nach der Spalte sid auf den Wert 1

# fig = px.histogram(data_raw, x='sid', nbins=1000)

# fig.show()

print(data_raw.dtypes)