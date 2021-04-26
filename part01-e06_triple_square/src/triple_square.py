#!/usr/bin/env python3


def triple(a):
    return a*3


def square(a):
    return a*a


def main():
    for i in range(1, 11):
        a = square(i)
        b = triple(i)
        if a > b:
            break
        print(f"triple({i})=={b} square({i})=={a}")


if __name__ == "__main__":
    main()
