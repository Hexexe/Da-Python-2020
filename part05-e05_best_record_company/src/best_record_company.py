#!/usr/bin/env python3

import pandas as pd

def best_record_company():
    a = pd.read_csv("src/UK-top40-1964-1-2.tsv", sep="\t")
    return a[a.Publisher == a.groupby("Publisher")["WoC"].sum().idxmax()].sort_values("WoC",ascending=False)

def main():
    print(best_record_company())
    

if __name__ == "__main__":
    main()
