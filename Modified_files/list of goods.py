import pandas as pd


Location = 'C:\Users\saisree849\Documents\GitHub\Super-Market-Data\extracted_data_files\jan14.csv'
df = pd.read_csv(Location)
lis = []
#lis.append("Description")

for record in df['Description']:
    lis.append(record)
    

Location = 'C:\Users\saisree849\Documents\GitHub\Super-Market-Data\extracted_data_files\\feb14.csv'
df = pd.read_csv(Location)

for record in df['Description']:
    lis.append(record)
    

Location = 'C:\Users\saisree849\Documents\GitHub\Super-Market-Data\extracted_data_files\mar14.csv'
df = pd.read_csv(Location)

for record in df['Description']:
    lis.append(record)
    

Location = 'C:\Users\saisree849\Documents\GitHub\Super-Market-Data\extracted_data_files\\apr14.csv'
df = pd.read_csv(Location)

for record in df['Description']:
    lis.append(record)
    

Location = 'C:\Users\saisree849\Documents\GitHub\Super-Market-Data\extracted_data_files\may14.csv'
df = pd.read_csv(Location)

for record in df['Description']:
    lis.append(record)
    

output = []
for x in lis:
    if x not in output:
        output.append(x)
        
output = sorted(output)
output.insert(0, 'Description')

new_file = open("C:\Users\saisree849\Documents\GitHub\Super-Market-Data\Modified_files\uniquegoodslist.txt", "a")
for item in output:
  new_file.write("%s\n" % item)

new_file.close()