import numpy as np


def polynomialModel(x, a):
    t = 0
    for k in range(len(a)):
        t = t + a[k] * x**k
    return t


def errorFitGradient(f, coefficients, data):
    # f: the fit function
    # coefficients: ai that we try to optimise
    # data: The data we try to fit
    return -2 * np.array(
        [
            np.sum(
                np.array(
                    [
                        (data[1, i] - f(data[0, i], coefficients)) * data[0, i] ** k
                        for i in range(len(data[0]))
                    ]
                )
            )
            for k in range(len(coefficients))
        ]
    )


def errorFit(f, coefficients, data):
    # f: the fit function
    # coefficients: ai that we try to optimise
    # data: The data we try to fit

    error = 0
    for i in range(len(data[0])):
        error = error + (data[1, i] - f(data[0, i], coefficients)) ** 2
    return error
