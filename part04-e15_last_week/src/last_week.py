#!/usr/bin/env python3

import pandas as pd
import numpy as np


def last_week():
    a = pd.read_csv("src/UK-top40-1964-1-2.tsv", sep="\t", converters={"LW": lambda x: np.int64(x) if x not in ["New", "Re"] else np.nan})
    b = a[~a["LW"].isna()]
    b.sort_values(by=["LW"], inplace=True)
    b["WoC"] -= 1
    b["Peak Pos"].where((b["Peak Pos"] != b["Pos"]) | (b["Peak Pos"] == b["LW"]), np.nan, inplace=True)
    b.index = b["LW"].rename()
    b = b.reindex(range(1, a.shape[0]+1))
    b["Pos"], b["LW"] = b.index, np.nan
    return b


def main():
    df = last_week()
    print("Shape: {}, {}".format(*df.shape))
    print("dtypes:", df.dtypes)
    print(df)


if __name__ == "__main__":
    main()
