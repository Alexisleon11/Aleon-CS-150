import pandas as pd

df = pd.DataFrame({'age': 18,
                   'name': ['Alice', 'Bob', 'Carl'],
                   'cardio': [60, 70, 80]})

df.loc[1:1,'age'] = 21
df.loc[2:2,'age'] = 23
print(df)