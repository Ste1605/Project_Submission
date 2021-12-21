import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mlp

df2 = pd.read_csv('president_county_candidate.csv')
df2 = df2.drop(df2[(df2.party != 'REP') & (df2.party != 'DEM')].index)
output3 = df2
df_group3 = output3.groupby(['party'],as_index=False).sum().sort_values(by = 'total_votes', ascending= True).head(20)
plt.style.use("fivethirtyeight")
slices = df_group3['total_votes']
lables = df_group3['party']
plt.pie(slices, labels=lables)
plt.title('2020 US Election by Party')
plt.tight_layout()
plt.show()
