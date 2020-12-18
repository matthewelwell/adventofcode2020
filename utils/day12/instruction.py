from utils.day12.constants import LEFT, RIGHT, directional_mappings


class Instruction:
    def __init__(self, raw_instruction: str):
        self.direction = raw_instruction[0]
        self.magnitude = int(raw_instruction[1:])

    def __str__(self):
        return f"{self.direction}{self.magnitude}"

    @property
    def is_movement(self):
        return self.direction in directional_mappings

    @property
    def is_rotation(self):
        return self.direction in {LEFT, RIGHT}