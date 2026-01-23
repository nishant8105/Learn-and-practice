import matplotlib.pyplot as plt
import numpy as np
def f(t):
    return np.exp(-t) * np.cos(2*np.pi*t)

t1 = np.arange(0.0, 5.0, 0.2)
t2 = np.arange(0.0, 5.0, 0.3)

plt.figure(1)

plt.subplot(211)
plt.plot(t1 , f(t1), 'b--' )


plt.subplot(212)
plt.plot(t2, np.cos(2*np.pi*t2), 'r--')
plt.grid()
plt.show()