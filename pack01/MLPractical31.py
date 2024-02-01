import pandas as pd

import numpy as np

print("numpy matrix = \n\n", np.random.randn(6, 4))

df = pd.DataFrame(np.random.randn(6, 4),

                  index=pd.date_range('20190101', periods=6, freq="D"),

                  columns=['A', 'B', 'C', 'D']

                  )

print("\n\npandas dataframe = \n", df)

df['E'] = df['A'].apply(lambda y: 1 if (y > 0) else 0)

print(df)

print("\n\n")

print(df.groupby('E').size())

print("\n\nHeadings in Dataframe : ", df.columns)  # [A, B, C, D, E]

#  0, 1, 2, 3, 4

print("\n\nRow Headings in Dataframe : ", df.index)

print("\n\nValues in Dataframe : \n", df.values)

print("\n", df.columns[2:5])  # [C, D, E]







