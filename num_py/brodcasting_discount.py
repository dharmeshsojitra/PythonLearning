import numpy as np


prices = np.array([100, 200, 300, 400, 500])

discount  = 10

final_price = prices - ( prices * discount/100 )

print(prices)
print(final_price)