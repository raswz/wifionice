import matplotlib as mpl
import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_parquet('wifioniceping.parquet') #Importiert die WifionIce.parquet-Datei

y = data['gps_breite'][::1] # Setzt die Breitenkoordinaten aus der Datei als x-Variable
x = data['gps_laenge'][::1] # Setzt die Breitenkoordinaten aus der Datei als y-Variable
c = data['link_ping'][::1] # Bestimmte die Größe der Punkte anhand der "gps_v"-Werte
s = 40

mpl.colors.Normalize(vmin=0, vmax=5000)
#mpl.colors.Colormap('Dark2', N=5)
plt.axis('equal') # Setzt für beide Achsen die gleichen Abstände, um ein kaum verzerrtes Abbild der Koordinaten zu bekommen

plt.scatter(x, y, s, c, cmap='Dark2_r', alpha=0.1, linewidths=0) # Erstellt einen Scatterplot mit der x- und y-Variable
plt.show() # Zeigt den erstellten Scatterplot