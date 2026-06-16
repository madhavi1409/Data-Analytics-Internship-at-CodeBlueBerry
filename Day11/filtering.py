import numpy as np
marks = np.array([78, 85, 92, 88, 76])
filtered_marks = marks[marks > 80]
print("Original Marks:", marks)
print("Marks greater than 80:", filtered_marks)