import numpy as np

d2=np.array(
    [[1, 2, 3, 4],
    [5, 6, 7, 8]]
)
print("shape of d2",d2.shape)#(2,4)2 = rows; 4 = column
print("Dimension of d2",d2.ndim)#2
print("Length of d2",len(d2))
a = np.arange(10)
print(a)
a = np.arange(1, 10, 2)
print(a)
a = np.linspace(0, 1, 6)
print(a)
a = np.ones((3,2))
print(a)
b = np.zeros((3,2))
print(b)
b = np.eye(4,4)
print(b)
b = np.diag([1, 2, 3, 4, 5])
print(b)
print(np.diag(b))
a = np.random.rand(4)
print(a)
a = np.random.randn(4)
print(a)
print(a.dtype)
a = np.arange(10)
print(a.dtype)
a = np.arange(10, dtype="float64")
print(a)
comples = np.array([1+2j, 2+4j])
print(comples.dtype) 
print(comples) 
a = a[1:8:2]
print("slice",a)