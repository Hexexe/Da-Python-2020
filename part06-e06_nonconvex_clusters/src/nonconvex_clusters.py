#!/usr/bin/env python3

import pandas as pd
import numpy as np
from sklearn.cluster import DBSCAN
from sklearn.metrics import accuracy_score
import scipy
import matplotlib.pyplot as plt


def find_permutation(n_clusters, real_labels, labels):
    permutation = []
    for i in range(n_clusters):
        idx = labels == i
        # Choose the most common label among data points in the cluster
        new_label = scipy.stats.mode(real_labels[idx])[0][0]
        permutation.append(new_label)
    return permutation


def nonconvex_clusters():
    df = pd.read_csv("src/data.tsv", sep="\t")
    X, y, r = df[["X1", "X2"]], df["y"], []
    ll = len(y.unique())
    for i in np.arange(0.05, 0.2, 0.05):
        model = DBSCAN(i)
        model.fit(X)
        mask = model.labels_ == -1
        outliers = sum(mask)
        clusters = max(model.labels_)+1
        perm = find_permutation(clusters, y, model.labels_)
        score = accuracy_score(y[~mask], [perm[label] for label in model.labels_[~mask]]) if clusters == ll else np.nan
        r.append([i, score, clusters, outliers])
    return pd.DataFrame(r, columns=["eps", "Score", "Clusters", "Outliers"], dtype="float64")


def main():
    print(nonconvex_clusters())



if __name__ == "__main__":
    main()
