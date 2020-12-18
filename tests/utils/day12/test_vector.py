import pytest

from utils.day12.vector import Vector


@pytest.mark.parametrize("vector, rotate_by, expected_x, expected_y", (
    (Vector(1, 0), 90, 0, -1),
    (Vector(0, -1), 90, -1, 0),
    (Vector(-1, 0), 90, 0, 1),
    (Vector(0, 1), 90, 1, 0),
    (Vector(1, 0), 180, -1, 0),
    (Vector(0, 1), 180, 0, -1),
    (Vector(1, 0), -90, 0, 1),
    (Vector(0, 1), -90, -1, 0),
    (Vector(-1, 0), -90, 0, -1),
    (Vector(0, -1), -90, 1, 0),
    (Vector(1, 0), -180, -1, 0),
    (Vector(0, 1), -180, 0, -1),
))
def test_rotate(vector, rotate_by, expected_x, expected_y):
    vector.rotate(rotate_by)
    assert vector.x == expected_x
    assert vector.y == expected_y
