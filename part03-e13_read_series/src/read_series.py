#!/usr/bin/env python3

import pandas as pd
import numpy as np


def read_series():
    i, v = [], []
    while True:
        inp = input("Insert index and value separated by space:")
        if len(inp) == 0: break
        s = inp.split()
        if len(s) != 2: raise Exception("Invalid input format")
        i.append(s[0])
        v.append(s[1])
    return pd.Series(v, i)


def main():
    print(read_series())


if __name__ == "__main__":
    main()
