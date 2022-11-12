import matplotlib.pyplot as plt
import numpy as np
from numpy.lib import math


def sinTaylor(x, nmax):
    t = 0
    for n in range(nmax + 1):
        t1 = x ** (2 * n + 1) * ((-1) ** n) / (math.factorial(2 * n + 1))
        t = t + t1
    return t


if __name__ == "__main__":
    plt.xlabel("x")
    plt.ylabel("y")
    plt.ylim([-2, 2])

    x_list = np.linspace(-10, 10, 101)
    plt.scatter(x_list, np.sin(x_list))

    plt.plot(x_list, sinTaylor(x_list, 3), "blue")
    plt.plot(x_list, sinTaylor(x_list, 6), "red")
    plt.plot(x_list, sinTaylor(x_list, 9), "green")
    plt.plot(x_list, sinTaylor(x_list, 18), "black")

    fname = "sin_taylor_series.png"
    plt.savefig(fname)

    actual_value = np.sin(10.5)
    predicted_value = sinTaylor(10.5, 18)

    accuracy = predicted_value / actual_value

    print("Accuracy  = ", accuracy, "\n")
