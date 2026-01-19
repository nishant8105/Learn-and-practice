import numpy as np

rng = np.random.default_rng()
print (rng.integers(1,7))
print(rng.integers(low=1, high=100, size=(2,5)))
print(np.random.uniform(low=-1, high=1, size=(3,2,1)))



array = np.array([1, 2, 3, 4, 5])
rng.shuffle(array)
print(array)
array = rng.choice(array, size=(2,3))
print(array)