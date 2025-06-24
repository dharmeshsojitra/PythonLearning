import pandas as pd
import xlrd

json_content = pd.read_json("../datasets/sample_Data.json")
print(json_content)


excel_content = pd.read_excel("../datasets/SampleSuperstore.xlsx")
print(excel_content)


csv_content = pd.read_csv("../datasets/sales_data_sample.csv", encoding="latin1")
print(csv_content)