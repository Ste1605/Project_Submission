import pandas as pd
import re
trumptweets= pd.read_csv("trumptweets.csv",nrows=42)
df = trumptweets

example_string = df.to_string()
output_file = open('output.csv','a')
output_file.write(example_string)


print(df.shape)
print(df.head)
string = "1698308935,https://twitter.com/realDonaldTrump/status/1698308935,Be sure to tune in and watch Donald Trump on Late Night with David Letterman as he presents the Top Ten List tonight!,2009-05-04 20:54:25,500,868,,,"




#print(trumptweets.head())
#print(trumptweets.shape)

#cleaned_data = trumptweets.fillna("")
#print(cleaned_data.head())
#print(cleaned_data.shape)

#droprows= trumptweets.dropna()
#print(trumptweets.shape,droprows.shape)

#dropcolumns= trumptweets.dropna(axis=1)
#print(trumptweets.shape,dropcolumns.shape)

#missing_values_count = trumptweets.isnull().sum()
#print(missing_values_count[0:9])

#string="realDonaldTrump/status"
#result=re.findall("realDonaldTrump/status",string)
#print(result)

result=re.findall("^\d*,[\w:/.]*,([^,]*)",string)
result2=re.findall("^\d*,[\w:/.]*,([^,]*)","trumptweets")

#df = pd.read_csv('trumptweets.csv')
#print(df['content'])

print(result2)






