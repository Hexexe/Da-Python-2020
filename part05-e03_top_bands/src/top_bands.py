#!/usr/bin/env python3

import pandas as pd

def top_bands():
    a = pd.read_csv("src/bands.tsv", sep="\t")
    b = pd.read_csv("src/UK-top40-1964-1-2.tsv", sep="\t")
    a["Band"] = a["Band"].str.upper()
    return pd.merge(b, a, left_on=["Artist"], right_on=["Band"])

def main():
    print(top_bands())

if __name__ == "__main__":
    main()
