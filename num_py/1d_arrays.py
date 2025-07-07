import numpy as np

one_d = np.array([1,2,3])
print(one_d)


print('type of the array is using type(): ', type(one_d))
print('type of the one_d array is: ',one_d.dtype)

print('is one_d array type of str? : ', isinstance(one_d, str))


print('*' * 15 +' using arange() to create a np array' + '*' * 15)

range_array = np.arange(10)
print(range_array)


range_array = np.arange(2, 10)
print(range_array)

range_array = np.arange(2, 10, 2)
print(range_array)