# Create a 1D NumPy array of integers from 1 to 12 (inclusive), then reshape it into a 3×4 matrix. Print the result and its shape.

import numpy as np
arr = np.arange(1, 13)
arr = arr.reshape(3, 4)
print(arr)
print(f"Shape :{arr.shape}")