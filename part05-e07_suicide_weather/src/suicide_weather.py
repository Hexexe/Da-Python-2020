#!/usr/bin/env python3

import pandas as pd

def suicide_fractions():
    a = pd.read_csv("src/who_suicide_statistics.csv")
    a["Suicides"] = a['suicides_no']/a["population"]
    return a.groupby("country")["Suicides"].mean()

def suicide_weather():
    c = pd.read_html("src/List_of_countries_by_average_yearly_temperature.html", index_col="Country")[0]
    c = pd.to_numeric(c.iloc[:, 0].str.replace("\u2212", "-"))
    s = suicide_fractions()
    cat = pd.concat([s, c], axis=1, join="inner")
    return len(s), len(c), len(cat), cat.corr(method="spearman").iloc[1, 0]

def main():
    sdf, tdf, cdf, spc = suicide_weather()
    print(f'''
    Suicide DataFrame has {sdf} rows
    Temperature DataFrame has {tdf} rows
    Common DataFrame has {cdf} rows
    Spearman correlation: {spc}
    ''')

if __name__ == "__main__":
    main()