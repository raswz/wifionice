import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.axes as ax
import numpy as np
import pandas as pd

data = pd.read_parquet('wifionice.parquet')

z = data['link_ping']



plt.hist(z, bins = 50)
plt.show()