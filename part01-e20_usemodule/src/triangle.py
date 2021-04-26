#!/usr/bin/env python
"""Module for calculating different things about triangles"""

__author__ = "Hexexe"
__version__ = "0.01 Pre-alpha early access"

from math import sqrt

def hypothenuse(a, b):
    """Calculates the hypothenuse when given the lengths of two other sides of a right-angled triangle as arguments."""
    return sqrt(a*a + b*b)

def area(a, b):
    """Calculates the area of the right-angled triangle, when two sides, perpendicular to each other, are given as parameters."""
    return 0.5 * a * b
