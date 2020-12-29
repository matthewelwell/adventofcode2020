from utils.day17.helpers import parse_input, perform_cycle

grid = {}


def part1(data: str):
    active_cubes = parse_input(data)
    for _ in range(6):
        active_cubes = perform_cycle(active_cubes)
    return len(active_cubes)


def part2(data: str):
    active_cubes = parse_input(data, dimensions=4)
    for _ in range(6):
        active_cubes = perform_cycle(active_cubes, dimensions=4)
    return len(active_cubes)
