#!/usr/bin/env python3

import math


def solve_quadratic(a, b, c):
    d = (b**2) - (4*a*c)
    r1 = (-b - math.sqrt(d)) / (2 * a)
    r2 = (-b + math.sqrt(d)) / (2 * a)
    return (r1, r2)


def main():
    print(solve_quadratic(1, 2, 1))


if __name__ == "__main__":
    main()
