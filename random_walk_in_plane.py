# filename: random_walk_in_plane.py
# author: Dowon Cha
# description:
#   With a point starting at the origin,
#   generate an angle that is uniformly distributed between [0,2pi)
#   And move the point by that angle with a distance of 1.
#   The Expected value of the square of the distance is n.
#   E(D^2) = n

import sys
import numpy as np
import matplotlib.pyplot as plt

# fig, ax = plt.subplots()

# Point in (x,y)
# point = (0.0, 0.0)

def walk(n):
    point = (0.0, 0.0)

    for i in range(n):
        angle = np.random.uniform(2 * np.pi)
        xi = point[0] + np.cos(angle)
        yi = point[1] + np.sin(angle)
        point = (xi, yi)

    return distance2(point)

def distance2(point):
    # Calculate the distance^2 of the point from the origin
    # d^2 = x^2 + y^2
    return point[0]**2 + point[1]**2

if __name__ == "__main__":
    n = int(sys.argv[1])
    trials = 1000

    result = 0.0
    for i in range(trials):
        result += walk(n)
    result /= trials

    print result

    # plt.plot(points, color='r', marking='o')
    # plt.title('Random Walk in Plane')
    # plt.axis([-n,n,-n,n])
    # plt.show()
