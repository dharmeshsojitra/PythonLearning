import pandas as pd
data = {
    "name":['Alen',None, 'Roy', 'Mark', 'Alice', 'Bob', 'Ricky']
    , "age":[45, 55,23,54,34,23,56]
    , "salary":[1000000, 8000000,4300000, 5400000, 2100000, 200000,500000]
    , "designation": ['CEO','COO', 'SDM', 'MD', 'SWD', 'QA', 'CP']
}

dataframe = pd.DataFrame(data)

print(dataframe.isnull())

print('*' * 2 + 'get number of missing data' + '*' * 2)
print(dataframe.isnull().sum())