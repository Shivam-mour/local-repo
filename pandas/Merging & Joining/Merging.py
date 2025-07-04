#pd.merge(df1, df2, on="column_Name", how="type_of_join")
import pandas as pd

#customer dataframe:
df_customers = pd.DataFrame({
    'Customer_id' : [1,2,3,],
    'Customer_name' : ["Suresh","Ramesh","Jignesh"]
})

#orders dataset:
df_orders = pd.DataFrame({
    'Customer_id' : [1,2,4],
    'Product_amount' : [200,9000,90]
})

#merging
merging = pd.merge(df_customers, df_orders, on="Customer_id", how='inner')
print('Inner Join')
print(merging)

merging = pd.merge(df_customers, df_orders, on="Customer_id", how='outer')
print('Outer Join')
print(merging)

merging = pd.merge(df_customers, df_orders, on="Customer_id", how='right')
print('Right Join')
print(merging)

merging = pd.merge(df_customers, df_orders, on="Customer_id", how='left')
print('Left Join')
print(merging)