import pandas as pd

data = {
    "Name" : ['Ram',None,'Ghanshyam','dhanshayam','Aditi','Jagdish','Raj','simran'],
    "Age" : [28,None,90,80,78,78,74,74],
    "Salary" : [50000,None,8800,99499,4485,84848,9494,49944],
    "Performance" : [9,None,6,7,8,9,8,8]
}

df = pd.DataFrame(data)
# filing the missing valuees
# .fillna( value ,inplace= True)
df.fillna(9,inplace=True)
print(df)
 #
df["Age"] = df["Age"].fillna(df['Age'].mean())
print(df)