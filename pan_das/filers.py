import pandas as pd

data = {
    "name":['Alen','Joy', 'Roy', 'Mark', 'Alice', 'Bob', 'Ricky']
    , "age":[45, 55,23,54,34,23,56]
    , "salary":[1000000, 200000,430000, 540000, 210000, 200000,500000]
    , "designation": ['CEO','COO', 'SDM', 'MD', 'SWD', 'QA', 'CP']
}

dataframe = pd.DataFrame(data, index = None)
print(dataframe)


salary_col = dataframe["salary"]
print(salary_col)

multi_col = dataframe[["age", "designation"]]
print(multi_col)

joy_row = dataframe[dataframe['name'] == 'Joy']
print(joy_row)

salary_more_than_750k = dataframe[dataframe['salary'] > 750000]
print(f'salary more than 750K is : \n{salary_more_than_750k}')


salary_and_age_filter = dataframe[(dataframe['salary'] > 750000) & (dataframe['age'] > 40)]
print(salary_and_age_filter)