# filename: fsa.py
# author: Dowon Cha
#
# problem: Fourier Series Application (Theoretical and Programming Problem):
# Consider two sets A and B, each having n different integers in the range from 0 to 10n. We
# wish to compute the Cartesian sum of A and B, defined by C = {x + y : x in A, y in B}
# Note that the integers are in the range from 0 to 20n. We want to find the elements of C and
# the number of times each element of C is realized as a sum of elements in A and B. Show
# that the problem can be solved in O(n log n) time. Describe your algorithm, implement
# the algorithm using existing FFT packages. (Hint : Represent A and B as polynomials
# of degree 10n, and show how the original problem becomes a polynomial multiplication
# problem. Group work is encouraged for this problem.)

import numpy as np
from scipy.signal import fftconvolve
from scipy.fftpack import fft, ifft, rfft, irfft

# Function for "cartesian sum" of 2 sets
# Treat the problem as the multiplication of two polynomials f(x), g(x)
# Which is best achived using convolution (f * g)(x)
# @param a ndarray coefficient representation of f(x)
# @param b ndarray coefficient representation of g(x)
def convolution(a, b):
    # Point-value multiplication requires 2n-1 terms
    # Pad a and b with n zeros
    # a = np.append(a, np.zeros(a.size))
    # b = np.append(b, np.zeros(b.size))

    # next = np.power(2, np.ceil(np.log(a.size)/np.log(2)));
    # assert next & (next - 1) == 0

    a = np.append(a, np.zeros(a.size))
    b = np.append(b, np.zeros(b.size))
    print a

    # Check a and b are power of 2
    # assert a.size & (a.size - 1) == 0
    # assert b.size & (b.size - 1) == 0

    # Fast fourier transform
    # Change polynomial representation from coefficients to point-value
    # O(n log n)
    A = rfft(a)
    B = rfft(b)
    print "A", A

    np.fft.fftshift(A)
    np.fft.fftshift(B)

    print "A", A
    print "B", B

    C = A * B

    print "C", C

    # Convert back from point-value to coefficient representation
    c = irfft(C)

    return c

# Horners rule
# Evalues a value x for a polynomial A
# @param x value to evaluate
# @param A Coefficient representation of polynomial to evaluate x
def horners(x, *A):
    y = 0
    for a in np.nditer(A):
        print "Y", y
        y = y * x + a
    return y

if __name__ == "__main__":

    n = 4                                           # number of samples must be power of 2
    a = np.random.random_integers(10 * n, size=n)   # generate n integers between [0,10*n)
    b = np.random.random_integers(10 * n, size=n)

    x = 4                                           # test evaluation point

    print "a:", a
    print "b:", b
    print "(a*b)(x)", x, horners(x, a) * horners(x, b)

    c = convolution(a, b)
    c1 = np.polymul(a, b)
    # c = fftconvolve(a, b)

    print "c:", c, c1
    print "c(x)", horners(x, c)
