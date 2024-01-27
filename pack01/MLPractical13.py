#Example-08

import numpy as np

arr = np.array( [11, 22, -33,  0,  44, 55] )

#                0    1   2    3    4   5

print( "arr.sum() = " , arr.sum()  )  #This is member function

print( np.sum(arr) )      #This is univarasal function

print( "arr.std() = " , arr.std()  )

print( "arr.mean()   = ", arr.mean() )

print( "np.mean(arr) = ", np.mean(arr) )

print( "arr.max() = " , arr.max()  )

print( "arr.min() = " , arr.min()  )

print( "arr.size = "  , arr.size   )

print( "arr.shape ="  , arr.shape  )

print( "arr.dtype= "  , arr.dtype  )

# following line will print( index of nonzero values )

print( "arr.nonzero() = ", arr.nonzero() )

print("\n-------------------\n")

# Example-09

import numpy as np

# Are all elements  nonzero

print(np.all([1, 2, 3, -4]))  # True

print(np.all([1, 2, 3, -4, 0]))  # False

# Is any elements non-zero

print(np.any([1, 2, 3, 4]))  # True

print(np.any([1, 2, 3, 4, 0]))  # True

print(np.any([0, 0, 0, 0., 0]))  # False

print(np.any([0, 0, 0, 0., 0, -1]))  # True

print("\n-------------------\n")
# Example-10


# Types of Operation Broadcasting:-

# 1) Scaler Operation Broadcasting

# 2) Array Operation Broadcasting

import numpy as np

n1 = np.array([4, 5, 6])

n2 = np.array([1, 2, 3])

print("n1   =   ", n1)  # [4,5,6]

#   +

print("n2   =   ", n2)  # [1,2,3]

print("n1 + n2 = ", n1 + n2)

print("n1 - n2 = ", n1 - n2)

n3 = np.array([4, 5, 6, 7])

# print(n1 + n3)

# NOTE:

# Shape must be the same for array operation broadcasting


print("\n-------------------\n")

# Example-11

import numpy as np

n4 = np.array([10, -1, 0, 90, 300, 3, -6, 2])

print("Before : n4 =", n4)

n5 = sorted(n4, reverse=True)  # 1) External Sorting

print("n5 =", n5)

print("After : n4 =", n4)

n4.sort()  # 2) Internal Sorting or In-place sorting

print("After n4.sort() = ", n4)

print("After n4.sort() = ", list(reversed(n4)))

print("After n4.sort() = ", tuple(reversed(n4)))

import numpy as np

n4 = np.array([777, 555, 222, 111, 999, 666])

#              0     1    2    3    4    5


print("n4   =      :", n4)

print("n4.argsort():", n4.argsort())  # Sorted list of positions

# [3,2,1,5,0,4]


indxArr = n4.argsort()  # [3,2,1,5,0,4]

print("Min=", n4[indxArr[0]])

print("Max=", n4[indxArr[len(indxArr) - 1]])

print("Sorted array=", n4[indxArr[:]])

# Trick-1: To print the array in sorted order

for i in n4.argsort():  # [3,2,1,5,0,4]

    print(n4[i], end=" ")

# Trick-2: To print the array in sorted order

print(n4[n4.argsort()])  # Original values in n4 will not change

print("n4 = ", n4)

print("\n-------------------\n")

# Example-12

import numpy as np

na = np.array([[1, 2, 3],

               [4, 5, 6]])

print("na = \n", na)

print("na.transpose() = \n", na.transpose())

print("na = \n", na)

print("np.eye = \n", np.eye(6))  # To create square matrix

