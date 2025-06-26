import pandas as pd
import numpy as np

data = {
    "Name" : ['Raj','Shayam','Ghanshyam','daman','loki'],
    "Age" : [10,20,30,40,50],
    "Salary" : [60000,90000,49999,9444,4444]
}

df = pd.DataFrame(data)
print(df)
print(df.describe())
