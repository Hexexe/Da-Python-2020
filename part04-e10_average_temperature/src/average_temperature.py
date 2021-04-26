#!/usr/bin/env python3
import pandas as pd

def average_temperature():
    a = pd.read_csv("src/kumpula-weather-2017.csv")
    return a[a["m"] == 7]["Air temperature (degC)"].mean()

def main():
    print(f"Average temperature in July: {average_temperature():.1f}")

if __name__ == "__main__":
    main()