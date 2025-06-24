import pandas as pd
data = {
    "name":['Alen','Jack', 'Roy', 'Mark', 'Alice', 'Bob', 'Ricky']
    , "age":[45, 55,23,19,34,23,56]
    , "salary":[1000000, 900000,4300000, 25400000, 2100000, 400000,900000]
    , "designation": ['CEO','COO', 'SDM', 'MD', 'SWD', 'QA', 'CP']
}

dataframe = pd.DataFrame(data)
print(dataframe)

dataframe.sort_values(by=['age', 'salary'], ascending=[True,False], inplace=True)
print('* ' *  30 + 'after sorting'+ '* ' * 30)

print(dataframe)