import matplotlib.pyplot as plt
import pandas as pd
import matplotlib as mlp
import os
import numpy as np

#df = pd.read_csv('president_county_candidate.csv', index_col=0)
#df1 = df.drop(['United States'])
#plt.rcParams.update(plt.rcParamsDefault)
#plt.style.use('grayscale')
#fig, ax = plt.subplots()
#df = df.sort_values('total_votes', ascending=False)
#ax.bar(df.index, df['total_votes'])
#ax.set_xticklabels(df.index, rotation=90, horizontalalignment = 'right', fontsize = '12')
#ax.set_title('State Votes for 2020 US Election', fontsize=12)
#ax.set_ylabel("#Votes")
#ax.set_xlabel('States')

#plt.show()

df1 = pd.read_csv('president_county_candidate.csv', index_col=0)
df2 = pd.read_csv('primary_results_2016.csv', index_col=0)
labels = ['2020', '2016']
EL1 = df1['total_votes']
EL2 = df2['votes']

x = np.arange(len(EL1))  # the label locations
width = 0.35  # the width of the bars

fig, ax = plt.subplots()
rects1 = ax.bar(x - width/2, EL1, width, label='Election_1')
rects2 = ax.bar(x + width/2, EL2, width, label='Election_2')

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('Total Votes')
ax.set_title('Election Year')
ax.set_xticks(x, labels)
ax.legend()

ax.bar_label(rects1, padding=3)
ax.bar_label(rects2, padding=3)

fig.tight_layout()

plt.show()
