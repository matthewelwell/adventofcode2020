import numpy as np


def part1(data: str):
    # convert the data into a numpy array
    # todo: possibly we want to convert values to 1s and 0s
    array = np.array([list(line) for line in data.splitlines()])
