import re
import typing

from utils.day14.utils import (
    get_binary_representation,
    process_floating_bits,
)


class Instruction:
    def __init__(self, integer_location: int, integer_value: int):
        self.location = Location(integer_location)
        self.integer_value = integer_value

    @property
    def binary_value(self):
        return get_binary_representation(self.integer_value)

    @classmethod
    def from_raw(cls, raw_instruction: str) -> "Instruction":
        regex_pattern = r"mem\[([0-9]+)\] \= ([0-9]+)"
        match = re.match(regex_pattern, raw_instruction)
        return cls(*[int(value) for value in match.groups()])

    def get_masked_value(self, mask: str):
        output = ""
        for i, char in enumerate(self.binary_value):
            output += char if mask[i] == "X" else mask[i]
        return output


class Location:
    def __init__(self, integer_location: int):
        self.integer_location = integer_location

    @property
    def binary_location(self):
        return get_binary_representation(self.integer_location)

    def get_masked_locations(self, mask: str) -> typing.Iterable[int]:
        masked_location = ""
        for i, char in enumerate(self.binary_location):
            mask_bit = mask[i]
            masked_location += mask_bit if mask_bit != "0" else char
        return process_floating_bits(masked_location)


class Runner:
    def __init__(self):
        self.memory = {}

    def store_value(self, instruction: Instruction, mask: str):
        masked_value = instruction.get_masked_value(mask)
        self.memory[instruction.location.integer_location] = int(masked_value, 2)

    @property
    def sum_of_values(self):
        return sum(self.memory.values())


class Part2Runner(Runner):
    def store_value(self, instruction: Instruction, mask: str):
        locations = instruction.location.get_masked_locations(mask)
        for location in locations:
            self.memory[location] = instruction.integer_value
