import matplotlib.pyplot as plt

plt.figure(1)
plt.subplot(121)
plt.grid()
plt.plot([1, 2, 3],[3, 2, 1])
plt.subplot(122)
plt.grid()
plt.plot([10, 29, 38], [2, 3, 4])

plt.figure(2)
plt.subplot(111)
plt.grid()
plt.plot([5, 11, 23, 43, 87],[9, 19, 33, 61,77])


plt.figure(3)
plt.subplot(121)
plt.grid()
plt.plot([2, 4, 6, 8],[50, 65, 75, 90])
plt.subplot(122)
plt.grid()
plt.plot([72, 78, 85, 90], [29, 30, 32, 35])


plt.show()