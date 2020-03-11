from timeline_in_matplotlib import GenerateTimeLine
from matplotlib import pyplot as plt
import pandas as pd

data = pd.read_csv(r'events.txt', parse_dates=True, index_col=0)
ax = GenerateTimeLine(data)
plt.show()