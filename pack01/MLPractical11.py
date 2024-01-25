d1 = [[1, 2],

      [3, 4],

      [5, 6],

      [7, 8],

      [9, 10],

      [11, 12],

      [13, 14]

      ]

print("d1 = ", d1)

print("\n-------------------\n")

import numpy as np

d2 = np.array([[1, 2],

               [3, 4],

               [5, 6],

               [7, 8],

               [9, 10],

               [11, 12],

               [13, 14]])

print("d2 = \n", d2)

print("d2.shape = ", d2.shape)  # (7,2)

print("d2.size  = ", d2.size)  # 14

print("d2.ndim  = ", d2.ndim)  # 2

# Entire expressione before "," is for rows

print("d2[: :2 , 0] = ", d2[::2, 0])  # [ 1  5  9 13]    [ row, col]

print("d2[ 1: : 2 , 1 ] = ", d2[1:: 2, 1])

print("d2[: :2 ] = \n", d2[::2])  # [ row, col]

# [  [1,2],  [5,6],  [9,10],  [13,14]  ]  All alternate rows




