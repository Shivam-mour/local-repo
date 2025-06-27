import pandas as pd

data = {
    "Name" : ['Ram','shayam','Ghanshyam','dhanshayam','Aditi','Jagdish','Raj','simran'],
    "Age" : [28,29,90,80,78,78,74,74],
    "Salary" : [50000,90000,8800,9949,4485,84848,9494,49944],
    "Performance" : [9,8,6,7,8,9,8,8]
}

df = pd.DataFrame(data)
print(df)

#display single column
# print(df["Name"])
# print(df["Age"])
# print(df["Salary"])
# print(df["Performance"])

#diplat multiple column
subset = df[["Name" , "Salary"]]
print(subset)