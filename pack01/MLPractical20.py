'''
import matplotlib.pyplot as plt

x = [2, 3, 4, 5, 6, 7]

y = [4, 9, 16, 25, 36, 49]

plt.plot(x, y, marker='o', markerfacecolor='red', markersize=15,

         linestyle='dashed', color='blue')

plt.title("Number with Squared values", fontsize=14, color='red')

plt.xlabel('-----Numbers----->', fontsize=14, color='red')

plt.ylabel('-----Square------>', fontsize=14, color='blue')

plt.axis([1, 8, 2, 51])

plt.grid(True)

plt.annotate('Square of 5',

             fontsize=10, color='red',

             xytext=(3, 40), xy=(5, 25),

             arrowprops=dict(facecolor='blue', shrink=.1))

plt.show()

'''

import matplotlib.pyplot as plt

import numpy as np

# evenly sampled time at 200ms intervals

t = np.arange(0.0, 5.0, 0.2)  # t = 0.0, 0.2, 0.4, 0.6, 0.8, 1.0.........4.8

print(t)

# red stars , blue squares and green dots

plt.plot(t, t, 'r*-',

         t, t + 3, 'bs-',

         t, t + 6, 'r-',

         t, t + 6, 'go',

         markersize=7)

plt.show()

# t = x = 0.0, 0.2, 0.4, 0.6, 0.8, 1.0.........4.8

# t = y = 0.0, 0.2, 0.4, 0.6, 0.8, 1.0.........4.8
