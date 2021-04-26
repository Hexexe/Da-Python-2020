#!/usr/bin/env python3

import pandas as pd
import numpy as np


def cleaning_data():
    a = pd.read_csv("src/presidents.tsv", sep="\t")
    a = a.where(a != "two", 2)
    a = a.where(a != "-", np.nan)
    a["President"] = a["President"].str.split(",").apply(lambda x: " ".join(x[::-1])).str.strip()
    a["Vice-president"] = a["Vice-president"].str.split(",").apply(lambda x: " ".join(x[::-1])).str.title().str.strip()
    a["Start"] = a["Start"].str.split(" ",expand=True)[0]
    a = a.astype({"President":object,"Start":int,"Last":float,"Seasons":int,"Vice-president":object})
    return a

def main():
    print(cleaning_data())

if __name__ == "__main__":
    main()
