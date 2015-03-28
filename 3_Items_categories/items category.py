from pandas import read_csv, Series
import pandas as pd
import re

Location = "C:\Users\saisree849\Documents\GitHub\Super-Market-Data\\3_Item_weekday\janday.csv"
df = pd.read_csv(Location)

df.columns = ['IndexNo', 'BillNo', 'Date', 'Day', 'Time', 'Description', 'Item', 'Quantity', 'Rate', 'Amount']
df = df.drop('IndexNo', axis=1)


lis = pd.Series()
for i in range(0 ,max(df.index)+1):
    lis = lis.set_value(i, 'UNNAMED')

df.insert(6,'Category',lis,allow_duplicates=False)

for idx, record in df['Item'].iteritems():
    if (re.search("ATTA", record) or re.search("BAKERY ITEMS", record) or re.search("BATTER", record) or re.search("BISCUITS", record) or re.search("CEREAL", record) or re.search("CHOCOLATE", record) or re.search("COCONUT", record) or re.search("COFFEE", record) or re.search("COOKING ITEMS", record) or re.search("COOKING OIL", record) or re.search("DRY FRUITS", record) or re.search("EGG", record) or re.search("ENERGY DRINKS", record) or re.search("GENERAL", record) or re.search("HONEY", record) or re.search("ICE CREAM", record) or re.search("INSTANT MIXES", record) or re.search("JAGGERY", record) or re.search("JAM", record) or re.search("KITCHEN PASTES", record) or re.search("KITCHEN POWDERS", record) or re.search("MAIDA", record) or re.search("MASALA", record) or re.search("MILK", record) or re.search("MILK PRODUCTS", record) or re.search("NOODLES", record) or re.search("ONIONS", record) or re.search("PAPAD", record) or re.search("PICKLES", record) or re.search("POPCORN", record) or re.search("PULSES", record) or re.search("RAVA", record) or re.search("RICE", record) or re.search("SALT", record) or re.search("SAUCE", record) or re.search("SNACKS", record) or re.search("SOUNF", record) or re.search("SPICES", record) or re.search("SUGAR", record) or re.search("TEA", record) or re.search("TURMERIC", record)) and df.loc[idx, 'Category'] == "UNNAMED":
        df.loc[idx,'Category'] = 'FOOD'
        
for idx, record in df['Item'].iteritems():
    if (re.search("BABY CARE", record) or re.search("BODY CARE", record) or re.search("BODY SOAP", record) or re.search("COMB", record) or re.search("DENTAL CARE", record) or re.search("DIAPERS", record) or re.search("HAIR CARE", record) or re.search("HAIR OIL", record) or re.search("HAIR REMOVALS", record) or re.search("HEALTH CARE", record) or re.search("SANITARY PADS", record) or re.search("SHAMPOO", record)) and df.loc[idx, 'Category'] == "UNNAMED":
        df.loc[idx,'Category'] = 'PERSONAL CARE'

for idx, record in df['Item'].iteritems():
    if (re.search("AIR FRESHENERS", record) or re.search("BATTERIES", record) or re.search("CARRY BAG", record) or re.search("CUTLERY", record) or re.search("DETERGENT", record) or re.search("DISH CLEANER", record) or re.search("FLOOR CLEANER", record) or re.search("INSECT REPELLENT", record) or re.search("HAIR REMOVALS", record) or re.search("LIGHTS", record) or re.search("MACHINES", record) or re.search("MATCHES", record) or re.search("PARTY NEEDS", record) or re.search("PLASTIC", record) or re.search("POOJA ITEMS", record) or re.search("TISSUE", record)) and df.loc[idx, 'Category'] == "UNNAMED":
        df.loc[idx,'Category'] = 'HOUSE HOLD CARE'

for idx, record in df['Item'].iteritems():
    if(re.search("BEVERAGES", record)) and df.loc[idx, 'Category'] == "UNNAMED":
        df.loc[idx,'Category'] = 'BEVERAGES'

for idx, record in df['Item'].iteritems():
    if(re.search("STATIONARY", record)) and df.loc[idx, 'Category'] == "UNNAMED":
        df.loc[idx,'Category'] = 'STATIONARY'

for idx, record in df['Item'].iteritems():
    if(re.search("OTHER", record) or re.search("RECHARGE", record) or re.search("SPORTS", record)) and df.loc[idx, 'Category'] == "UNNAMED":
        df.loc[idx,'Category'] = 'OTHER'

df.to_csv("C:\Users\saisree849\Documents\GitHub\Super-Market-Data\\3_Items_categories\jancat.csv", sep = ",")