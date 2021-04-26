#!/usr/bin/env python3

import pandas as pd
from sklearn import linear_model

def coefficient_of_determination():
    a = pd.read_csv("src/mystery_data.tsv", sep="\t")
    r, x, y = linear_model.LinearRegression(), a.iloc[:,0:5], a.iloc[:,-1]
    s = [r.fit(a[i].values.reshape(-1, 1),y).score(a[i].values.reshape(-1, 1),y) for i in x]
    s.insert(0, r.fit(x, y).score(x, y))
    return s
    
def main():
    for i,j in enumerate(coefficient_of_determination()):
        print(f"R2-score with feature(s) X{i}: {j}") if i != 0 else print(f"R2-score with feature(s) X: {j}")
if __name__ == "__main__":
    main()