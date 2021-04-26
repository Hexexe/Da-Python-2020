#!/usr/bin/env python3

import pandas as pd

def suicide_fractions():
    a = pd.read_csv("src/who_suicide_statistics.csv")
    a["kys"] = a['suicides_no']/a["population"]
    return a.groupby("country")["kys"].mean()

def main():
    print(suicide_fractions())

if __name__ == "__main__":
    main()
