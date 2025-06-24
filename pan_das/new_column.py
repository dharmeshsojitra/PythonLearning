import pandas as pd

data = {
    "name":['Alen','Joy', 'Roy', 'Mark', 'Alice', 'Bob', 'Ricky']
    , "age":[45, 55,23,54,34,23,56]
    , "salary":[1000000, 8000000,4300000, 5400000, 2100000, 200000,500000]
    , "designation": ['CEO','COO', 'SDM', 'MD', 'SWD', 'QA', 'CP']
}

dataframe = pd.DataFrame(data)
print(dataframe)

print('*'* 100)

dataframe["bonus"] = dataframe["salary"] * 0.1

print(dataframe)


print('*'*20 + 'using insert method' + '*'*20)

dataframe.insert(0, "emp_id", [1,2,3,4,5,6,7])
print(dataframe)
