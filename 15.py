import typing

from utils.day15.game import Game


def part1(data: str) -> typing.Union[str, int]:
    starting_numbers = list(int(number) for number in data.split(","))
    game = Game(starting_numbers)
    results = game.play(to=2020)
    return list(results)[-1]


def part2(data: str) -> typing.Union[str, int]:
    pass
