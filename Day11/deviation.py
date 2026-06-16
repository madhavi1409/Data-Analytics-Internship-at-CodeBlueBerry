import numpy as np
sales = np.array([100, 200, 300,40,60,123,567,445])
print(np.std(sales))
print(np.mean(sales))
new_array = np.array([100, 200, 300, 400, 500])
new_array = np.reshape(5, 1)
print(new_array)
print(sales.flatten())
print(sales.sort())