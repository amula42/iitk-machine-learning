# NOTE: seed value makes the random numbers predictable & regenratable

# NOTE:  virtual random numbers are predictable.

import numpy as np

res1 = np.random.rand(4)

print("\n res1 = ", res1)

# seed value makes the random numbers predictable

np.random.seed(1)

res2 = np.random.rand(4)

print("\n res2 = ", res2)

np.random.seed(0)

res3 = np.random.rand(4)

print("\n res3 ", res3)

np.random.seed(1)

res4 = np.random.rand(4)

print("\n res4 = ", res4)

res5 = np.random.randint(50, 90, size=4)

print("\n res5 = ", res5)







