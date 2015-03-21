import pandas as pd
import re

Location = 'C:\Users\saisree849\Documents\GitHub\Super-Market-Data\Modified_files\catlist.txt'
df = pd.read_csv(Location)

df['Description'] = df['Description'].map(str.strip)

for num1 in range(0 ,max(df.index)+1):
    for num2 in range(0 ,max(df.index)+1):
        if (re.search(df.loc[num1, 'Description'], df.loc[num2, 'Description'])):
            if (re.match(r'(.*)\s+(.*)', df.loc[num1,'Description'])):
                matchobj = re.match(r'(.*)\s+(.*)', df.loc[num1,'Description'])
                df.loc[num1,'Description'] = matchobj.group(1)
                break

for num1 in range(0 ,max(df.index)+1):
    for num2 in range(0 ,max(df.index)+1):
        if (re.search(df.loc[num1, 'Description'], df.loc[num2, 'Description'])):
            if (re.match(r'(.*)\s+(.*)', df.loc[num1,'Description'])):
                matchobj1 = re.match(r'(.*)\s+(.*)', df.loc[num1,'Description'])
                if not (len(matchobj1.group(1)) == 1):
                    df.loc[num1,'Description'] = matchobj1.group(1)
                    break
                    
for num1 in range(0 ,max(df.index)+1):
    df.loc[num1,'Description'] = str(df.loc[num1,'Description']+" ")
    
    
new_file = "C:\Users\saisree849\Documents\GitHub\Super-Market-Data\Modified_files\correctedlist1.csv"
df.to_csv(new_file,sep = ",")