import numpy as np

from utils.day11.constants import VACANT, OCCUPIED, FLOOR
from utils.day11.helpers import count_unique_values, not_floor


class WaitingArea:
    def __init__(self, seats: np.ndarray):
        self.seats = seats
        self.rows, self.cols = seats.shape

    def update_seats(self) -> bool:
        new_seats = np.copy(self.seats)
        updated = False

        for i in range(self.rows):
            for j in range(self.cols):
                value = self.seats[i, j]
                if value == VACANT:
                    new_seats[i, j] = (
                        OCCUPIED
                        if OCCUPIED not in self.get_all_in_line_of_sight(i, j)
                        else VACANT
                    )
                elif value == OCCUPIED:
                    occupied_adjacent = self.get_all_in_line_of_sight(i, j).count(OCCUPIED)
                    new_seats[i, j] = VACANT if occupied_adjacent >= 5 else OCCUPIED
                else:
                    new_seats[i, j] = value

                # set a state value to confirm if any updates
                # were made in this iteration
                if not updated and new_seats[i, j] != self.seats[i, j]:
                    updated = True

        self.seats = new_seats
        return updated

    def get_adjacent_seats(self, x: int, y: int) -> np.ndarray:
        min_x, max_x = (max(x - 1, 0), min(x + 2, self.rows))
        min_y, max_y = (max(y - 1, 0), min(y + 2, self.cols))
        return self.seats[min_x:max_x, min_y:max_y]

    def count_occupied_adjacent(self, x: int, y: int) -> int:
        adjacent_seats = self.get_adjacent_seats(x, y)
        count = count_unique_values(adjacent_seats, OCCUPIED)
        return count - 1  # -1 to account for seat we're looking at

    def get_all_in_line_of_sight(self, x: int, y: int) -> list:
        down_slope = np.diagonal(self.seats, offset=y - x).flatten()
        up_slope = np.diagonal(
            np.fliplr(self.seats), offset=(self.cols + 1 - (x + 1)) - (y + 1)
        ).flatten()

        row = self.seats[x: x + 1].flatten()
        column = self.seats.T[y: y + 1].flatten()

        return [
            # TODO: the slopes aren't working correctly as the slicing isn't accurate
            #  need to find a way to determine where to slice the diagonal
            next(filter(not_floor, reversed(down_slope[:x])), None),
            next(filter(not_floor, down_slope[x+1:]), None),
            next(filter(not_floor, reversed(up_slope[:-y])), None),
            next(filter(not_floor, up_slope[-y-1:]), None),
            next(filter(not_floor, reversed(row[:y])), None),
            next(filter(not_floor, row[y+1:]), None),
            next(filter(not_floor, reversed(column[:x])), None),
            next(filter(not_floor, column[x+1:]), None),
        ]
