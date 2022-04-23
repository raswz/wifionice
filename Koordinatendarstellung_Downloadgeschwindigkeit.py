import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_parquet('wifionice.parquet') #Importiert die WifionIce.parquet-Datei

y = data['gps_breite'] # Setzt die Breitenkoordinaten aus der Datei als x-Variable
x = data['gps_laenge'] # Setzt die Breitenkoordinaten aus der Datei als y-Variable
s = data[''] # Bestimmte die Größe der Punkte anhand der ""-Werte

plt.axis('equal') # Setzt für beide Achsen die gleichen Abstände, um ein kaum verzerrtes Abbild der Koordinaten zu bekommen

plt.scatter(x, y) # Erstellt einen Scatterplot mit der x- und y-Variable
plt.show() # Zeigt den erstellten Scatterplot