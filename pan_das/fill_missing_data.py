import pandas as pd
data = {
    "name":['Alen','Jack', 'Roy', 'Mark', 'Alice', 'Bob', 'Ricky']
    , "age":[45, 55,23,None,34,23,56]
    , "salary":[1000000, None,4300000, 5400000, 2100000, 200000,500000]
    , "designation": ['CEO','COO', 'SDM', 'MD', 'SWD', 'QA', 'CP']
}

dataframe = pd.DataFrame(data)
print(dataframe)
mean_age = dataframe.age.mean()
dataframe['age'] =dataframe['age'].fillna(mean_age)

print(dataframe)


dataframe['salary'] = dataframe['salary'].fillna(dataframe['salary'].mean())
print(dataframe)