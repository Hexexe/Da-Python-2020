#!/usr/bin/env python3
import random


def merge(L1, L2):
    l3 = L1+L2
    for i in range(len(l3)):
        low = i
        for j in range(i + 1, len(l3)):
            if l3[j] < l3[low]:
                low = j
        l3[i], l3[low] = l3[low], l3[i]
    return l3


def main():
    l1 = random.sample(range(1, 100), 10)
    l2 = random.sample(range(1, 100), 10)
    print(l1, l2)
    print(merge(sorted(l1), sorted(l2)))


if __name__ == "__main__":
    main()
