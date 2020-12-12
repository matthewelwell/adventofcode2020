import numpy as np

from utils.day11.helpers import count_unique_values
from utils.day11.waiting_area import WaitingAreaPart1, WaitingAreaPart2
from utils.day11.constants import OCCUPIED


def part1(data: str):
    seats = np.array([list(line) for line in data.splitlines()])
    waiting_area = WaitingAreaPart1(seats=seats)

    updated = True
    while updated:
        updated = waiting_area.update_seats()

    return count_unique_values(waiting_area.seats, OCCUPIED)


def part2(data: str):
    seats = np.array([list(line) for line in data.splitlines()])
    waiting_area = WaitingAreaPart2(seats=seats)

    updated = True
    while updated:
        updated = waiting_area.update_seats()

    return count_unique_values(waiting_area.seats, OCCUPIED)
