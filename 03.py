import numpy


def part1(data):
    return trees_encountered(data, 3)


def part2(data):
    slopes = ((1, 1), (3, 1), (5, 1), (7, 1), (1, 2))
    return numpy.prod([trees_encountered(data, slope[0], slope[1]) for slope in slopes])


def trees_encountered(data: str, x_increment: int, y_increment: int = 1) -> int:
    index = 0
    trees = 0
    for row in data.split("\n")[::y_increment]:
        if row[index % len(row)] == "#":
            trees += 1
        index += x_increment
    return trees
