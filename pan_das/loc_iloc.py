import pandas as pd
data = {
    "id":[1,2,3,4,5,6,7]
    ,"name":['Alen','Joy', 'Roy', 'Mark', 'Alice', 'Bob', 'Ricky']
    , "age":[45, 55,23,54,34,23,56]
    , "salary":[1000000, 8000000,4300000, 5400000, 2100000, 200000,500000]
    , "designation": ['CEO','COO', 'SDM', 'MD', 'SWD', 'QA', 'CP']
}

dataframe = pd.DataFrame(data).set_index('id')
print(dataframe)

print(dataframe.loc[3])

print(dataframe.iloc[:3])
print(dataframe.iloc[2][2])