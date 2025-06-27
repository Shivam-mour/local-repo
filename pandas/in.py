'''1-columns , rows ?
2- what type of data?
3- missing data

info()
1- number of rows and columns
2- columns name
3- int64 float object
4- non null counts
5- memory usage of the data'''


import pandas as pd


df = pd.read_csv("sales_data_sample.csv", encoding="latin1", )
print('Displaying the info of data set')
print(df.info())