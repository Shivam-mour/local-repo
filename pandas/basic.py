#importing libraries
import pandas as pd

#reading data from CSV file into a dataframe
#encoding = "latin1" | "utf-8"
df = pd.read_csv("sales_data_sample.csv", encoding="latin1", )
print(df)


