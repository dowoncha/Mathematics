import numpy as np
import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt

# We don't know a, b, c (Unknown coefficients)
# Should be exact for constant, linear, quadratic
# How to get coefs? => Taylor expansion
# Solve
def method_of_undetermined_coefficients():
    # u''(x_i) ~= a * u(x_(i+1)) + b * u(x_i) + c * u(x_(i-1))
    # u''(x_i) ~= a*u(x_i + h) + b*u(x_i) + c*u(x_i - h)
    # Do a taylor expand (h is a small number) at x_i = 0 for 4,5 terms
    # u''(x_i)-() = u(0)(a+b+c) + u'(0)(a-c)h + u''(0) * (((a+c)/2)h^2 - 1)
    # Exact for constant term a + b + c = 0 (u^(n) = 0)
    # Exact for linear term (a-c)h = 0
    # Exact for quadratic term ((a+c)/2)h^2 = 1
    return

# u1 = ui
# u0 = ui - 1
# u2 = ui + 1
# Approximates u''(x_i)
def finite_diff(u0, u1, u2):
    return


# x array of x values
# y array of f(x) values
# x.size == y.size
# returns  differentiated at a value or f'(x)
def differentiate(f, x, x0, scale):
    return

def discretize(f, a, b, n):
    x, h = np.linspace(a, b, n, retstep = True)

    y = f(x)

    return (x, y, h)

if __name__ == "__main__":
    a = 0.0
    b = 1.0

    def f(x):
        return x * x

    n = 20

    x, y, h = discretize(f, a, b, n)

    dy = np.zeros(y.shape, np.float)
    # i, j = i + 1
    # (y_j - y_i) / (x_j - x_i)
    dy[0:-1] = np.diff(y) / np.diff(x)
    # Last value doesn't have j to differentiate so we use j = i - 1
    dy[-1] = (y[-1] - y[-2]) / x[-1] - x[-2]

    print x, y, h

    plt.plot(x, y)

    # Solve u''(x)=f(x)
    # u(0)=u(1)=0
    #
