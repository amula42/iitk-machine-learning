# 1)-See the top & bottom rows of the frame

import numpy as np

import pandas as pd

df = pd.DataFrame(np.random.randn(6, 4),

                  index=pd.date_range('20190101', periods=6, freq="D"),

                  columns=['A', 'B', 'C', 'D']

                  )

print("\n\npandas df.head() = \n")

print(df.head())

print(df.head(3))

print("\n\ndf.tail() = \n", df.tail())

print("\n\ndf.tail(3) = \n", df.tail(3))

print("\n\ndf.sample() = \n", df.sample())

print("\n\ndf.sample(3) = \n", df.sample(3))

print( "\n\n df.T = \n", df.T  )

print("\n\noriginal values : \n ", df)

print("\n\nSorted values   : \n ")

print(df.sort_values(by='B', ascending=True))

print("original values : \n ", df)

del df["C"]

print( df )





