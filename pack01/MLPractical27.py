# Pie Charts

# ---------------------

import matplotlib.pyplot as plt

myLabels = ['S1', 'S2', 'S3']

sections = [60, 90, 50]  # 60 + 90 + 50 = 200

myColors = ['c', 'g', 'r']  # 30%  45%  25%

plt.pie(sections, labels=myLabels, colors=myColors,

        startangle=45,

        explode=(.1, 0, 0),

        autopct='%.2f%%')

plt.title('Pie Chart Example')

plt.show()




