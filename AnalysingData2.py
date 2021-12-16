import pandas as pd
import re

trumptweets2= pd.read_csv("trumptweets.csv")
df = trumptweets2
print(df.shape)
#print(df.head)
string =""

result2=re.findall("^\d*,[\w:/.]*,([^,]*)",string)
print(result2)