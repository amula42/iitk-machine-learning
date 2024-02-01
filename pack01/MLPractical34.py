# Use of  optimized pandas data access methods, .at, .iat, .loc, .iloc

import numpy as np

import pandas as pd

df = pd.DataFrame(np.random.randn(6, 4),

                  index=pd.date_range('20190101', periods=6, freq="D"),

                  columns=['A', 'B', 'C', 'D']

                  )

# Selecting a single column, which yields a Series, equivalent to df.A

print("\n\n df.A=    \n", df.A)

print("\n\n df['A']= \n", df['A'])

# print First three rows

print(df['2019-01-01':   '2019-01-03'])

# Selecting via [], which slices the rows.

print(df[0:3])  # print First three rows

#print( specific rows by using range of index values

print( df['20190102' : '20190104']   )
