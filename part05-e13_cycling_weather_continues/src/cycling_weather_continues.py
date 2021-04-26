#!/usr/bin/env python3

import pandas as pd
from sklearn import linear_model

def split_date_continues():
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
    c = pd.concat([b, a], axis=1)
    return c[c["Year"]==2017].groupby(["Day","Month","Year"]).sum().reset_index()

def cycling_weather():
    a = split_date_continues()
    b = pd.read_csv("src/kumpula-weather-2017.csv")
    c = pd.merge(b, a, left_on=["d", "m", "Year"], right_on=["Day", "Month", "Year"])
    return c.drop(["m", "d", "Time", "Time zone"] ,axis=1).fillna(method="ffill")

def cycling_weather_continues(station):
    df = cycling_weather()
    r = linear_model.LinearRegression()
    x = df[['Precipitation amount (mm)','Snow depth (cm)','Air temperature (degC)']]
    y = df[[station]]
    return (r.fit(x,y).coef_[0],r.score(x,y))
    
def main():
    station = "Baana"
    coef, score = cycling_weather_continues(station)
    print(f"Measuring station: {station}")
    print(f"Regression coefficient for variable 'precipitation': {coef[0]:.1f}")
    print(f"Regression coefficient for variable 'snow depth': {coef[1]:.1f}")
    print(f"Regression coefficient for variable 'temperature': {coef[2]:.1f}")
    print(f"Score: {score:.2f}")

if __name__ == "__main__":
    main()
