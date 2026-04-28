import numpy as np

array = np.array([1, 2, 3, 4])
array = array * 2
print(array)

array2 = np.array('A')
print(array2.ndim)

array3 = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])
print(array3.ndim)

array4 = np.array([[1, 2, 3, 4],
                   [5, 6, 7, 8],
                   [9, 10, 11, 12],
                   [13, 14, 15, 16]])
print(array4[1:3:1])

array5 = np.array([1, 2])
print(array5 + 10)
print(array5 - 10)
print(array5 ** 10)

#Vectorized Math Functions
array6 = np.array([1, 2, 3, 4])
array7 = np.array([1.2, 2.5, 3.7, 4.9])
radii = np.array([1, 2, 3, 4])
print(np.sqrt(array6))
print(np.exp(array6))
print(np.round(array7))
print(np.log(array6))
print(np.pi)
print(np.pi * radii ** 2)

# Elemnetwise Operations
array8 = np.array([1, 2, 3, 4])
array9 = np.array([10, 20, 30, 40])

print(array8 + array9)
print(array8 * array9)
print(array8 / array9)

#Comparision Operators
array10 = np.array([1, 2, 3, 4])
print(array10 > 2)
print(array10 == 2)
print(array10 <= 2)
print(array10 != 2)

array11=array10.copy()
array11[array10 > 2] = 0
print(array11)

#Broadcasting allows NumPy to perform operations on arrays
#with different shapes by virtually expanding dimensions
#so they match the larger array's shape.

#the diemnsions have the same size.
#OR
#One of the dimensions has a size of 1.