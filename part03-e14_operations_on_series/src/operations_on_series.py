#!/usr/bin/env python3

import pandas as pd
import numpy as np


def create_series(L1, L2):
    return (pd.Series(L1, index=list("abc")), pd.Series(L2, index=list("abc")))


def modify_series(s1, s2):
    s1["d"] = s2.pop("b")
    return (s1, s2)


def main():
    s1, s2 = create_series([1, 2, 3], [4, 5, 6])
    print(modify_series(s1, s2))
    print(s1+s2)


if __name__ == "__main__":
    main()
