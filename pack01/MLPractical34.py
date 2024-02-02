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

#Selection by Label

#For getting a cross section using a label

print("\n\n", df.loc['2019-01-06']   )


dates = pd.date_range('20190101', periods=6, freq="D")

print( "\n\n",  df.loc[ dates[0] ]    )

#Selecting on a multi-axis by label

print( df.loc[ :  ,  ['A','D'] ] )


#Selecting on a multi-axis by label

print( df.loc['20190102' : '20190104' , ['A','D']] )




#Reduction in the dimensions of the returned object

print( df.loc['20190102' ,  ['A','D'] ] )

# For getting a scalar value

dates = pd.date_range('20190101', periods=6, freq="D")

print(df.loc[dates[0], 'A'])

# For getting fast access to a scalar

#  (equiv to the prior method)

print(df.at[dates[0], 'A'])




#Select via the row index position of the passed integers

print( df.iloc[ 3 ]  )




#For getting fast access to a scalar

# (equiv to the prior method)

print( df.iat[1,1]  )

#Note: iat is faster than iloc




