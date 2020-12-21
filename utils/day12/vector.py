

class Vector:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def __str__(self):
        return self.x, self.y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        return Vector(self.x * other.x, self.y * other.y)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def rotate(self, degrees: int, around: "Vector" = None):
        """
        General formula for rotating a point 90 degrees (clockwise)
        around point px, py:

            x' = (y - py) + px
            y' = -(x - px) + py

        """
        degrees = degrees if degrees > 0 else 360 - abs(degrees)
        around = around or Vector(0, 0)

        self.x, self.y = {
            90: ((self.y - around.y) + around.x, -(self.x - around.x) + around.y),
            180: (self.x - 2 * (self.x - around.x), self.y - 2 * (self.y - around.y)),
            270: (-(self.y - around.y) + around.x, (self.x - around.x) + around.y)
        }.get(degrees)

    @property
    def manhattan_distance(self):
        return abs(self.x) + abs(self.y)
