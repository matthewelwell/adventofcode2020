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

    def get_masked_value(self, mask: str):
        output = ""
        binary_value = '{:036b}'.format(self.integer_value)
        for i, char in enumerate(binary_value):
            output += char if mask[i] == "X" else mask[i]
        return output


class Runner:
    def __init__(self):
        self.memory = {}

    def store_value(self, instruction: Instruction, mask: str):
        masked_value = instruction.get_masked_value(mask)
        self.memory[instruction.location] = int(masked_value, 2)

    @property
    def sum_of_values(self):
        return sum(self.memory.values())
