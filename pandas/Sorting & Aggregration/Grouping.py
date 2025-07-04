import pandas as pd

data = {
    "Name" : ['Ram','shayam','Ghanshyam','dhanshayam','Aditi',],
    "Age" : [22,22,25,22,23],
    "Salary" : [40000,50000,60000,50000,60000],
}

df = pd.DataFrame(data)
grouped = df.groupby("Age")["Salary"].sum()
print(grouped)

multi_grouped = df.groupby(["Age","Name"])["Salary"].sum()
print(multi_grouped)

#different function in group
#sum()
#mean()
#count()
#min()
#max()
#std()