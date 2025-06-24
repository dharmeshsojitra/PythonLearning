import pandas as pd

dataset = {
    "name":['hoff', 'Crawley', 'Anderson', 'Mullaly', 'Gough','Waugh']
    , "age":[50, 50, 43, 54,34,78]
    ,"income":[5000, 30000, 40000, 23333, 30000, 9000]
}

dataframe = pd.DataFrame(dataset)

print(f'first 5 records :{dataframe.head()}')

print(f'first 2 records :{dataframe.head(2)}')

print(f'last 5 records :{dataframe.tail()}')

print(f'last 2 records :{dataframe.tail(2)}')