from utils.day12.ship import BaseShip, ShipPart1, ShipPart2


def part1(data):
    instructions = ShipPart1.convert_instructions(data.splitlines())

    ship = ShipPart1()
    ship.process_instructions(instructions)
    return ship.manhattan_distance


def part2(data):
    instructions = ShipPart2.convert_instructions(data.splitlines())

    ship = ShipPart2()
    ship.process_instructions(instructions)
    return ship.manhattan_distance

