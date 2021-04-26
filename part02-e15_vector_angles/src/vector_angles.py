#!/usr/bin/env python3

import numpy as np
import scipy.linalg as l


def vector_angles(X, Y):
    gg = [np.dot(X[i], Y[i]) / (l.norm(X[i]) * l.norm(Y[i])) for i in range(X.shape[0])]
    return np.degrees(np.arccos(np.clip(gg, -1.0, 1.0)))


def main():
    x = np.array([[0, 0, 1], [-1, 1, 0]])
    y = np.array([[0, 1, 0], [1, 1, 0]])
    print(vector_angles(x, y))


if __name__ == "__main__":
    main()
