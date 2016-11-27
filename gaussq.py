import decimal
from decimal import *
import numpy as np
from scipy import integrate
import matplotlib.pyplot as plt

def coefficients(kind, n, alpha, beta, b, a, muzero):
    return

def gaussq(kind, n, alpha, beta, kpts, endpts, b):
    # Computes the nodes t_j and weights w(j) for gaussian quadrature rules
    # with pre-assigned nodes. These are used when one wishes to approximate
    # Integral (from a to b) f(x)*w(x) dx
    # by Sum (from j = 1 to n) w(j)f(t_j)
    #
    # Input parameters
    # kind an integer between 1 and 6 giving hte type of quadrature rule (weight function)
    # 1. legendre quadrature
    # 2. chebyshev quadrature
    # 3. chebyshev qudrature
    return

def gauss_cheb(f, a, b, degrees):
    # For evaluating integrals of the form
    # Integrate (from -1 to 1) f(x)/sqrt(1-x^2) * dx
    # f the function to evaluate. Do not include the weight function
    # a lower bound
    # b upper bound
    # degrees

    # Nodes are chosen using x_i=cos((2i-1)/2n*PI)
    def nodes(i, n):
        return np.cos((2.0 * i - 1.0) / 2 * n * np.pi)

    # Get degree amount of nodes
    x = np.arange(degrees, dtype=np.dtype(decimal.Decimal))

    vfunc = np.vectorize(nodes)
    x = vfunc(x, n)

    # Weight function is w_i = pi / n
    w = np.pi / n

    approximation = np.sum(w * f(x))

    return approximation

def gauss(f, a, b, degrees):
    # Get nodes and weights of legendre polynomial quadrature
    [x, w] = np.polynomial.legendre.leggauss(degrees)

    if (a != -1.0 and b != 1.0):
        x = (np.pi / 2) * x + (np.pi / 2)

    result = np.sum(w*f(x))

    return result

def problem2_1():
    def f(x):
        return np.exp(x) * np.cos(x)

    degrees = 10

    result = gauss(f,0.0,np.pi,degrees)

    print result

    x = np.arange(Pi, step=degrees)

def problem2_2(degrees):
    def f(x):
        return np.exp(x * x)

    result = gauss_cheb(f, Decimal('-1'), Decimal('1'), degrees)

    print result
if 1:
    print "Current precision: ", getcontext().prec

    n = 40
    problem2_2(n)
