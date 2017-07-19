__author__ = 'Алексей'
from math import sqrt


def solve(a, b, c):
    d = b**2 - 4*a*c
    if d < 0:
        print ("No solutions")
    elif d == 0:
        x = -b / (2*a)
        print ("one solution " + str(x))
    elif d > 0:
        x1 =(-b + sqrt(d)) / (2*a)
        x2 =(-b - sqrt(d)) / (2*a)
        print ("two solution " + str(x1) + " and " + str(x2))
    else:
        print("what are u input???!")

solve(1, 2, 1)
solve(1, 1, 1)
solve(1, 5, 6)