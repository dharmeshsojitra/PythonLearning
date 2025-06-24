import pandas as pd

data = {
    "name":['Alen','Jack', 'Jack', 'Mark', 'Alice', 'John', 'Ricky']
    , "age":[45, 55,23,19,34,23,56]
    , "salary":[1000000, 900000,4300000, 2400000, 2100000, 400000,900000]
    , "designation": ['CEO','COO', 'SDM', 'MD', 'SWD', 'QA', 'CP']
}

df =pd.DataFrame(data)

print(df)

grp_by_name = df.groupby('name')["salary"].sum()

print(grp_by_name)