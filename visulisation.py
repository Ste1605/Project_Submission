import matplotlib.pyplot as plt
import pandas as pd
import matplotlib as mlp
import os

df = pd.read_csv('president_state.csv', index_col=0)
df1 = df.drop(['United States'])
plt.rcParams.update(plt.rcParamsDefault)
plt.style.use('grayscale')
fig, ax = plt.subplots()
df1 = df1.sort_values('total_votes', ascending=False)
ax.bar(df1.index, df1['total_votes'])
ax.set_xticklabels(df1.index, rotation=90, horizontalalignment = 'right', fontsize = '12')
ax.set_title('State Votes for 2020 US Election', fontsize=12)
ax.set_ylabel("#Votes")
ax.set_xlabel('States')

plt.show()



