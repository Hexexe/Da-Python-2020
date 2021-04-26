#!/usr/bin/env python3

import pandas as pd
from sklearn.linear_model import LinearRegression

def mystery_data():
    a = pd.read_csv("src/mystery_data.tsv", sep="\t")
    return LinearRegression(fit_intercept=False).fit(a.iloc[:,0:5],a.iloc[:,-1]).coef_

def main():
    for i,j in enumerate(mystery_data()):
        print(f"Coefficient of X{i+1} is {j}")
    
if __name__ == "__main__":
    main()
