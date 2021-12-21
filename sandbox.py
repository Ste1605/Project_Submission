import pandas as pd
from pandas import Series, DataFrame
import re
import matplotlib.pyplot as plt
import matplotlib as mlp
import os
import numpy as np

df1 = pd.read_csv('president_county_candidate.csv')
#print(df1.tail())

states = df1['state']
tv = df1['total_votes']
party = df1['party']

x = np.arange(len(states))  # the label locations
width = 0.35  # the width of the bars

fig, ax = plt.subplots()
rects1 = ax.bar(x - width/2, tv, width, label='Men')
rects2 = ax.bar(x + width/2, party, width, label='Women')

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('Scores')
ax.set_title('Scores by group and gender')
ax.set_xticks(x, states)
ax.legend()

ax.bar_label(rects1, padding=3)
ax.bar_label(rects2, padding=3)

fig.tight_layout()

plt.show()