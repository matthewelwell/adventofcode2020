import numpy as np

from utils.day11.helpers import count_unique_values

VACANT = "L"
OCCUPIED = "#"
FLOOR = "."


class WaitingArea:
    def __init__(self, seats: np.ndarray):
        self.seats = seats
        self.rows, self.cols = seats.shape

    def update_seats(self) -> bool:
        new_array = np.copy(self.seats)
        updated = False

        for i in range(0, self.rows):
            for j in range(0, self.cols):
                value = self.seats[i, j]
                if value == VACANT:
                    new_array[i, j] = OCCUPIED if OCCUPIED not in self.get_adjacent_seats(i, j) else VACANT
                elif value == OCCUPIED:
                    occupied_adjacent = self.count_occupied_adjacent(i, j)
                    new_array[i, j] = VACANT if occupied_adjacent >= 4 else OCCUPIED
                else:
                    new_array[i, j] = value

                # set a state value to confirm if any updates
                # were made in this iteration
                if not updated and new_array[i, j] != self.seats[i, j]:
                    updated = True

        self.seats = new_array

        return updated

    def get_adjacent_seats(self, x: int, y: int) -> np.ndarray:
        min_x = max(x - 1, 0)
        max_x = min(x + 2, self.cols)
        min_y = max(y - 1, 0)
        max_y = min(y + 2, self.rows)
        return self.seats[min_x:max_x, min_y:max_y]

    def count_occupied_adjacent(self, x: int, y: int) -> int:
        adjacent_seats = self.get_adjacent_seats(x, y)
        count = count_unique_values(adjacent_seats, OCCUPIED)
        return count - 1  # -1 to account for seat we're looking at
