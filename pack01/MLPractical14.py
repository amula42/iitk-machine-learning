import numpy as np

print("--Element wise Comparisons:--")

a = np.array([1, 2, 3, 4])

b = np.array([4, 2, 2, 4])

print("a == b : ", a == b)  # array([False,  True, False,  True], dtype=bool)

print("a > b :  ", a > b)  # array([False, False,  True, False], dtype=bool)

print("---Array - wise comparisons:---")

a = np.array([1, 2, 3, 4])

b = np.array([4, 2, 2, 4])

c = np.array([1, 2, 3, 4])

d = np.array([1, 2, 3, 5])

print("np.array_equal(a,b):", np.array_equal(a, b))  # False

print("np.array_equal(a,c):", np.array_equal(a, c))  # True

print("np.array_equal(a,d):", np.array_equal(a, d))  # False

print("-----Logical operations:----")

a = np.array([1, 1, 0, 0], dtype=bool)  # a=  [ True True  False False]

b = np.array([1, 0, 1, 0], dtype=bool)  # b= [ True False True  False]

print("a= ", a)

print("b= ", b)

print(np.logical_or(a, b))  # array([ True,  True,  True, False])

print(np.logical_and(a, b))  # array([ True, False, False, False])




