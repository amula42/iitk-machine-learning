#   Boolean Indexing

# ============================

import pandas as pd

import numpy as np

df = pd.DataFrame(np.random.randn(6, 4),

                  index=pd.date_range('20190101', periods=6, freq="D"),

                  columns=['A', 'B', 'C', 'D']

                  )

print("\n\n df= \n", df)

print("\n\n df.A= \n", df.A)

print("\n\n df.A  > 0 = \n", df.A > 0)

print("\n df[ df.A > 0 ] = ")

print(df[df.A > 0])

#Task:

print("\n\n", df[ (df.B < 0)  &  (df.D < 0) ]   )

print("\n", df[df.B > df.B.mean()])

print("\n", df['B'][df.B > df.B.mean()])

print("\n\n")

# Selecting values from a DataFrame where a boolean condition is met.

print(df > 0)

print("\n\n")

print(df[df > 0])

# Using the isin() method for filtering:

df2 = df.copy()

df2['E'] = ['one', 'one', 'two', 'three', 'four', 'three']

print(df2)




#Performing a descriptive statistic

print( df.mean() )

print("\n\nMean of B : ", df.B.mean())

print("\n\nMean of B : ", df['B'].mean())




#Same operation on the other axis

print( df.mean(axis=1) )

print("\n\nAfter rows deletion \n ")

print(df2.drop(df2.index[2:4], axis=0))  # 0 -Row Deletion

print("\n\nAfter columns deletion \n ")

print(df2.drop(df2.columns[1:3], axis=1))  # 1 -Column Deletion

# print( "\n\nAfter deletion \n " )

print(df2)

print("df2.index = ", df2.index)

print("\n\ndf2.index[2:4] = ", df2.index[2:4])

# Following is invalid operation

# print( df2.drop(   df2.index[2:4] , axis=1 ) )

#writing to MS Excel

#Install (1)openpyxl  and (2)xlrd pluginnns

#Note: Installation not required if anaconda3 configured

#Writing to an excel file

df.to_excel('outputData.xlsx', sheet_name='Sheet1')









