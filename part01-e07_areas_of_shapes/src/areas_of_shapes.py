#!/usr/bin/env python3

import math


def main():
    while True:
        inp = input("Choose a shape (triangle, rectangle, circle):")
        if inp == "triangle":
            b = float(input("Give base of the triangle: "))
            h = float(input("Give height of the triangle: "))
            print(f"The area is {0.5*b*h:.6f}")
        elif inp == "rectangle":
            w = float(input("Give width of the rectangle: "))
            h = float(input("Give height of the rectangle: "))
            print(f"The area is {w*h:.6f}")
        elif inp == "circle":
            r = float(input("Give radius of the circle:"))
            print(f"The area is {math.pi * r**2:.6f}")
        elif inp == "":
            break
        else:
            print("Unknown shape!")


if __name__ == "__main__":
    main()
