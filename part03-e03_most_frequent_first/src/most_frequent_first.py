#!/usr/bin/env python3

import numpy as np


def most_frequent_first(a, c):
    d = {}
    [d.setdefault(i[0], []).append(i[1]) for i in zip(a[:, c], range(len(a)))]
    l = [i for i in sorted(d, key=lambda k: len(d[k]), reverse=True) for i in d.get(i)]
    return a[tuple([l])]


def main():
    a = np.random.randint(0, 10, (10, 10))
    print(most_frequent_first(a, 0))


if __name__ == "__main__":
    main()
