from numpy import polynomial as P

if __name__ == "__main__":
    p = P.Polynomial([1, -1.0/2, -1.0/8, -3.0/24, -15.0/384, -165.0/3840])
    print p
    c = p.convert(kind=P.Chebyshev)
    print c
    print c.basis(3)
