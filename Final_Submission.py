#####libaries needed for project
import pandas as pd
import re
import matplotlib.pyplot as plt
import matplotlib as mlp
import os
import numpy as np
###############################

#pres_county_cand= pd.read_csv("C:\Users\Ste Mc - Laptop\PycharmProjects\Project_Submission\president_county_candidate.csv")
#print(pres_county_cand.head())
#print(pres_county_cand.shape)

#missing_values_count = pres_county_cand.isnull().sum()
#print(missing_values_count[0:6])

#drop_duplicates= pres_county_cand.drop_duplicates(subset=["state"])
#print(pres_county_cand.shape,drop_duplicates.shape)

#removing unnecessary characters from the candidate column
#df= pd.read_csv("president_county_candidate.csv")
#df['candidate']=df['candidate'].str.replace(r"Joe Biden","Sleepy Joe")
#print(df.head())

df= pd.read_csv("president_county_candidate.csv")
#df['party']=df['party'].str.replace(r"DEM","Democrats").str.replace(r"REP","Republicans")
#print(df.head())


#mapper = {"REP": "Republican", "DEM": "Democrat"}
#df['full party name'] = df['party'].replace(mapper)

#for col in df.columns:
#    print(col)
#print(df.head())
#print(df.shape)

#Code to add to remove party examples that are not DEM or REP
uniqueParty = df['party'].unique()
#print(uniqueParty)

uniqueParty2 =['LIB', 'GRN', 'WRI', 'PSL', 'IND', 'ALI', 'CST', 'ASP', 'OTH', 'UTY',
 'LLC', 'SWP', 'BAR', 'PRO', 'NON', 'PRG', 'UNA', 'BMP', 'GOP', 'BFP', 'APV', 'IAP',
 'LLP', 'SEP']


#print(type(uniqueParty2))
#print(uniqueParty2)

#df = pd.DataFrame(list(uniqueParty2))
#df = df[df.column_name.isin(uniqueParty2) == False]
#print(df.head())
df_2020 = df.drop(df[(df.party != 'REP') & (df.party != 'DEM')].index)

#df.drop(df.index[df['party'] == 'LIB|GRN'], inplace = True)
#print(df.head())
#print(df_2020.shape)


df1 = pd.read_csv('president_county_candidate.csv').set_index("county")
df2 = pd.read_csv('primary_results_2016.csv').set_index("county")

print(df1.shape,df2.shape)

left = pd.read_csv('president_county_candidate.csv')
right = pd.read_csv('primary_results_2016.csv')
merged_data= pd.merge(left,right,on='county')


df3 = merged_data
pd.set_option('max_columns', None)
print(df3.shape)
#print(df3.columns.tolist())
#df3.to_csv('Output.csv')
df3.drop(['state_abbreviation', 'fips', 'won', 'fraction_votes'], axis=1, inplace=True)

print(df3.head())
#print(df3.columns.tolist())
