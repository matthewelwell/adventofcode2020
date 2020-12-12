import numpy as np

from utils.day11.helpers import count_unique_values
from utils.day11.waiting_area import WaitingArea, OCCUPIED


def part1(data: str):
    # convert the data into a numpy array of 1s (occupied), 0s (vacant) and None (floor)
    array = np.array([list(line) for line in data.splitlines()])

    waiting_area = WaitingArea(seats=array)

    updated = True
    while updated:
        updated = waiting_area.update_seats()

    return count_unique_values(waiting_area.seats, OCCUPIED)

