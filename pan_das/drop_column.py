import pandas as pd
data = {
    "name":['Alen','Joy', 'Roy', 'Mark', 'Alice', 'Bob', 'Ricky']
    , "age":[45, 55,23,54,34,23,56]
    , "salary":[1000000, 8000000,4300000, 5400000, 2100000, 200000,500000]
    , "designation": ['CEO','COO', 'SDM', 'MD', 'SWD', 'QA', 'CP']
}

dataframe = pd.DataFrame(data)

new_df = dataframe.drop(columns=['designation'], inplace = False)

print('*'*20 +'old data frame'+'*'*20)
print(dataframe)
print('*'*20 +'new data frame'+'*'*20)
print(new_df)

dataframe.drop(columns=['designation'], inplace = True)
print('*'*20 +'old data frame after inpalce is TRUE'+'*'*20)
print(dataframe)
