import matplotlib.pyplot as plt
import numpy as np


def derivitive(f, x, h):
    # f: Function
    # x: Argument
    # h: stepsize

    return (f(x + h) - f(x)) / h


def nDerivative(f, x, h, n):
    # f: Function
    # x: Argument
    # h: stepsize
    # n: order of derivitive

    t = 0
    for k in range(n + 1):
        t = t + (-1) ** (k + n) * np.lib.math.factorial(n) / (
            np.lib.math.factorial(k) * np.lib.math.factorial(n - k)
        ) * f(x + k * h)

    return t / h**n


def func(x):
    return 2 * np.sin(x) ** 2 + x


def taylor(f, x, x0, nmax, h):
    t = 0
    for n in range(nmax + 1):
        t = t + nDerivative(f, x0, h, n) * (x - x0) ** n / np.lib.math.factorial(n)
    return t


if __name__ == "__main__":
    nmax = 15
    h = 0.05

    plt.ylim([-5, 8])

    x_list = np.linspace(-5, 5, 101)
    plt.scatter(x_list, func(x_list))

    plt.plot(x_list, taylor(func, x_list, 0, nmax, h), "blue")
    plt.plot(x_list, taylor(func, x_list, 2, nmax, h), "red")
    plt.plot(x_list, taylor(func, x_list, -3, nmax, h), "green")

    fname = "./plots/general_taylor"

    plt.savefig(fname)
