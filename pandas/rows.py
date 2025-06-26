#head() tail()
#head(n) default=5
#tail(n)

import pandas as pd

df = pd.read_csv("sales_data_sample.csv", encoding="latin1", )
print("Print First 10 Rows")
print(df.head(10))
print("Print Last 10 Rows")
print(df.tail(10))