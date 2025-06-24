import pandas as pd

print('printing info of csv')
data_frame = pd.read_csv('../datasets/sales_data_sample.csv', encoding= 'latin1')
print(data_frame.info())

print(50 * '*')
print('printing info of csv')
excel_dataframe = pd.read_excel('../datasets/SampleSuperstore.xlsx', )

print(excel_dataframe.info())