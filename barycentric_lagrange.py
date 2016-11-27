# filename: barycentric_lagrange.py
# author: Dowon Cha
# summary:
#   Interpolation problem of given (x,y) points fit a polynomial
#   Improve upon lagrange interpoltaion by using
#   barycentric representation of coordinates

# Why Lagrange is only theoretical
# 1. Each evaluation of p(x) requires O(n^2) add and mult
# 2. Adding a new data pair requires a new computation from scratch
# 3. Computation is numerically unstable

# Using Barycentric coordinates allows lagrange to be run in O(n) like Newton's Divided-differences

import numpy as np
import matplotlib.pyplot as plt

def interpolate(x, y, w):
    # Given array of x, y and weights
    # Interplate the function using barycentric lagrange
    # Assumptions: x are chebyshev roots
    # Number of barycentric interpolant points
    xx = np.linspace(-1, 1, 5000)
    numer = np.zeros(len(xx))
    denom = np.zeros(len(xx))

    # Weight function using chebyshev's
    # Uncomment to use: paper's delta as [.5, 1, ..., 1, .5]
    # w = np.ones(len(x) + 1)
    # w[0] = c[-1] = .5
    # for i in range(len(w)):
    #     if (w[i] % 2 == 1):
    #         w[i] *= -1

    for j in range(n):
        xdiff = xx - x[j]
        temp = c[j] / xdiff
        numer = numer + temp * y[j]
        denom = denom + temp

    ff = numer / denom

    return (xx, ff)

if __name__ == "__main__":
    n = 1000

    # Function we will be interpolation for
    def fi(x):
        return np.abs(x) + x / 2.0 - x**2

    f = np.vectorize(fi)

    # Compute sample points and weight function using chebyshev gaussian
    (x, w) = np.polynomial.chebyshev.chebgauss(n)
    # Compute y_i values
    y = f(x)

    (xx, yy) = interpolate(x, y, w)

    plt.title('Barycentric Lagrange Interpolation')

    plt.subplot(3, 1, 1)
    plt.plot(x, y, 'bo-')
    plt.subplot(3, 1, 2)
    plt.plot(xx, yy, 'r-')

    # Error plot
    plt.subplot(3, 1, 3)
    plt.plot(x, )

    plt.show()
