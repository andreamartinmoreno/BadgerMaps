import pandas as pd

#Pandas dataframe view settings
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)

#Reading csv file
df = pd.read_csv('sampletest1.csv')

#Edit object typo from date types
df["Last Check-In Date"] = pd.to_datetime(df["Last Check-In Date"],
                                          infer_datetime_format=True)
print(df, '\n')

for n in range(len(df)):
 if(df.isnull().iloc[n]['Street']):
  print('Street of this register',n,'is empty')
 if(df.isnull().iloc[n]['Zip']):
  print('Zip of this register: ',n,' is empty')
 if(df.isnull().iloc[n]['City']):
  print('City of this register: ',n,' is empty')
 if(df.isnull().iloc[n]['Last Check-In Date']):
  print('Last Check-In Date of this register: ',n,' is empty')
 if(df.isnull().iloc[n]['Company']):
  print('Company of this register: ',n,' is empty')
print('\n')


#Tasks

#Retrieve the customer with the earliest check in date
df.sort_values(by=["Last Check-In Date"], inplace=True)
if(df.isnull().iloc[0,2]):
  print('Street of this register is empty')
if(df.isnull().iloc[0,3]):
  print('Zip of this register is empty')
if(df.isnull().iloc[0,4]):
  print('City of this register is empty')
if(df.isnull().iloc[0,6]):
  print('Last Check-in Date of this register is empty')
if(df.isnull().iloc[0,9]):
  print('Company of this register is empty')
  
print(df.iloc[0], '\n')

#Retrieve the customer with the latest check in date
df.sort_values(by=["Last Check-In Date"], inplace=True, ascending=False)
if(df.isnull().iloc[0,2]):
  print('Street of this register is empty')
if(df.isnull().iloc[0,3]):
  print('Zip of this register is empty')
if(df.isnull().iloc[0,4]):
  print('City of this register is empty')
if(df.isnull().iloc[0,6]):
  print('Last Check-in Date of this register is empty')
if(df.isnull().iloc[0,9]):
  print('Company of this register is empty')
  
print(df.iloc[0], '\n')

#Retrieve a list of customer’s full names ordered alphabetically.
df.sort_values(by=["Last Name"], inplace=True, ascending=True)
print(df[['First Name', 'Last Name']], '\n')

#Retrieve a list of the companies user’s jobs ordered alphabetically.
df.sort_values(by=["Job"], inplace=True, ascending=True)
print(df[['First Name', 'Last Name', 'Job', 'Company']], '\n')


