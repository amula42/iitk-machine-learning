# Training Data Visualization

# ----------------------------


# Understanding the Training Data of ML With Visualization

# --------------------------------------------------------


#  A)- Univariate Plots for Data Visualization


#  B)- Multivariate Plots for Data Visualization


# A)- Univariate Plots

#   In this section we will look at three techniques

#   that you can use to understand each attribute of

#   your dataset independently.


#   1) Univariate Histogram Plot.

#   2) Univariate Density Plots.

#   3) Univariate Box and Whisker Plots.


# B)- Multivariate Plots

#   1)- Correlation Matrix Plot.

#   2)- Scatter Matrix Plot.


# 1)-Example of Univariate Histogram Plot

# ------------------------------------------------------

# A fast way to get an idea of the distribution

# of each attribute is to look at histograms.


# Histograms group data into bins and provide you

#  a count of the number of observations in each bin.


# From the shape of the bins you can quickly get a

# feeling for whether an attribute is Gaussian,

#  skewed or even has an exponential distribution.


# from matplotlib import pyplot as plt

'''
import matplotlib.pyplot as plt

import pandas

filename = 'indians-diabetes.data.csv'

hnames = ['preg', 'plas', 'pres',

          'skin', 'test', 'mass',

          'pedi', 'age', 'class']

df = pandas.read_csv(filename, names=hnames)

print(df)

df.hist()

plt.tight_layout()

plt.show()

# A.2)-Example of Univariate Density Plots

# ------------------------------------------------------

# Density plots are another way of getting a quick idea

# of the distribution of each attribute.


# This plots look like an abstracted histogram with a smooth

# curve drawn through the top of each bin, much like your eye

#  tried to do with the histograms.


import pandas

import matplotlib.pyplot as plt

filename = 'indians-diabetes.data.csv'

hnames = ['preg', 'plas', 'pres',

          'skin', 'test', 'mass', 'pedi', 'age', 'class']

dataframe = pandas.read_csv(filename, names=hnames)

dataframe.plot(kind='density', subplots=True, layout=(3, 3), sharex=False)

plt.tight_layout()

plt.show()



# 3)-Example of Univariate Box and Whisker Plots

# -------------------------------------------------------------------------------------------


# Another useful way to review the distribution of each attribute

# is to use Box and Whisker Plots or boxplots for short.


# Boxplots summarize the distribution of each attribute,

# drawing a line for the median (middle value) and a box around the

# 25th and 75th percentiles (the middle 50% of the data).


# The whiskers give an idea of the spread of the data and dots outside

# of the whiskers show candidate outlier values

# (values that are 1.5 times greater than the size of spread

#  of the middle 50% of the data).

# ---------------------------------------------------------------------------------------------


# import matplotlib.pyplot as plt


from matplotlib import pyplot as plt

import pandas

filename = "indians-diabetes.data.csv"

hnames = ['preg', 'plas', 'pres',

          'skin', 'test', 'mass', 'pedi', 'age', 'class']

dataframe = pandas.read_csv(filename, names=hnames)

dataframe.plot(kind='box', subplots=True,

               layout=(3, 3),

               sharex=False,

               sharey=False)

plt.show()




# 1)- Correlation Matrix Plot.

# -------------------------------------------


# Correlation gives an indication of how related

# the changes are between two variables.


# If two variables change in the same direction they are

# positively correlated.


# If they change in opposite directions together

# (one goes up, one goes down), then they

# are negatively correlated.


# You can calculate the correlation between each

# pair of attributes.This is called a correlation matrix.


# You can then plot the correlation matrix and

# get an idea of which variables have a

# high correlation with each other.


import warnings

warnings.filterwarnings(action="ignore")

# Correlations Matrix Plot

import matplotlib.pyplot as plt

import pandas as pd

import numpy

pd.set_option('display.width', 1000)

pd.set_option('display.max_column', None)

hnames = ['preg', 'plas', 'pres', 'skin',

          'test', 'mass', 'pedi', 'age', 'class']

dataframe = pd.read_csv('indians-diabetes.data.csv', names=hnames)

correlations = dataframe.corr()

print(correlations)

# plot correlation matrix

fig = plt.figure()

# Following will add matrix and side bar in entire area

subFig = fig.add_subplot(111)

cax = subFig.matshow(correlations, vmin=-1, vmax=1)

fig.colorbar(cax)

# -----------------------------

ticks = numpy.arange(0, 9)  # It will generate values from 0,1,2,3,4,5,6,7,8

subFig.set_xticks(ticks)

subFig.set_yticks(ticks)

subFig.set_xticklabels(hnames)

subFig.set_yticklabels(hnames)

# -----------------------------

plt.show()

'''

# 2)-Scatter Matrix Plot


# A scatter plot shows the relationship between two variables

# as dots in two dimensions, one axis for each attribute.


# You can create a scatter plot for each pair of attributes

#  in your data.


# Drawing all these scatter plots together is called a scatter

#  plot matrix.


# Scatter plots are useful for spotting structured relationships

#  between variables, like whether you could summarize the

#  relationship between two variables with a line.


# Scatter Matrix Plot for Multivariate Data

# ------------------------------------------

import warnings

warnings.filterwarnings(action="ignore")

import matplotlib.pyplot as plt

import pandas as pd

from pandas.plotting import scatter_matrix

hNames = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']

dataframe = pd.read_csv("indians-diabetes.data.csv", names=hNames)

scatter_matrix(dataframe)

plt.show()







