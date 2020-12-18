from utils.day12.ship import Ship


def part1(data):
    instructions = Ship.convert_instructions(data.splitlines())

    ship = Ship()
    ship.process_instructions(instructions)
    return ship.manhattan_distance

