import pandas as pd

data = {
    "Name" : ['Ram','shayam','Ghanshyam','dhanshayam','Aditi','Jagdish','Raj','simran'],
    "Age" : [28,29,90,80,78,78,74,74],
    "Salary" : [50000,90000,8800,99499,4485,84848,9494,49944],
    "Performance" : [9,8,6,7,8,9,8,8]
}

df = pd.DataFrame(data)

#sorting only one column 
# df.sort_values(by = "Name", ascending=False, inplace=True)
# print(df)

#sorting only multiple columns
df.sort_values(by = ["Age","Salary"], ascending=[True,True], inplace=True)
print(df)