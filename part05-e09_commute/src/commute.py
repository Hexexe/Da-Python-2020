#!/usr/bin/env python3

import pandas as pd
import matplotlib.pyplot as plt

def split_date():
    a = pd.read_csv("src/Helsingin_pyorailijamaarat.csv", sep=";").dropna(how="all").dropna(how="all", axis=1)
    b = a.Päivämäärä.str.split(" ", expand=True)
    b.columns = ["Weekday", "Day", "Month", "Year", "Hour"]
    b.Hour = b.Hour.str[:2]
    d = {"ma": "Mon", "ti": "Tue", "ke": "Wed", "to": "Thu", "pe": "Fri", "la": "Sat", "su": "Sun"}
    m = {"tammi": 1, "helmi": 2, "maalis": 3, "huhti": 4, "touko": 5, "kesä": 6, "heinä": 7, "elo": 8, "syys": 9, "loka": 10, "marras": 11, "joulu": 12}
    b.Weekday = b.Weekday.map(d)
    b.Month = b.Month.map(m)
    b = b.astype({"Weekday": object, "Day": int, "Month": int, "Year": int, "Hour": int})
    a.drop("Päivämäärä", axis=1, inplace=True)
    return pd.concat([b, a], axis=1)

def bicycle_timeseries():
    a = split_date()
    a["Date"] = pd.to_datetime(a[["Year", "Month", "Day", "Hour"]])
    a.drop(["Year", "Month", "Day","Hour"], axis=1, inplace=True)
    a.set_index("Date", inplace=True)
    return a

def commute():
    a = bicycle_timeseries()["2017-08-01":"2017-08-31"]
    a["Weekday"] = a.index.weekday+1
    return a.groupby("Weekday").sum()
    
def main():
    plt.plot(commute())
    w="x mon tue wed thu fri sat sun".title().split()
    plt.gca().set_xticklabels(w)
    plt.show()

if __name__ == "__main__":
    main()