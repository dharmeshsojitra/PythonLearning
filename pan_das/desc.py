import pandas as pd

json_dataframe = pd.read_json('../datasets/sample_Data.json')

print(json_dataframe.describe())

print('*'*50)

excel_dataframe = pd.read_excel('../datasets/SampleSuperstore.xlsx')
print(excel_dataframe.describe())