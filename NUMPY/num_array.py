import numpy as np

print (" 1D array")
a = np.array((1,2,3,4,5,6))
print(a)

print(a.ndim)
print(a.shape)
print(len(a))

print("2D array")
b =  np.array([[1,2,3],[4,5,6]])
print(a)
#a = np.array((1,2,3,4,5,6))
print(b)
print(b.ndim)
print(b.shape)
print(len(b))

print("3D array")
c = np.array([[[1,2,3,],[4,5,6,]],[[7,8,9],[10,11,12]]])
print(c)
print(c.ndim)
print(c.shape)
print(len(c))

print("function of array")
a = np.arange(10)  #array of number from 1 to 9 excluding last 10
print("arange function")
print(a)
a = np.arange(1,10,2)# start , end(exclude), step 
print(a)
a = np.linspace(0,1,6) # star , end , number of points
print("linspace")
print (a)
a = np.ones((3,3,))#create array of 3X3 of 1
print("ones matrix")
print(a)
a = np.zeros((2,3))#create array of 2X3 of 0
print("zeroes matrix")
print(a)
a = np.eye(3)# create a identity matrix of 1 at diagonal and 0 at else place
print("identity matrix")
print (a)
a = np.diag([1,2,3,4,5])# constuct a diagonal array
print("diagonal matrix")
print (a)
print(np.diag(a))
a = np.random.randn(4)
print("random array")
print(a)
# The `#23.30` at the end of the code snippet is a comment. In Python, any text following a `#` symbol
# on a line is considered a comment and is ignored by the Python interpreter when running the code.
# Comments are used to provide explanations or notes about the code for better understanding by humans
# reading the code. In this case, `#23.30` seems to be a placeholder or a note left by the author of
# the code.
#23.30
