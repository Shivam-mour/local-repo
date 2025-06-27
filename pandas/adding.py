import pandas as pd

data = {
    "Name" : ['Ram','shayam','Ghanshyam','dhanshayam','Aditi','Jagdish','Raj','simran'],
    "Age" : [28,29,90,80,78,78,74,74],
    "Salary" : [50000,90000,8800,99499,4485,84848,9494,49944],
    "Performance" : [9,8,6,7,8,9,8,8]
}

df = pd.DataFrame(data)
df['Bonus'] = df['Salary'] * 0.1
print(df)

#using insert method
#df.insert(index, "column_name", value)

df.insert(0, "Employee ID", [0,1,2,3,4,5,6,7])
print(df)