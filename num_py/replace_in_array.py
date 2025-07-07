import numpy as np

x = np.arange(10)

out  = x.copy()


out[out %2 == 0] = -1
print(out)
print(x)