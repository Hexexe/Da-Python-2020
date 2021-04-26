#!/usr/bin/env python3
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA


def explained_variance():
    df = pd.read_csv("src/data.tsv", sep="\t")
    return df.var(axis=0), PCA().fit(df).explained_variance_


def main():
    var, exv = explained_variance()
    print(f"The variances are: {' '.join(f'{i:.3f}' for i in var)}")
    print(f"The explained variances after PCA are: {' '.join(f'{i:.3f}' for i in exv)}")
    cs = np.cumsum(exv)
    plt.plot(np.arange(1, len(cs)+1), cs)
    plt.show()


if __name__ == "__main__":
    main()
