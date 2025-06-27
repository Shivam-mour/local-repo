"""
problems:-
1- how bigis your dataset
2- what are the names of columns

solution:- .shape and .columns
"""

import pandas as pd
data = {
    "Name" : ['Raj','Shayam','Ghanshyam','daman','loki'],
    "Age" : [10,20,30,40,50],
    "Salary" : [60000,90000,49999,9444,4444]
}

df = pd.DataFrame(data)
print(f'Shape: {df.shape}\nColumns: {df.columns}')
print(pd.options.display.max_rows)