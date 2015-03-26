import pandas as pd


Location = 'C:\Users\saisree849\Documents\GitHub\Super-Market-Data\Expanded_Description\jandesc.csv'
df = pd.read_csv(Location)
df.columns = ['IndexNo', 'BillNo', 'Date', 'Time', 'Description', 'Quantity', 'Rate', 'Amount']
lis = []
#lis.append("Description")
for record in df['Description']:
    lis.append(record)
    

Location = 'C:\Users\saisree849\Documents\GitHub\Super-Market-Data\Expanded_Description\\febdesc.csv'
df = pd.read_csv(Location)
df.columns = ['IndexNo', 'BillNo', 'Date', 'Time', 'Description', 'Quantity', 'Rate', 'Amount']

for record in df['Description']:
    lis.append(record)
    


Location = 'C:\Users\saisree849\Documents\GitHub\Super-Market-Data\Expanded_Description\mardesc.csv'
df = pd.read_csv(Location)
df.columns = ['IndexNo', 'BillNo', 'Date', 'Time', 'Description', 'Quantity', 'Rate', 'Amount']

for record in df['Description']:
    lis.append(record)
    

Location = 'C:\Users\saisree849\Documents\GitHub\Super-Market-Data\Expanded_Description\\aprdesc.csv'
df = pd.read_csv(Location)
df.columns = ['IndexNo', 'BillNo', 'Date', 'Time', 'Description', 'Quantity', 'Rate', 'Amount']

for record in df['Description']:
    lis.append(record)
    

Location = 'C:\Users\saisree849\Documents\GitHub\Super-Market-Data\Expanded_Description\maydesc.csv'
df = pd.read_csv(Location)
df.columns = ['IndexNo', 'BillNo', 'Date', 'Time', 'Description', 'Quantity', 'Rate', 'Amount']

for record in df['Description']:
    lis.append(record)
    
output = []
for x in lis:
    if x not in output:
        output.append(x)
        
output = sorted(output)
output.insert(0, 'Description')

new_file = open("C:\Users\saisree849\Documents\GitHub\Super-Market-Data\Expanded_Description\listofdescriptions.txt", "a")

for item in output:
  new_file.write("%s\n" % item)
  
new_file.close()
