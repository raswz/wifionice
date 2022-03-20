import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.axes as ax
import numpy as np
import pandas as pd

data = pd.read_parquet('wifionice.parquet')

y = data['gps_breite'].iloc[::1000]
x = data['gps_laenge'].iloc[::1000]
z = data['link_ping'].iloc[::1000]

plt.axis('equal')

plt.scatter(x, y, c = z, marker = '.')
plt.show()