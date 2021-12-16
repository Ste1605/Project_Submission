import pandas as pd
import re
#pres_county_cand= pd.read_csv("president_county_candidate.csv")
#print(pres_county_cand.head())
#print(pres_county_cand.shape)

#missing_values_count = pres_county_cand.isnull().sum()
#print(missing_values_count[0:6])

#drop_duplicates= pres_county_cand.drop_duplicates(subset=["county"])
#print(pres_county_cand.shape,drop_duplicates.shape)

#removing unnecessary characters from the candidate column
#df= pd.read_csv("president_county_candidate.csv")
#df['candidate']=df['candidate'].str.replace(r"Joe Biden","Sleepy Joe")
#print(df.head())

#df= pd.read_csv("president_county_candidate.csv")
#df['party']=df['party'].str.replace(r"DEM","Democrats").str.replace(r"REP","Republicans")
#print(df.head())

#df = pd.read_csv('president_county_candidate.csv')
#new_column = pd.DataFrame({'Full Party Name1': []})
#df = df.merge(new_column, left_index = True, right_index = True)

#mapper = {"REP": "Republican", "DEM": "Democrat"}
#df['Full Party Name'] = df['party'].replace(mapper)

#for col in df.columns:
#    print(col)
#print(df.head())
#print(df.shape)
#print(df)

#df1 = pd.read_csv('president_county_candidate.csv').set_index("state")
#df2 = pd.read_csv('president_state.csv').set_index("state")

#print(df1.shape,df2.shape)

#concat_data=pd.concat([df1,df2],axis=1)
#concat_data=df1.join(df2,lsuffix="_State",rsuffix="_County")
#print(concat_data.shape,concat_data.info())


left = pd.read_csv('president_county_candidate.csv')
right = pd.read_csv('president_state.csv')
merged_data= pd.merge(left,right,on='state')


df = merged_data
df.to_csv('Output.csv')


print(merged_data.shape)

