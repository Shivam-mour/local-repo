import pandas as pd

data = {
    "Name" : ['Ram','shayam','Ghanshyam','dhanshayam','Aditi','Jagdish','Raj','simran'],
    "Age" : [28,29,90,80,78,78,74,74],
    "Salary" : [50000,90000,8800,99499,4485,84848,9494,49944],
    "Performance" : [9,8,6,7,8,9,8,8]
}

df = pd.DataFrame(data)
high_salary = df[df['Salary']> 50000]
print(high_salary)

#filter multiple conditions
#BOTH CONDITION HAS TO BE CORRECT : &
filtered = df[(df['Age']>35) & (df['Salary']>50000)]
print(filtered)

#Any one condition ha sto be correct : OR
filtered_OR = df[(df['Age']>35) | (df['Salary']>50000)]
print(filtered_OR)