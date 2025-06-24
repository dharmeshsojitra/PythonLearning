import pandas as pd


data = {
    "name":['Raj','Anupa']
    , "age":[45, 55]
    , "salary":[1000000, 200000]
    , "designation": ['CEO','COO']
}

dataframe = pd.DataFrame(data)

shape = dataframe.shape
print(shape)
print(f'the no of rows in the dataframe is {shape[0]}')
columns = dataframe.columns
print(columns)