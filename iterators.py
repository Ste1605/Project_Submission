import pandas as pd
df = pd.read_csv('president_county_candidate.csv')

#state_county =['Kent County','New Castle County','Sussex County','District of Columbia','Ward 2','Ward 3','Ward 4','Ward 5','Ward 6','Ward 7','Ward 8']
electees =df['candidate']
party =df['party']

#count = 1
#for name in party:
    #print(count, name)

counter_list = list(enumerate(party, 1))
print(counter_list)

