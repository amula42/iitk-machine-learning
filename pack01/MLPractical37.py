# Working with Missing Data in Pandas DataSet to be used for AI/ML Projects

# ------------------------------------------------------------------------


# In Pandas missing data is represented by two value:


# 1) None: None is a Python singleton object that is often used for missing data in Python code.

# 2) NaN : NaN (an acronym for Not a Number), is a special floating-point value

#  recognized by all systems that use the standard IEEE floating-point representation


# Pandas treat None and NaN as essentially interchangeable

# for indicating missing or null values.

# To facilitate this convention, there are several useful

# functions for detecting,removing, and replacing

# null values in Pandas DataFrame :


# Handling Missing values in dataset

# 1) isnull()

# 2) notnull()

# 3) dropna()

# 4) fillna()

# 5) replace()

# 6) interpolate()

'''
# In order to check null values in Pandas DataFrame, we use isnull() function

# This function return dataframe of Boolean values which are True for NaN values.


import pandas as pd

import numpy as np

# dictionary of lists

dict = {'First Score': [100, 90, np.nan, 95],

        'Second Score': [30, 45, 56, np.nan],

        'Third Score': [np.nan, 40, 80, 98]

        }

# creating a dataframe from list

df = pd.DataFrame(dict)

print(df)

# using isnull() function

df2 = df.isnull()

print(df2)
'''
# 2)Checking for missing values using not null()


# In order to check null values in Pandas Dataframe, we use notnull() function

# This function return dataframe of Boolean values which are False for NaN values.


import pandas as pd

import numpy as np

# dictionary of lists

dict = {'First Score': [100, 90, np.nan, 95],

        'Second Score': [30, 45, 56, np.nan],

        'Third Score': [np.nan, 40, 80, 98]

        }

# creating a dataframe using dictionary

df = pd.DataFrame(dict)

# using notnull() function

bool_df2 = df.notnull()

print("\n\n", df)

print("\n\n", bool_df2)




