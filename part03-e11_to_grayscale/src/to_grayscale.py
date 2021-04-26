#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt


def to_red(img):
    return [1, 0, 0] * img


def to_green(img):
    return [0, 1, 0] * img


def to_blue(img):
    return [0, 0, 1] * img


def to_grayscale(img):
    return np.sum([0.2126, 0.7152, 0.0722] * img, axis=2)


def main():
    painting = plt.imread("./src/painting.png")
    p = painting.copy()
    f, ax = plt.subplots(3, 1)
    ax[0].imshow(to_red(p))
    ax[1].imshow(to_green(p))
    ax[2].imshow(to_blue(p))
    plt.show()

    plt.imshow(to_grayscale(p))
    plt.gray()
    plt.show()


if __name__ == "__main__":
    main()
