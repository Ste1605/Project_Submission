import matplotlib.pyplot as plt
import pandas as pd
import matplotlib as mlp
import os
import numpy as np

df = pd.read_csv('president_state.csv', index_col=0)
df = df.drop(['United States'])
plt.rcParams.update(plt.rcParamsDefault)
plt.style.use('grayscale')
fig, ax = plt.subplots()
df = df.sort_values('total_votes', ascending=False)
ax.bar(df.index, df['total_votes'])
ax.set_xticklabels(df.index, rotation=60, horizontalalignment = 'right', fontsize = '12')
ax.set_title('State Votes for 2020 US Election', fontsize=12)
ax.set_ylabel("#Votes (mm)")
ax.set_xlabel('States')

plt.show()
