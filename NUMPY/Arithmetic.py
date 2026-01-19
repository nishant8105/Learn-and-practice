import numpy as np
# Arithmetic Operaion

array = np.array([1,2,3,4])
print("Scaler Arithmetic")
print("Addition",array + 1)
print("Subtract",array - 2)
print("Multiplaction",array * 3)
print("Division",array/4)
print("Exponention",array ** 2)

array = np.array([1,2,3,4])
print("Vector Arithmetic")
print("Squre root:",np.sqrt(array))
array = np.array([1.32 ,2.56, 3.9, 4.09])
print("Round off: " , np.round(array))
print(np.pi)


# ### Exercise
# assume array radii have radius of circle find area of circle /n
# radii = np.array([1,2,3,4])

radii = np.array([1,2,3,4])
area = np.pi * radii ** 2
print(area)

# ### Element wise arithemetic

array1 = np.array([1, 2, 3, 4])
array2 = np.array([5, 6, 7, 8])
print(array1 + array2)
print(array1 - array2)
print(array1 * array2)
print(array1 / array2)
# print(array1 % array2)
print(array1 ** array2)



# ### Comparision Operator

score = np.array([91, 65, 32, 81, 55, 54, 25, 56, 100 ])
print(score == 100)
print(score >= 60)
print(score <= 60)
