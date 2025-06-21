import numpy as np

arr = np.array([[1,2,23.8,4], [2,6,5,4]])
print(arr)


print(f'shape of the arr: {arr.shape}')
print(f'size of the arr : {arr.size}')
print(f' no of dimensions of the arr : {arr.ndim}')
print(f'datatypes of the arr : {arr.dtype}')


arr = np.array([1,2.3, 3.4,0.2])
print(arr.dtype)
int_arr = arr.astype(int)
print(int_arr)