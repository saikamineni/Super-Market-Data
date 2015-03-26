from pandas import read_csv
import pandas as pd
import numpy as np
import datetime


location = "C:\Users\saisree849\Documents\GitHub\Super-Market-Data\\3_Granular_items\janitems.csv"
df = pd.read_csv(location)

df.columns = ['IndexNo', 'BillNo', 'Date', 'Time', 'Description','Item', 'Quantity', 'Rate', 'Amount']
df = df.drop('IndexNo', axis=1)

df = df[np.isfinite(df['Rate'])]
lis = pd.Series()
for i in range(0 ,max(df.index)+1):
    lis = lis.set_value(i, 'UNNAMED')
    
df.insert(2,'Day',lis,allow_duplicates=False)

for idx, record in df['Date'].iteritems():
    day, month, year = (int(x) for x in record.split('/'))    
    ans = datetime.date(year, month, day)
    df.loc[idx, 'Day'] = ans.strftime("%A").upper()
    
df.to_csv("C:\Users\saisree849\Documents\GitHub\Super-Market-Data\\3_Item_weekday\janday.csv", sep = ",")



location = "C:\Users\saisree849\Documents\GitHub\Super-Market-Data\\3_Granular_items\\febitems.csv"
df = pd.read_csv(location)

df.columns = ['IndexNo', 'BillNo', 'Date', 'Time', 'Description','Item', 'Quantity', 'Rate', 'Amount']
df = df.drop('IndexNo', axis=1)

df = df[np.isfinite(df['Rate'])]
lis = pd.Series()
for i in range(0 ,max(df.index)+1):
    lis = lis.set_value(i, 'UNNAMED')
    
df.insert(2,'Day',lis,allow_duplicates=False)

for idx, record in df['Date'].iteritems():
    day, month, year = (int(x) for x in record.split('/'))    
    ans = datetime.date(year, month, day)
    df.loc[idx, 'Day'] = ans.strftime("%A").upper()
    
df.to_csv("C:\Users\saisree849\Documents\GitHub\Super-Market-Data\\3_Item_weekday\\febday.csv", sep = ",")



location = "C:\Users\saisree849\Documents\GitHub\Super-Market-Data\\3_Granular_items\maritems.csv"
df = pd.read_csv(location)

df.columns = ['IndexNo', 'BillNo', 'Date', 'Time', 'Description','Item', 'Quantity', 'Rate', 'Amount']
df = df.drop('IndexNo', axis=1)

df = df[np.isfinite(df['Rate'])]
lis = pd.Series()
for i in range(0 ,max(df.index)+1):
    lis = lis.set_value(i, 'UNNAMED')
    
df.insert(2,'Day',lis,allow_duplicates=False)

for idx, record in df['Date'].iteritems():
    day, month, year = (int(x) for x in record.split('/'))    
    ans = datetime.date(year, month, day)
    df.loc[idx, 'Day'] = ans.strftime("%A").upper()
    
df.to_csv("C:\Users\saisree849\Documents\GitHub\Super-Market-Data\\3_Item_weekday\marday.csv", sep = ",")



location = "C:\Users\saisree849\Documents\GitHub\Super-Market-Data\\3_Granular_items\\apritems.csv"
df = pd.read_csv(location)

df.columns = ['IndexNo', 'BillNo', 'Date', 'Time', 'Description','Item', 'Quantity', 'Rate', 'Amount']
df = df.drop('IndexNo', axis=1)

df = df[np.isfinite(df['Rate'])]
lis = pd.Series()
for i in range(0 ,max(df.index)+1):
    lis = lis.set_value(i, 'UNNAMED')
    
df.insert(2,'Day',lis,allow_duplicates=False)

for idx, record in df['Date'].iteritems():
    day, month, year = (int(x) for x in record.split('/'))    
    ans = datetime.date(year, month, day)
    df.loc[idx, 'Day'] = ans.strftime("%A").upper()
    
df.to_csv("C:\Users\saisree849\Documents\GitHub\Super-Market-Data\\3_Item_weekday\\aprday.csv", sep = ",")



location = "C:\Users\saisree849\Documents\GitHub\Super-Market-Data\\3_Granular_items\mayitems.csv"
df = pd.read_csv(location)

df.columns = ['IndexNo', 'BillNo', 'Date', 'Time', 'Description','Item', 'Quantity', 'Rate', 'Amount']
df = df.drop('IndexNo', axis=1)

df = df[np.isfinite(df['Rate'])]
lis = pd.Series()
for i in range(0 ,max(df.index)+1):
    lis = lis.set_value(i, 'UNNAMED')
    
df.insert(2,'Day',lis,allow_duplicates=False)

for idx, record in df['Date'].iteritems():
    day, month, year = (int(x) for x in record.split('/'))    
    ans = datetime.date(year, month, day)
    df.loc[idx, 'Day'] = ans.strftime("%A").upper()
    
df.to_csv("C:\Users\saisree849\Documents\GitHub\Super-Market-Data\\3_Item_weekday\mayday.csv", sep = ",")