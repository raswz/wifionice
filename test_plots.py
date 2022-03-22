import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.axes as ax
import numpy as np
import pandas as pd

data = pd.read_parquet('wifionice.parquet')

x = data[data['link_ping'] > 5000]

plt.hist(x)
plt.show()