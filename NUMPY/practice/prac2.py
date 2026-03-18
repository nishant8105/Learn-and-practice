# Given the array below, use boolean indexing to extract all elements greater than 5, then replace all elements less than or equal to 5 with 0.
# arr = np.array([3, 8, 1, 6, 2, 9, 4, 7, 5])
# Task 1 → extract elements > 5
# Task 2 → replace elements <= 5 with 0 (in-place)


import numpy as np
arr = np.array([3, 8, 1, 6, 2, 9, 4, 7, 5])

task1 = arr[arr > 5]
print(f"Array of greater than 5 :{task1}")

arr[arr <= 5] = 0
print(f"Replace all element less than or equal to 5 with 0 : {arr}")