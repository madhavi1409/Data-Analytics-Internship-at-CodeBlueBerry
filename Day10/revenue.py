import numpy as np
revenue = np.array([25000, 30000, 28000, 35000, 32000, 40000])
print("Monthly Revenue", revenue)
print("Total Revenue", np.sum(revenue))
print("Average Revenue", np.mean(revenue))
print("Highest Revenue", np.max(revenue))
print("Lowest Revenue", np.min(revenue))