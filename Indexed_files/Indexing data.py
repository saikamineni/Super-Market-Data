#import

from pandas import DataFrame, read_csv
import pandas as pd


#read data

Location = 'C:\Users\saisree849\Documents\GitHub\Super-Market-Data\extracted_data_files\jan14.csv'
df = pd.read_csv(Location)

new_file = "C:\Users\saisree849\Documents\GitHub\Super-Market-Data\Indexed_files\indjan.csv"
df.to_csv(new_file,sep = ",")


Location = 'C:\Users\saisree849\Documents\GitHub\Super-Market-Data\extracted_data_files\\feb14.csv'
df = pd.read_csv(Location)

new_file = "C:\Users\saisree849\Documents\GitHub\Super-Market-Data\Indexed_files\indfeb.csv"
df.to_csv(new_file,sep = ",")


Location = 'C:\Users\saisree849\Documents\GitHub\Super-Market-Data\extracted_data_files\mar14.csv'
df = pd.read_csv(Location)

new_file = "C:\Users\saisree849\Documents\GitHub\Super-Market-Data\Indexed_files\indmar.csv"
df.to_csv(new_file,sep = ",")


Location = 'C:\Users\saisree849\Documents\GitHub\Super-Market-Data\extracted_data_files\\apr14.csv'
df = pd.read_csv(Location)

new_file = "C:\Users\saisree849\Documents\GitHub\Super-Market-Data\Indexed_files\indapr.csv"
df.to_csv(new_file,sep = ",")


Location = 'C:\Users\saisree849\Documents\GitHub\Super-Market-Data\extracted_data_files\may14.csv'
df = pd.read_csv(Location)

new_file = "C:\Users\saisree849\Documents\GitHub\Super-Market-Data\Indexed_files\indmay.csv"
df.to_csv(new_file,sep = ",")