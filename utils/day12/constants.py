from utils.day12.vector import Vector

EAST = "E"
WEST = "W"
NORTH = "N"
SOUTH = "S"
LEFT = "L"
RIGHT = "R"
FORWARD = "F"
directional_mappings = {
    EAST: Vector(1, 0),
    SOUTH: Vector(0, -1),
    WEST: Vector(-1, 0),
    NORTH: Vector(0, 1),
}