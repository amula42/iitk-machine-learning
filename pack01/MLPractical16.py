import numpy as np

a = np.arange(1, 6)  # [ 1, 2, 3, 4, 5]

print(np.sin(a))  # array([ 0., 0.84147098,  0.90929743,  0.14112001, -0.7568025 ])

print(np.log(a))  # array([ -inf,  0. ,  0.69314718,  1.09861229,  1.38629436])

print(np.exp(a))  # array([  1. ,   2.71828183,   7.3890561 ,  20.08553692,  54.59815003])

# Basic reductions

# -----------------


# Computing sums

print("\n-------------------\n")

import numpy as np

x = np.array([1, 2, 3, 4])

print("np.sum(x) : ", np.sum(x))  # 10  --> Lib univarsal funtion

print("x.sum()   : ", x.sum())  # 10  --> Member Function

print("\n-------------------\n")
import numpy as np

print("---Sum by rows and by columns:---")

x = np.array([[1, 2], [3, 4]])

print("x = \n", x)

print("x.sum() = ", x.sum())  # 10

# array(  [ [1, 2],

#          [3, 4]  ]   )

print("x.sum(axis=0) column wise sum = ", x.sum(axis=0))  # columns (first dimension)

# array([4, 6])

print(x[:, 0].sum(), x[:, 1].sum())

# 4, 6


print("x.sum(axis=1) row wise sum = ", x.sum(axis=1))  # rows (second dimension)

# #array([3, 7])

print(x[0, :].sum(), x[1, :].sum())  # 3, 7




