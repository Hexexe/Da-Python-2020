#!/usr/bin/env python3

import pandas as pd


def split_date(df):
    a = df.Päivämäärä.str.split(" ",expand=True)
    a.columns = ["Weekday","Day", "Month", "Year","Hour"]
    a.Hour = a.Hour.str[:2]
    d = {"ma":"Mon","ti":"Tue","ke":"Wed","to":"Thu","pe":"Fri","la":"Sat","su":"Sun"} 
    m = {"tammi":1,"helmi":2,"maalis":3,"huhti":4,"touko":5,"kesä":6,"heinä":7,"elo":8,"syys":9,"loka":10,"marras":11,"joulu":12}
    a.Weekday = a.Weekday.map(d)
    a.Month = a.Month.map(m)
    return a.astype({"Weekday":object,"Day":int,"Month":int,"Year":int,"Hour":int})

def split_date_continues():
    a = pd.read_csv("src/Helsingin_pyorailijamaarat.csv", sep=";").dropna(how="all").dropna(how="all", axis=1)
    b = split_date(a)
    a.drop("Päivämäärä", axis=1, inplace=True)
    return pd.concat([b, a], axis=1)

def main():
    df = split_date_continues()
    print("Shape:", df.shape)
    print("Column names:\n", df.columns)
    print(df.head())


if __name__ == "__main__":
    main()
