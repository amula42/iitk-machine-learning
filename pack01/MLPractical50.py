import numpy as np

import matplotlib.pyplot as plt

# Manual Implementation of Linear Regression

# ------------------------------------------

def estimate_coef(x, y):
    # number of observations/points/ training data

    n = np.size(x)

    # mean of x and y vector

    m_x = np.mean(x)

    m_y = np.mean(y)

    SS_xy = np.sum(x * y) - n * m_x * m_y

    SS_xx = np.sum(x * x) - n * m_x * m_x

    # Calculating regression coefficients

    m = SS_xy / SS_xx

    c = m_y - m * m_x  # c = y - mx

    return (m, c)  # Parameters of Hypothesis instance = model


def plot_regression_line(x, y, b):  # b[0] = c, b[1] = m

    # plotting the actual points as scatter plot

    plt.scatter(x, y, color="r", marker="o", s=30)

    y_pred = b[0] + b[1] * x  # y_pred = c + m * X

    #         c      m

    # res = 1 / ( 1 + math.exp( - y_pred ) )

    plt.scatter(x, y_pred, color="g", marker="o", s=60)

    plt.plot(x, y_pred, color="b")

    # putting labels

    plt.xlabel("-----------X------->")

    plt.ylabel("-----------Y------->")

    # function of show plot

    plt.show()


def startAIAlgorithm():
    x = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
    y = np.array([1, 3, 2, 5, 7, 8, 8, 9, 10, 12])

    # estimateing coefficients

    m, c = estimate_coef(x, y)  # Sender values

    print("Estimated coefficients:\n ")

    print("Slope m = ", m)

    print("y-Intercept c =", c)

    print("Model :   y  = ", m, " *  x  + ", c)

    plot_regression_line(x, y, [c, m])

    #                   0  1


if __name__ == "__main__":  # This is main function

    startAIAlgorithm()




# Drawback of this ML Algorithm

#    1) Historic Data & ML Logic in same code file.

#    2) All Calculations done mannually

#    3) Model not applied for future predictions
