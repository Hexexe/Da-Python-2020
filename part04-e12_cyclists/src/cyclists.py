#!/usr/bin/env python3
import pandas as pd

def cyclists():
    return pd.read_csv("src/Helsingin_pyorailijamaarat.csv", sep=";").dropna(how="all").dropna(how="all", axis=1)

def main():
    print(cyclists())
    
if __name__ == "__main__":
    main()
