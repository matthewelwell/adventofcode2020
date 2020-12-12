import numpy as np

from utils.day11.helpers import count_unique_values
from utils.day11.waiting_area import WaitingArea, OCCUPIED


def part1(data: str):
    seats = np.array([list(line) for line in data.splitlines()])
    waiting_area = WaitingArea(seats=seats)

    updated = True
    while updated:
        updated = waiting_area.update_seats()

    return count_unique_values(waiting_area.seats, OCCUPIED)
