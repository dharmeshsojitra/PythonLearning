import numpy as np

a = np.arange(10).reshape(2,5)
b = np.arange(10).reshape(2,5)
print(a)
print(b)

vstack_arr = np.vstack((a,b))
print(vstack_arr)