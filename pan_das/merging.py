import pandas as pd

orders = pd.DataFrame({
    "cust_id":[1,2,3]
    , 'order_id':[989, 3783, 8937]
    ,"order_amount":[844, 334,3334]
})

return_orders =  pd.DataFrame({
    "order_id":[989, 8937]
    , "return_amount":[432, 22]
    , "item_id": [23,45]
})

print('* ' * 30 + 'inner merge' + '* ' * 30)
merged_df = pd.merge(orders, return_orders, how='inner', on='order_id')
print(merged_df)

print('* ' * 30 + 'outer merge' + '* ' * 30)
merged_df = pd.merge(orders, return_orders, how='outer', on='order_id')
print(merged_df)

print('* ' * 30 + 'left merge' + '* ' * 30)
merged_df = pd.merge(orders, return_orders, how='left', on='order_id')
print(merged_df)

print('* ' * 30 + 'right merge' + '* ' * 30)
merged_df = pd.merge(orders, return_orders, how='right', on='order_id')
print(merged_df)
