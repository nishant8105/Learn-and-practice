import numpy as np

#Filtering = Refers to the process of selecting elements fron an array that match a given condition
ages = np.array(
    [[21, 17, 19, 20 , 16, 30, 18, 65],
    [39, 22, 15, 99, 18, 19, 20, 21]])

teenagers = ages[ages < 18 ]
print(teenagers)
adult = ages[ (ages > 18) & (ages < 65)]
print(adult)
seniors = ages[ages >= 65]
print(seniors)
even = ages [(ages & 1 == 0)]
print(even)

adult = np.where(ages >= 18, ages, np.nan)