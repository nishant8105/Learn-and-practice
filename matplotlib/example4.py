import matplotlib.pyplot as plt

x1 = [1, 2, 3, 4, 5, 6]
y1 = [1, 4, 9, 16, 25, 36]
y2 = [1, 4, 6, 8, 10, 12]

lines = plt.plot(x1, y1, x1, y2)

plt.setp(lines[0], color='r', linewidth=1.0 , label='square')
plt.setp(lines[1], color='g', linewidth=2.0, label='double')
plt.legend()
plt.grid()
plt.show()