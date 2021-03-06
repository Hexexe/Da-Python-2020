#!/usr/bin/env python3

import pandas as pd

def inverse_series(s):
    return pd.Series(s.index,s.values)

def main():
    print(inverse_series(pd.Series([1,2,3], index = list("abc"))))

if __name__ == "__main__":
    main()
