#!/usr/bin/env python3

import numpy as np


def first_half_second_half(a):
    return a[np.sum(a[:, :np.shape(a)[1]//2], axis=1) > np.sum(a[:, np.shape(a)[1]//2:], axis=1)]


def main():
    for m in range(2, 10):
        a = np.random.randint(1,10,(m,2*m))
        print(f"{a}\n\n{first_half_second_half(a)}\n\n")


if __name__ == "__main__":
    main()
