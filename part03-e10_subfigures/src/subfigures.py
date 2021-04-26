#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt


def subfigures(a):
    fig, ax = plt.subplots(1, 2)
    ax[0].plot(a[:, 0], a[:, 1])
    ax[1].scatter(a[:, 0], a[:, 1], c=a[:, 2], s=a[:, 3])
    plt.show()


def main():
    a = np.random.randint(0, 20, (10, 4))
    print(a)
    subfigures(a)


if __name__ == "__main__":
    main()
