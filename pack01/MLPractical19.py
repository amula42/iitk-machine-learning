'''
import matplotlib.pyplot as plt

plt.plot([1, 2, 3, 4, 5], [1, 2, 3, 4, 5], 'bo-', label='line 1', linewidth=2)

plt.plot([1, 2, 3, 4, 5], [1, 4, 9, 16, 25], 'rs--', label='line 2', linewidth=4)

plt.axis([0, 6, 0, 26])

plt.legend(loc="upper right")

plt.show()
'''

import matplotlib.pyplot as plt

# If you make multiple lines with one plot command,

# the kwargs apply to all those lines, e.g.:

x1 = [1, 2, 3]

y1 = [1, 2, 3]

x2 = [1, 2, 3]

y2 = [1, 4, 9]

plt.plot(x1, y1, 'ro-', x2, y2, 'bs--', linewidth=7)

plt.axis([0, 4, 0, 10])

plt.title("Report genereted by IIT Kanpur")

plt.show()




