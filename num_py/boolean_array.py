import numpy as np

bool_arr = np.full((3,3), True)
print(bool_arr)
print(bool_arr.reshape(1,9))
print(bool_arr.dtype)