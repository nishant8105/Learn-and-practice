import matplotlib.pyplot as plt
import numpy as np
arr = np.arange(0 , 5, 0.2)
plt.plot(arr , arr**2 , "b--" , label = 'arr**2')
plt.plot(arr , arr**2.5 , "gs", label = 'arr**2.5')
plt.plot(arr , arr**3 , "r^", label = 'arr**3')
plt.legend()
plt.grid()
plt.show()