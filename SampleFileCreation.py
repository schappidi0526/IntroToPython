import pandas as pd
data=pd.read_excel("C:\\Users\\kumar\\Downloads\\countries_population.xls")
print(data)
#if we want to see just the first 5 rows of the data
print(data.head())
print(data.head(3))
#if we want to see just the last 5 rows of the data
print(data.tail())
print(data.tail(3))