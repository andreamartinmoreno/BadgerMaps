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
print('OUR DATAFRAME \n')
print(df, '\n')

#Exceptions
#Testing for specified fields
print('Exceptions \n')
for n in range(len(df)):
  if (df.isna().iloc[n]['Street']):
    print('Street of this register', n, 'is empty')
  if (df.isna().iloc[n]['Zip']):
    print('Zip of this register: ', n, ' is empty')
  if (df.isna().iloc[n]['City']):
    print('City of this register: ', n, ' is empty')
  if (df.isna().iloc[n]['Last Check-In Date']):
    print('Last Check-In Date of this register: ', n, ' is empty')
  if (df.isna().iloc[n]['Company']):
    print('Company of this register: ', n, ' is empty')
print('\n')


#Testing for empty rows
shape=df.shape
x=0
for n in range(len(df)):
  for m in range(shape[1]):
    if df.isna().iloc[n,m]:
      x+=1
    if x==shape[1]:
      print('Row number:',n,'is empty hola. \n')
  x=0

#Testing for empty fields
for a in range(len(df)):
  for b in range(shape[1]):
    if df.isna().iloc[a,b]:
      print('The row', a, 'contains field:', df.columns[b], 'empty')
      
      
#Tasks

#Retrieve the customer with the earliest check in date
print('Tasks \n\n')
print('Retrieve the customer with the earliest check in date \n')
df.sort_values(by=["Last Check-In Date"], inplace=True) 
print(df.iloc[0], '\n')

#Retrieve the customer with the latest check in date
print('Retrieve the customer with the latest check in date \n')
df.sort_values(by=["Last Check-In Date"], inplace=True, ascending=False)
print(df.iloc[0], '\n')

#Retrieve a list of customer’s full names ordered alphabetically.
print('Retrieve a list of customer’s full names ordered alphabetically \n')
df.sort_values(by=["Last Name"], inplace=True, ascending=True)
cust_list = df[['First Name', 'Last Name']].values.tolist()
print(cust_list, '\n')

#Retrieve a list of the companies user’s jobs ordered alphabetically.
print('Retrieve a list of the companies user’s jobs ordered alphabetically \n')
df.sort_values(by=["Job"], inplace=True)
jobs_list = df['Job'].values.tolist()
print(jobs_list, '\n')
