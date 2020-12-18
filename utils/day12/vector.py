import math

import numpy as np


class Vector:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def __str__(self):
        return self.x, self.y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __mul__(self, other):
        return Vector(self.x * other.x, self.y * other.y)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def rotate(self, degrees: int):
        degrees = degrees if degrees > 0 else 360 - abs(degrees)

        self.x, self.y = {
            90: (self.y, -self.x),
            180: (-self.x, -self.y),
            270: (-self.y, self.x)
        }.get(degrees)

    @property
    def manhattan_distance(self):
        return abs(self.x) + abs(self.y)
