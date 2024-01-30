import numpy as np

import matplotlib.pyplot as plt

# Plotting with default settings

X = np.linspace(-np.pi, np.pi, 255, endpoint=True)

print("X= ", X)

S = np.sin(X)  # sin0 = 0  and sin90=1

C = np.cos(X)  # cos0 = 1  and cos90 = 0

plt.plot(X, S, label='sin curve')

plt.plot(X, C, label='cos curve')

plt.grid(True)

plt.legend(loc="upper left")

plt.show()




