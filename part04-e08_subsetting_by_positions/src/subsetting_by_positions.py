#!/usr/bin/env python3
import pandas as pd

def subsetting_by_positions():
    a = pd.read_csv("src/UK-top40-1964-1-2.tsv", sep="\t",index_col="Pos")
    return a.iloc[:10,[1,2]]

def main():
    print(subsetting_by_positions())

if __name__ == "__main__":
    main()