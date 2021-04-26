#!/usr/bin/env python3

import pandas as pd
import numpy as np

def missing_value_types():
    return pd.DataFrame([
            ["United Kingdom", np.nan, None],
            ["Finland", 1917, "Niinistö"],
            ["USA", 1776, "Trump"],
            ["Sweden", 1523, None],
            ["Germany", np.nan, "Steinmeier"],
            ["Russia", 1992, "Putin"]
        ],
        columns=["State", "Year of independence", "President"],
    ).set_index("State")
               
def main():
    print(missing_value_types())

if __name__ == "__main__":
    main()
