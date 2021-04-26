#!/usr/bin/env python3

from fractions import Fraction

class Rational(object):
    def __init__(self, a, b):
        self.c = Fraction(a, b)

    def __mul__(self, p):
        f = self.c * p.c
        return Rational(f.numerator, f.denominator)

    def __truediv__(self, p):
        f = self.c / p.c
        return Rational(f.numerator, f.denominator)

    def __add__(self, p):
        f = self.c + p.c
        return Rational(f.numerator, f.denominator)

    def __sub__(self, p):
        f = self.c - p.c
        return Rational(f.numerator, f.denominator)

    def __gt__(self, p):
        return self.c > p.c

    def __lt__(self, p):
        return self.c < p.c

    def __eq__(self, p):
        return self.c == p.c

    def __str__(self,):
        return f"{self.c}"


def main():
    r1 = Rational(1, 4)
    r2 = Rational(2, 3)
    print(r1)
    print(r2)
    print(r1*r2)
    print(r1/r2)
    print(r1+r2)
    print(r1-r2)
    print(Rational(1, 2) == Rational(2, 4))
    print(Rational(1, 2) > Rational(2, 4))
    print(Rational(1, 2) < Rational(2, 4))


if __name__ == "__main__":
    main()
