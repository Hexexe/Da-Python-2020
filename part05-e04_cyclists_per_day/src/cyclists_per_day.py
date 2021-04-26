#!/usr/bin/env python3

import pandas as pd
import matplotlib.pyplot as plt


def split_date():
    a = pd.read_csv("src/Helsingin_pyorailijamaarat.csv", sep=";").dropna(how="all").dropna(how="all", axis=1)
    b = a.Päivämäärä.str.split(" ",expand=True)
    b.columns = ["Weekday","Day", "Month", "Year","Hour"]
    b.Hour = b.Hour.str[:2]
    d = {"ma":"Mon","ti":"Tue","ke":"Wed","to":"Thu","pe":"Fri","la":"Sat","su":"Sun"} 
    m = {"tammi":1,"helmi":2,"maalis":3,"huhti":4,"touko":5,"kesä":6,"heinä":7,"elo":8,"syys":9,"loka":10,"marras":11,"joulu":12}
    b.Weekday = b.Weekday.map(d)
    b.Month = b.Month.map(m)
    b = b.astype({"Weekday":object,"Day":int,"Month":int,"Year":int,"Hour":int})
    a.drop("Päivämäärä", axis=1, inplace=True)
    return pd.concat([b, a], axis=1)

def cyclists_per_day():
    return split_date().drop(["Weekday", "Hour"], axis=1).groupby(["Year","Month","Day"]).sum()
    
def main():
    plt.plot(cyclists_per_day().loc[2017,8])
    plt.show()

if __name__ == "__main__":
    main()