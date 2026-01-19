
# ## what is numpy
# - numpy ia fundamental packages for scientific computing in python
# - numpy is a python library that provides a multidimensional array object, varies derived objects.
# ### what is numpy array
# - an array is a grid of values and it contains information about the raw saya, how to locate an element, and hoe to interpret an element.

# ## numpy vs python list
# - Advantages of using Numpy Arrays over Python Lists
# 1. consumes less memory
# 2. fast as campare to python list.
# 3. convenient to use.
#

# #### Installation Numpy
# - pip install numpy
# #### import numpy
# - import numpy as np

import numpy as np
x = np.array([1,2,3,4,5])
print(type(x),x)
x = x*2
print(type(x),x)

y = [1,2,3,4,5]
print(type(y),y)
y=y*2
print(type(y),y)
print(np.__version__)


# ### Multidimensional array

array1 = np.array(['A','B','C'])
print(f"Dimenstion of{array1} is {array1.ndim}")
print(array1.shape)
print("=======================================")
array2 = np.array([
    ['A','B','C'],
    ['D','E','F'],
    ['G','H','I']
])
print(f"Dimenstion of{array2} is {array2.ndim}")
print(array2.shape)
print("=======================================")
array3 = np.array([
    [['A','B','C'],['D','E','F'],['G','H','I']],
    [['J','K','L'],['M','N','O'],['P','Q','R']],
    [['S','T','U'],['R','W','X'],['Y','Z','  ']]
])
print(f"Dimenstion of{array3} is {array3.ndim}")
print(array3.shape)
print("=======================================")


print(array3[0][0][0])
print(array3[0,0,0])
word = array3[0,0,0]+array3[1,2,0]+array3[1,2,0]+array3[1,0,2]+array3[0,1,1]
print(word)

array = np.array([
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
])
# array[strat:end:step] Subscript operator
print("Row")
print("array[0]:",array[0])
print( " ")
print("array[1]:",array[1])
print( " ")
print("array[2]:",array[2])
print( " ")
print("array[3]:",array[3])
print( " ")
print("array[0:3]:",array[0:3])
print( " ")
print("array[1:4]:",array[1:4])
print( " ")
print("array[2:]:",array[2:])
print( " ")
print("array[0:3:2]:",array[0:3:2])
print( " ")
print("array[ : :2]:",array[: : 2])
print( " ")
print("array[0:3:1]:",array[0:3:1])
print( " ")
print("array[ : :-1](Reverse):",array[: : -1])
print( " ")


print("Column")
print(array[:,1])#[2,,6,10,14]
print(array[: , -1]) # last column [4,8,12,16]
print(array[:,0:3]) # print first three column
print(array[:, 1::2])
print(array[:,::-1])

print(array[0:2,0:2])#[1,2,5,6]
print(array[2: , 2: ])#[11,12,15,16]
print(array[1:3,1:3])#[6,7,10,11]
