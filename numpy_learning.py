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

# Broadcasting allows NumPy to perform operations on arrays
# with different shapes by virtually expanding dimensions
# so they match the larger array's shape.

# the diemnsions have the same size.
# OR
# One of the dimensions has a size of 1.

array12 = np.array([[1, 2, 3]])
array13 = np.array([[10], [20], [30]])
print(array12.shape)
print(array13.shape)
print(array12 * array13)

array14 = np.array([[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]])
array15 = np.array([[1], [2], [3], [4], [5], [6], [7], [8], [9], [10]])
print(array14.shape)
print(array15.shape)
print(array14 * array15) # Multiplication Table of 1 to 10

# Aggregate Functions = Summerize data and typically 
#                       Return a single value

array16 = np.array([[1, 2, 3, 4],
                   [5, 6, 7, 8]])
print(np.sum(array16))
print(np.mean(array16))
print(np.max(array16))
print(np.min(array16))
print(np.std(array16)) # standard deviation
print(np.var(array16)) # Variance
print(np.argmin(array16))
print(np.argmax(array16))
print(np.sum(array16, axis=0)) # sum of each column
print(np.sum(array16, axis=1)) # sum of each row

#Filtering (refers to the process of selecting specific elements from an array based on certain conditions or criteria.)
ages = np.array([[25, 30, 35, 40, 45, 18, 17, 14],
                [12, 34, 56, 78, 90, 5, 25, 30]])
teenagers = ages[ages < 18]
adults = ages[(ages >= 18) & (ages < 65)]
seniors = ages[ages >= 65]
evens = ages[ages % 2 == 0]
odds = ages[ages % 2 != 0]
print(teenagers)
print(adults)
print(seniors)
print(evens)
print(odds)

replacements = np.where(ages >= 18, ages, 0)
print(replacements)