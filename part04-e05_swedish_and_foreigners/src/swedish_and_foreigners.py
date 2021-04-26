#!/usr/bin/env python3

import pandas as pd


def swedish_and_foreigners():
    a = pd.read_csv("src/municipal.tsv", sep="\t",index_col="Region 2018")["Akaa":"Äänekoski"]
    return a[(a.iloc[:, 2] > 5) & (a.iloc[:, 3] > 5)].iloc[:,[0,2,3]]


def main():
    print(swedish_and_foreigners())


if __name__ == "__main__":
    main()
