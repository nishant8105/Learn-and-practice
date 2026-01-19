import numpy as np
# ### Broadcasting
# Broadcasting allows Numpy to perform opertaions on arrays with different shapes by virtually expanding demensions so they match the larger arrays's shape
# the demensions have the same size
#                 OR
# One of the dimension has a size of 1

array1 = np.array([[1, 2, 3, 4]])
array2 = np.array([[1], [2], [3],[4]])

print(array1.shape)
print(array2.shape)

print( array1 * array2)
array1 = np.array([[1, 2, 3, 4],[5, 6, 7, 8]])
print(array1.shape)
print(array2.shape)
# print( array1 * array2) error


array1 = np.array([
    [ 1, 2, 3,  4],
    [ 2,  4,  6,  8],
    [ 3,  6,  9, 12],
    [ 4,  8, 12, 16]
 ])
print(array1.shape)
print(array2.shape)
print(array1 * array2)


array2 = np.array([[1, 5], [2, 6], [3, 7],[4, 8]])
print(array1.shape)
print(array2.shape)
# print(array1 * array2)Error


# ### Multiplication Table


array1 = np.array([[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]])
array2 = np.array([[1], [2], [3], [4], [5], [6], [7], [8], [9], [10]])
print(array1.shape)
print(array2.shape)
print(array1 * array2)
