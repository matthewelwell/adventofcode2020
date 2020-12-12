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
        new_seats = np.copy(self.seats)
        updated = False

        for i in range(self.rows):
            for j in range(self.cols):
                value = self.seats[i, j]
                if value == VACANT:
                    new_seats[i, j] = (
                        OCCUPIED
                        if OCCUPIED not in self.get_adjacent_seats(i, j)
                        else VACANT
                    )
                elif value == OCCUPIED:
                    occupied_adjacent = self.count_occupied_adjacent(i, j)
                    new_seats[i, j] = VACANT if occupied_adjacent >= 4 else OCCUPIED
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
