# Filling null values with the previous ones

# ------------------------------------------
'''
import pandas as pd

import numpy as np

# dictionary of lists

dict = {'First Score': [100, 90, np.nan, 95],

        'Second Score': [30, 45, 56, np.nan],

        'Third Score': [np.nan, 40, 80, 98]

        }

# creating a dataframe from dictionary

df = pd.DataFrame(dict)

# filling a missing value with previous ones

df2 = df.fillna(method='pad')

print(df)

print()

print(df2)


'''

# Filling null value with the next ones

# ------------------------------------------


import pandas as pd

import numpy as np

# dictionary of lists

dict = {'First Score': [100, 90, np.nan, 95],

        'Second Score': [30, 45, 56, np.nan],

        'Third Score': [np.nan, 40, 80, 98]

        }

# creating a dataframe from dictionary

df = pd.DataFrame(dict)

# filling  null value using fillna() function

df2 = df.fillna(method='bfill')

print(df)

print(df2)




