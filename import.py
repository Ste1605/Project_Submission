import pandas as pd
#df = pd.read_csv('president_county_candidate.csv')
#df = df.drop(df[(df.party != 'REP') & (df.party != 'DEM')].index)
#df_group = df.groupby(['party', 'state'],as_index=False).sum().sort_values(by = 'total_votes', ascending= False).head(20)
#df_group['year'] = 2020
#print(df_group.shape)
#print(df_group.head())



#df['party']=df['party'].str.replace(r"DEM","Democrats").str.replace(r"REP","Republicans")

df1 = pd.read_csv('president_county_candidate.csv')
df1['year'] = 2020
df1= df1.drop(df1[(df1.party != 'REP') & (df1.party != 'DEM')].index)
#df1 = pd.read_csv('president_county_candidate.csv').set_index("state")

df2 = pd.read_csv('primary_results_2016.csv')
df2['year'] = 2016
#df2 = pd.read_csv('primary_results_2016.csv').set_index("state")



output2 = pd.concat(map(pd.read_csv, ['president_county_candidate.csv', 'primary_results_2016.csv']))
output3 = pd.concat([df1,df2])
output3.drop(['state_abbreviation', 'fips', 'won', 'fraction_votes'], axis=1, inplace=True)
output3["total_votes"].fillna(output3["votes"], inplace=True)
output3.drop(['votes'], axis=1, inplace=True)


print(df1.shape)
print(df1.info())
print(df2.shape)
print(df2.info())
print(output3.shape)
print(output3.info())







