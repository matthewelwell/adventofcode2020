import typing

import numpy as np

from utils.day11.constants import FLOOR


def count_unique_values(array: np.ndarray, value: typing.Any) -> int:
    unique_counts = np.asarray(np.unique(array, return_counts=True)).T
    for row in unique_counts:
        if row[0] == value:
            return int(row[1])
    return 0


def not_floor(element: str) -> bool:
    return element != FLOOR
