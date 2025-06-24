import pandas as pd

dataset  = {
    "name": ["John", 'Alice', 'Bob'],
    "age":[10,20,30],
    "city":['Mumbai','Delhi','Pune']
}

df = pd.DataFrame(dataset)
print(df)

df.to_csv("../datasets/name.csv", index=False)

df.to_excel("../datasets/name.xlsx", index=False)

df.to_json("../datasets/name.json", orient="records")