import pandas as pd

#Pandas dataframe view settings
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)

#Reading csv file
df = pd.read_csv('sampletest1.csv')
print(df.dtypes)
print(df)
df["Last Check-In Date"] = pd.to_datetime(df["Last Check-In Date"],
                                          infer_datetime_format=True)
print(df.dtypes)
df.sort_values(by=["Last Check-In Date"], inplace=True)
print(df)
print(df.iloc[0])

#queryName = "`First Name` != 'Anselmo'"
#dfname = df.query(queryName)
#print(dfname)#
