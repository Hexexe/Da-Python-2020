#!/usr/bin/env python3
import pandas as pd

def growing_municipalities(df):
    return len(df[df.iloc[:,1]>0])/len(df)

def main():
    a = pd.read_csv("src/municipal.tsv", sep="\t",index_col="Region 2018")["Akaa":"Äänekoski"]
    print(f"Proportion of growing municipalities: {growing_municipalities(a) * 100:.1f}%")

if __name__ == "__main__":
    main()
