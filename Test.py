import numpy as np
import pandas as pd
import re

df = pd.read_csv('president_county_candidate.csv')
y = np.array(df['total_votes'])
# Where y is greater than 5, returns index position
np.where(y>5)
array(df['total_votes'], dtype=int64),)
# First will replace the values that match the condition,
# second will replace the values that does not
np.where(y>5, "Hit", "Miss")
array(['Miss', 'Miss', 'Hit', 'Hit', 'Miss', 'Hit', 'Miss', 'Hit', 'Hit'],dtype='<U4')



