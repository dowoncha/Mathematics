# filename: pi_monte_carlo.py
# author: Dowon Cha
# Description:
#   Approximate the value of PI using monte carlo method
#   If a circle of radius R is inscribed in square of length 2R
#   area(circle) = PI*R^2
#   area(square) = 4R^2
#   area(circle)/area(square) = PI/4

import numpy as np
import matplotlib.pyplot as plt
import sys

def in_circle(x, y):
    # Returns boolean stating whether the point is inside circle of radius 1
    return x**2 + y**2 <= 1

def approx(n):
    # Approximate pi by sampling uniform distribution inside unit square
    # and calculating proportion of points inside circle

    points = np.random.uniform(-1.0, 1.0, size=(2,n))
    # Generate uniform points inside square of length 2
    count_in_circle = in_circle(points[0], points[1]).sum()
    # Approximate pi by checking how many points landed inside the circle
    return 4.0 * count_in_circle / n

if __name__ == "__main__":
    n = 1000
    x = np.arange(1, n)
    vecf = np.vectorize(approx)
    y = vecf(x)

    # Plot approximation to pi
    plt.subplot(2, 1, 1)
    plt.plot(x, y, 'b-')
    # plt.axhline(y=2.0,xmin=1,xmax=n, linewidth=1.0)
    plt.title('Approximation of PI')

    # Plot Error
    # As n -> Infinity, Err -> 0. approximation should converge to pi
    err = np.pi - y
    plt.subplot(2, 1, 2)
    plt.title('Error')
    plt.plot(x, err, 'r-')
    plt.show()
