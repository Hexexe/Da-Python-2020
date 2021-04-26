#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt


def center(a):
    # note the order: (center_y, center_x)
    return ((a.shape[0] / 2) - 0.5, (a.shape[1] / 2) - 0.5)


def radial_distance(a):
    (h, w), c = a.shape[0:2], np.array(center(a))
    z = np.zeros((h, w))
    for i in [i[0] for i in np.ndenumerate(z)]:
        z[i] = np.linalg.norm(i - c)
    return z


def scale(a, tmin=0.0, tmax=1.0):
    """Returns a copy of array 'a' with its values scaled to be in the range
    [tmin,tmax]."""
    return np.interp(a, (a.min(), a.max()), (tmin, tmax))


def radial_mask(a):
    return scale(1 - radial_distance(a))


def radial_fade(a):
    return a * radial_mask(a).reshape(a.shape[0], a.shape[1], 1)


def main():
    painting = plt.imread("./src/painting.png")
    p = painting.copy()
    fig, ax = plt.subplots(3, 1)
    ax[0].imshow(p)
    ax[1].imshow(radial_mask(p))
    ax[2].imshow(radial_fade(p))
    plt.show()


if __name__ == "__main__":
    main()
