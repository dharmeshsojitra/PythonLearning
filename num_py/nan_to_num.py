import numpy as np

arr = np.array([1, 2, 3, np.nan, 5])

print(arr)

print(np.isnan(arr) )

clean_arr = np.nan_to_num(arr)

print(clean_arr)

clean_arr = np.nan_to_num(arr, nan=1000)
print(clean_arr)
print(arr)


arr = np.array([1, 2, 3, np.nan, 5])


clean_arr = np.nan_to_num(arr, nan=1000, copy=False)
print(clean_arr)
print(arr)

arr = np.array([1, 2, 3, np.nan, 5])


clean_arr = np.nan_to_num(arr, nan=1000, copy=True)
print(clean_arr)
print(arr)
