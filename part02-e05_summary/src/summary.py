#!/usr/bin/env python3

import sys
import numpy as np

def summary(filename):
    with open(filename) as f:
        l = []
        for i in f:
            try:
                l.append(float(i))
            except ValueError:
                pass
    return (np.sum(l), np.average(l), np.std(l, ddof=1))

def main():
    for i in sys.argv[1:]:
        j = summary(i)
        print(f"File: {i} Sum: {j[0]:.6f} Average: {j[1]:.6f} Stddev: {j[2]:.6f}")
   
if __name__ == "__main__":
    main()
