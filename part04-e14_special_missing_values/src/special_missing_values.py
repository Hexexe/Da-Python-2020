#!/usr/bin/env python3

import pandas as pd
import numpy as np

def special_missing_values():
    a = pd.read_csv("src/UK-top40-1964-1-2.tsv", sep="\t", converters = { "LW": lambda x: np.int64(x) if x not in ["New", "Re"] else None })
    return a[a["Pos"] > a["LW"]]

def main():
    print(special_missing_values())

if __name__ == "__main__":
    main()
