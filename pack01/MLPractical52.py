# Import the important libraries and the dataset we are using to perform Polynomial Regression.

# Importing the libraries


import matplotlib.pyplot as plt

import pandas as pd

# Importing the dataset

data = pd.read_csv('LinearRegressionPoly_Data.csv')

print(data)

print(data.shape)  # (7,2)

X = data.iloc[:, 0:1].values  # [ rows , cols ]

y = data.iloc[:, 1].values  # [ rows , cols ]

print("X.shape = ", X.shape, "\n X=\n", X)

print("y.shape = ", y.shape, "\n y=", y)

# Import the important libraries and the dataset we are using to perform Polynomial Regression.

# Importing the libraries


import matplotlib.pyplot as plt

import pandas as pd

# Importing the dataset

data = pd.read_csv('LinearRegressionPoly_Data.csv')

print(data)

print(data.shape)  # (7,2)

X = data.iloc[:, 0:1].values  # [ rows , cols ]

y = data.iloc[:, 1].values  # [ rows , cols ]

print("X.shape = ", X.shape, "\n X=\n", X)

print("y.shape = ", y.shape, "\n y=", y)




