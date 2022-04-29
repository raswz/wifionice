import matplotlib as mpl
import matplotlib.pyplot as plt
import pandas as pd
ax = plt.axes()

data = pd.read_parquet(r'c:\users\Ronja\Documents\GitHub\wifionice\wifionice.parquet') #Importiert die WifionIce.parquet-Datei

y = data['gps_breite'][::100] # Setzt die Breitenkoordinaten aus der Datei als x-Variable
x = data['gps_laenge'][::100] # Setzt die Breitenkoordinaten aus der Datei als y-Variable
s = data['sid'][::100] # Bestimmte die Größe der Punkte anhand der "gps_v"-Werte

plt.title("WifiOnIce")

#ax.set_facecolor(transparent=True)

#mpl.colors.Normalize(vmin=0, vmax=5000)
#mpl.colors.Colormap('Dark2', N=5)
#ax.set_aspect('equal', adjustable='box', anchor='C') # Setzt für beide Achsen die gleichen Abstände, um ein kaum verzerrtes Abbild der Koordinaten zu bekommen

plt.scatter(x, y, s, linewidths=0) # Erstellt einen Scatterplot mit der x- und y-Variable
plt.show() # Zeigt den erstellten Scatterplot
#plt.savefig('wifionice.png', dpi=600, facecolor=None) # Speichert den Scatterplot als .png-Datei