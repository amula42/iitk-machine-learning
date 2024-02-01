import numpy as np

import pandas as pd

df2 = pd.DataFrame({'A': 1.0,

                    'B': pd.Timestamp("20190102"),

                    'C': pd.Series(7, index=list(range(5)), dtype='float64'),

                    'D': np.array([3] * 5, dtype='int64'),

                    'E': pd.Categorical(["male", "female", "female", "mobile", "male"],

                                        categories=["male", "female"]),

                    'F': 'foo'

                    }

                   )

print(df2)

print("df2.describe() \n", df2.describe())

print("df2.describe(include='all')= \n", df2.describe(include="all"))




