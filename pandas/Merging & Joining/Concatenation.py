'''
vertically (row-wise)
horizontally (column wise)

pd.concate([df1, df2], axis=0, ignore_index=True)
'''
import pandas as pd

#region 1
df_region1 = pd.DataFrame({
    'CustomerID' : [1,2],
    'Name' : ['Gopal','Nomi']
})

#region 2
df_region2 = pd.DataFrame({
    'CustomerID' : [3,4],
    'Name' : ['Shami','Shayum']
})

#concatinate
df_con = pd.concat([df_region1,df_region2], axis=1, ignore_index=False)
print(df_con)