#####libaries needed for project

import pandas as pd
from pandas import Series, DataFrame
import re
import matplotlib.pyplot as plt
import matplotlib as mlp
import os
import numpy as np

###############################

#Imported csv file -
    #dropped all values which party was not related to DEM/REP
    #updated party name to read full name rather than abbrivation
    #grouped the data party/state and sorted in ascedning order total votes
    #added a new column to indiacte the year - 2020
    #**Insight here that California has highest number of votes in US election

df = pd.read_csv('president_county_candidate.csv')
df = df.drop(df[(df.party != 'REP') & (df.party != 'DEM')].index)
df['party']=df['party'].str.replace(r"DEM","Democrats").str.replace(r"REP","Republicans")
df_group = df.groupby(['party', 'state'],as_index=False).sum().sort_values(by = 'total_votes', ascending= False).head(20)
df_group['year'] = 2020
#print(df_group.shape)
#print(df_group.head())


#Merged Data & Manuipulate the data set
    #for df1 - the year was added to the DF to indicate the year of election
    #dropped all values which party was not related to DEM/REP
    #for df2 - the year was added to the DF to indicate the year of election
    #as the eyar was added for each df I could then concatenate the two data sets
    #creating a new df allowed me to add the updated df1 & df2 dataframes for concatenation
    #once the data was concatenated I dropped the columns which were of no relevance
    #there was a difference in how votes were recorded in each df hence why I replaced total votes with votes thus completing my dataset and ensuring there was no NaNs
    #final step was to remove the vote column as the data was passed into the total votes column
        #votes and total votes are clearly still unique due to the corraltion to the year column which was added
    #**Insight - there was a much higher turnout overall in 2020

df1 = pd.read_csv('president_county_candidate.csv')
df1['year'] = 2020
df1= df1.drop(df1[(df1.party != 'REP') & (df1.party != 'DEM')].index)
df1['party']=df1['party'].str.replace(r"DEM","Democrat").str.replace(r"REP","Republican")

df2 = pd.read_csv('primary_results_2016.csv')
df2['year'] = 2016

output3 = pd.concat([df1,df2])
output3.drop(['state_abbreviation', 'fips', 'won', 'fraction_votes'], axis=1, inplace=True)
output3["total_votes"].fillna(output3["votes"], inplace=True)
output3.drop(['votes'], axis=1, inplace=True)

df_group3 = output3.groupby(['year', 'party'],as_index=False).sum().sort_values(by = 'total_votes', ascending= True).head(20)

#print(df1.shape)
#print(df1.info())
#print(df2.shape)
#print(df2.info())
#print(output3.shape)
#print(output3.info())
#print(df_group3.head())


#print(output3.shape)
#print(output3)

    #first chart showcasing the total votes per state for 2020 Election
df = pd.read_csv('president_state.csv', index_col=0)
df = df.drop(['United States'])
plt.rcParams.update(plt.rcParamsDefault)
plt.style.use('grayscale')
fig, ax = plt.subplots()
df = df.sort_values('total_votes', ascending=False)
ax.bar(df.index, df['total_votes'])
ax.set_xticklabels(df.index, rotation=60, horizontalalignment = 'right', fontsize = '12')
ax.set_title('State Votes for 2020 US Election Chart#1', fontsize=12)
ax.set_ylabel("#Votes (mm)")
ax.set_xlabel('States')


df = pd.read_csv('president_state.csv', index_col=0)
df = df.drop(['United States'])
plt.rcParams.update(plt.rcParamsDefault)
plt.style.use('grayscale')
fig, ax = plt.subplots()
df = df.sort_values('total_votes', ascending=False)
ax.plot(df.index, df['total_votes'])
ax.set_xticklabels(df.index, rotation=60, horizontalalignment = 'right', fontsize = '12')
ax.set_title('State Votes for 2020 US Election Chart#2', fontsize=12)
ax.set_ylabel("#Votes (mm)")
ax.set_xlabel('States')

#plt.show()

df = pd.read_csv('president_state.csv', index_col=0)
df = df.drop(['United States'])
plt.rcParams.update(plt.rcParamsDefault)
plt.style.use('grayscale')
fig, ax = plt.subplots()
df = df.sort_values('total_votes', ascending=False)
ax.scatter(df.index, df['total_votes'])
ax.set_xticklabels(df.index, rotation=60, horizontalalignment = 'right', fontsize = '12')
ax.set_title('State Votes for 2020 US Election Chart#3', fontsize=12)
ax.set_ylabel("#Votes (mm)")
ax.set_xlabel('States')

#plt.show()

fig, ax = plt.subplots()
dft = pd.read_csv('president_state.csv')
tup = ('F', 'M')
dft = dft[dft.state.str.startswith(tup)]
dft = dft.sort_values('total_votes', ascending=False)
x = dft['state']
y = dft['total_votes']
ax.bar(x,y)
ax.set(title='State Votes for 2020 US Election Chart#4',
       ylabel='#Votes (mm)',
       xlabel='States')
ax.tick_params(axis='x',rotation=60)
plt.style.use('fivethirtyeight')

plt.show()


fig, ax = plt.subplots()
dft = pd.read_csv('president_state.csv')
tup = ('F', 'M')
y = list(tup)
y.append('I')
tup = tuple(y)

dft = dft[dft.state.str.startswith(tup)]
dft = dft.sort_values('total_votes', ascending=False)
x = dft['state']
y = dft['total_votes']
ax.bar(x,y)
ax.set(title='State Votes for 2020 US Election Chart#5',
       ylabel='#Votes (mm)',
       xlabel='States')
ax.tick_params(axis='x',rotation=60)
plt.style.use('fivethirtyeight')
plt.show()

#######Pie Chart#1 using 2016 data - votes per party
df2 = pd.read_csv('primary_results_2016.csv')
output3 = df2
df_group3 = output3.groupby(['party'],as_index=False).sum().sort_values(by = 'votes', ascending= True).head(20)
plt.style.use("fivethirtyeight")
slices = df_group3['votes']
lables = df_group3['party']
plt.pie(slices, labels=lables)
plt.title('2016 US Election by Party')
plt.tight_layout()
plt.show()

#######Pie Chart#1 using 2020 data - votes per party
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


