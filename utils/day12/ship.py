import typing

from utils.day12.constants import RIGHT, FORWARD, directional_mappings
from utils.day12.instruction import Instruction
from utils.day12.vector import Vector


class BaseShip:
    def __init__(self):
        self.ship_location = Vector(0, 0)
        self.current_direction = Vector(1, 0)
        self.waypoint_location = Vector(10, 1)

    @staticmethod
    def convert_instructions(
        raw_instructions: typing.List[str],
    ) -> typing.Iterable[Instruction]:
        return map(
            lambda raw_instruction: Instruction(raw_instruction.strip()),
            raw_instructions,
        )

    def process_instructions(self, instructions: typing.Iterable[Instruction]):
        for instruction in instructions:
            self.process_instruction(instruction)

    def process_instruction(self, instruction: Instruction):
        if instruction.is_movement:
            self._move(instruction)
        elif instruction.is_rotation:
            self._rotate(instruction)
        else:
            self._move_forward(instruction)

    @property
    def manhattan_distance(self):
        return self.ship_location.manhattan_distance

    def _move(self, instruction: Instruction):
        mapping = directional_mappings[instruction.direction]
        vector_modifier = Vector(instruction.magnitude, instruction.magnitude)
        self.ship_location = self.ship_location + (mapping * vector_modifier)

    def _rotate(self, instruction: Instruction):
        degrees = (
            instruction.magnitude
            if instruction.direction == RIGHT
            else -1 * instruction.magnitude
        )
        self.current_direction.rotate(degrees)

    def _move_forward(self, instruction: Instruction):
        assert instruction.direction == FORWARD

        vector_magnitude = Vector(instruction.magnitude, instruction.magnitude)
        self.ship_location += self.current_direction * vector_magnitude


class ShipPart1(BaseShip):
    pass


class ShipPart2(BaseShip):
    def _rotate(self, instruction: Instruction):
        # override the rotate method since we want to rotate the waypoint
        # relative to the ship, not the ship itself
        degrees = (
            instruction.magnitude
            if instruction.direction == RIGHT
            else -1 * instruction.magnitude
        )
        self.waypoint_location.rotate(degrees, around=self.ship_location)

    def _move(self, instruction: Instruction):
        mapping = directional_mappings[instruction.direction]
        vector_modifier = Vector(instruction.magnitude, instruction.magnitude)
        self.waypoint_location = self.waypoint_location + (mapping * vector_modifier)

    def _move_forward(self, instruction: Instruction):
        assert instruction.direction == FORWARD

        vector_magnitude = Vector(instruction.magnitude, instruction.magnitude)
        direction = self.waypoint_location - self.ship_location
        movement_vector = direction * vector_magnitude

        self.ship_location += movement_vector
        self.waypoint_location += movement_vector
