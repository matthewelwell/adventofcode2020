from math import ceil


class Bus:
    def __init__(self, id_: int):
        self.id = id_

    def next_departure_time(self, after: int = None):
        return 0 if after is None else (ceil(after / self.id) * self.id)
