import math
import random

from matplotlib import pyplot
import numpy as np

# def gaussian(x, a, b, c):
# 	return - a * math.exp(-((x - b) ** 2) / (2 * c * c))


# print(gaussian(-1, 1, 1, 1))


def gaussian(x, a, b, c):
    return a * np.exp(-np.power(x - b, 2.) / (0.1 * np.power(c, 2.)))


def main():
    for a, b, c in [(1, 0, 1)]:
        pyplot.plot(gaussian(np.arange(0, 1, 0.01, dtype=float), a, b, c))

    # print(random.uniform(gaussian(player.pause, 1, 0, 100), 1))


if __name__ == '__main__':
    main()
