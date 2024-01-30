import warnings

warnings.filterwarnings(action="ignore")

import matplotlib.pyplot as plt

plt.figure(1)  # the first figure

plt.subplot(311)  # the first subplot in the first figure

plt.plot([1, 2, 3])

#     x = [0, 1, 2]

plt.subplot(312)  # the second subplot in the first figure

plt.plot([4, 5, 6])

#    x = [0, 1, 2]


plt.subplot(313)  # the third subplot in the first figure

plt.plot([7, 8, 9])

plt.figure(2)  # a second figure

plt.plot([11, 12, 13])  # creates a subplot(111) by default

plt.figure(1)  # figure 1 current; subplot(313) still current

plt.subplot(311)  # make subplot(311) in figure1 current

plt.title('Easy as 1, 2, 3')  # subplot 311 title

plt.figure(3)  # a second figure

# x = [1,2,3,4,5]

import numpy as np

x = np.arange(1, 6)  # x = [ 1, 2, 3,  4,  5 ]

y = x ** 2  # y = [ 1, 4, 9, 16, 25 ]

plt.plot(x, y, 'ro-')

plt.show()




