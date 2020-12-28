import re


class Instruction:
    def __init__(self, location: int, integer_value: int):
        self.location = location
        self.integer_value = integer_value

    @classmethod
    def from_raw(cls, raw_instruction: str) -> "Instruction":
        regex_pattern = r"mem\[([0-9]+)\] \= ([0-9]+)"
        match = re.match(regex_pattern, raw_instruction)
        return cls(*[int(value) for value in match.groups()])


class Runner:
    def __init__(self, mask: str = "X" * 32):
        self.mask = mask
        self.memory = {}

    def store_value(self, instruction: Instruction):
        masked_value = self.apply_mask(instruction.integer_value)
        self.memory[instruction.location] = int(masked_value, 2)

    def apply_mask(self, integer_value: int) -> str:
        output = ""
        binary_value = '{:036b}'.format(integer_value)
        for i, char in enumerate(binary_value):
            output += char if self.mask[i] == "X" else self.mask[i]
        return output

    @property
    def sum_of_values(self):
        return sum(self.memory.values())
