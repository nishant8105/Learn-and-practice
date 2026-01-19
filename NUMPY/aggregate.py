import numpy as np

# aggregate function = summarize data typically return a single value
array = np.array([[1, 2, 3, 4, 5],[6, 7, 8, 9, 10]])

print(np.sum(array))#1+2+3+4+5+6+7+8+9+10=55
print(np.mean(array)) # average
print(np.std(array)) # standard deviation
print(np.var(array)) # variance
print(np.min(array)) #min value
print(np.max(array))# max value
print(np.argmin(array)) # min value index
print(np.argmax(array))# max value index

print(np.sum(array, axis=0)) # sum of column
print(np.sum(array, axis=1)) # sum of row
print(np.sum(array, axis=2)) # sum of row
