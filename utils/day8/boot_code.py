import typing
from dataclasses import dataclass


@dataclass
class Instruction:
    NOP = "nop"
    ACC = "acc"
    JMP = "jmp"

    operation: str
    argument: int = None
    executed: bool = False


class BootCodeRunner:
    instructions: typing.List[Instruction] = []
    accumulator: int

    def run(self, input_: str):
        self.accumulator = 0  # always reset the accumulator on a new run

        instructions = [
            self._parse_raw_instruction(raw_instruction)
            for raw_instruction in input_.splitlines()
        ]

        counter = 0
        while True:
            instruction = instructions[counter]

            if instruction.executed:
                return self.accumulator
            elif instruction.operation == Instruction.NOP:
                instruction.executed = True
                counter += 1
            elif instruction.operation == Instruction.ACC:
                instruction.executed = True
                self.accumulator += instruction.argument
                counter += 1
            elif instruction.operation == Instruction.JMP:
                instruction.executed = True
                counter += instruction.argument

    def _parse_raw_instruction(self, raw_instruction: str) -> Instruction:
        operation, raw_argument = raw_instruction.split()
        return Instruction(operation=operation, argument=int(raw_argument))
