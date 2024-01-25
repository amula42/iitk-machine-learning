import numpy as np

zr = np.zeros([3, 4])

print("Zero filed array zr = \n", zr)

ar = np.ones([4, 4], dtype=int)  # By default is float

print("1's filed array ones = \n", ar)

print(ar * 4)

print(ar.dtype)

zr2 = np.zeros([2, 5])

print("Zero filed array zr2 = \n", zr2)

zr = np.zeros([2, 3, 4])

print("Zero filed array zr = \n", zr)

print("Total no of values = ", zr.size)

print("zr.shape = ", zr.shape)

print("zr.ndim   = ", zr.ndim)

print("\n-------------------\n")
import numpy as np

# We can create numpy array from range

ar = np.arange(11, 16)  # Rule of II & EE

print("ar = ", ar)

# ar = [11, 12, 13, 14, 15]

#      0   1    2   3   4

ar[3] = 77

print("After updating, ar = ", ar)

# [11, 12, 13, 77, 15]




