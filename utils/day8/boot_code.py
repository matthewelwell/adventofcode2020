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
    counter: int

    def run(self, input_: str):
        # always reset the counter and accumulator on a new run
        self.accumulator = 0
        self.counter = 0

        instructions = self._get_instructions(input_)

        while True:
            instruction = instructions[self.counter]
            if instruction.executed:
                return self.accumulator

            handler = self.get_handler(instruction.operation)
            handler(instruction)
            instruction.executed = True

    def _get_instructions(self, input_):
        return [
            self._parse_raw_instruction(raw_instruction)
            for raw_instruction in input_.splitlines()
        ]

    @staticmethod
    def _parse_raw_instruction(raw_instruction: str) -> Instruction:
        operation, raw_argument = raw_instruction.split()
        return Instruction(operation=operation, argument=int(raw_argument))

    def get_handler(self, operation):
        return getattr(self, f"handle_{operation.lower()}")

    def handle_nop(self, instruction: Instruction):
        self.counter += 1

    def handle_jmp(self, instruction: Instruction):
        self.counter += instruction.argument

    def handle_acc(self, instruction: Instruction):
        self.accumulator += instruction.argument
        self.counter += 1
