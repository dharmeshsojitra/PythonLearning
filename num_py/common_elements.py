import numpy as np

a = np.array([1,2,3,4,5])

b = np.arange(5)

common_arr = np.intersect1d(a,b)
print(common_arr)