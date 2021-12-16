import pandas as pd
df = pd.read_csv('president_county_candidate.csv')

#index_list = df.index.tolist()
#print(index_list)

#state_name_list = df["state"].tolist()
#print(state_name_list)

#state_name_list = df["state"].unique()
state_name_list = df["state"].tolist()
#print(state_name_list)
#print(state_name_list.shape)

#county_name_list = df["county"].unique()
county_name_list = df["county"].tolist()
#print(county_name_list)
#print(county_name_list.shape)

#e = enumerate(county_name_list)
#print(type(e))

#e_list = list(e)
#print(e_list)

#for index, value in enumerate(county_name_list):
#    print(index,value)

#z = zip(state_name_list, county_name_list)
#print(type(z))

#z_list = list(z)
#print(z_list)

result = []
for chunk in pd.read_csv('president_county_candidate.csv', chunksize=1000):
    result.append(sum(chunk['total_votes']))
total = sum(result)
print("The total number of votes in the 2020 US Presidential election were",total)