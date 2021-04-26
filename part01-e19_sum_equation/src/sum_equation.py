#!/usr/bin/env python3


def sum_equation(L):
    return f"{0 if len(L) == 0 else ' + '.join(map(str,L))} = {sum(L)}"


def main():
    print(sum_equation([1, 5, 7]))


if __name__ == "__main__":
    main()
