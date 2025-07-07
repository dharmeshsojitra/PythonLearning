import numpy as np

arr = np.arange(30)

odd_arr = arr[(arr%2 ==1 ) & (arr >24)]
print(odd_arr)