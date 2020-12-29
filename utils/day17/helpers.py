import typing
from itertools import product

ACTIVE = "#"


def parse_input(data: str, dimensions: int = 3) -> typing.Set[typing.Tuple[int, ...]]:
    output = set()
    for y, line in enumerate(data.splitlines()):
        for x, state in enumerate(line.strip()):
            if state == ACTIVE:
                output.add((x, y) + (0,) * (dimensions - 2))
    return output


def perform_cycle(
    active_cubes: typing.Set[typing.Tuple], dimensions: int = 3
) -> typing.Set[typing.Tuple[int, ...]]:
    """
    Mostly borrowed from https://www.reddit.com/r/adventofcode/comments/keqsfa/2020_day_17_solutions/ghbttls
    """

    # iterate over the active cubes and build a dictionary keyed off the cubes
    # location with values equal to the number of active cubes they neighbour with
    neighbours = dict()
    for cube in active_cubes:
        for diff in filter(
            lambda d: d != (0,) * dimensions, product((-1, 0, 1), repeat=dimensions)
        ):
            neighbour_position = tuple(i + di for i, di in zip(cube, diff))
            neighbours[neighbour_position] = neighbours.get(neighbour_position, 0) + 1

    # build a new set of active cubes by looking at the number of neighbours for
    # each cube that has at least one active cube as a neighbour (as built above)
    new_active_cubes = set()
    for position, neighbours in neighbours.items():
        if (position in active_cubes and neighbours == 2) or neighbours == 3:
            new_active_cubes.add(position)

    return new_active_cubes
