import typing
from dataclasses import dataclass


@dataclass
class Instruction:
    NOP = "nop"
    ACC = "acc"
    JMP = "jmp"

    operation: str
    argument: int = None

    def switch_operation(self):
        self.operation = self.NOP if self.operation == self.JMP else self.JMP


class BootCodeRunner:
    accumulator: int
    counter: int
    executed = set()

    def run(self, instructions: typing.List[Instruction]):
        # always reset the state variables on a new run
        self.accumulator = 0
        self.counter = 0
        self.executed = set()

        num_instructions = len(instructions)

        while True:
            if self.counter in self.executed or self.counter == num_instructions:
                break
            self.execute_instruction(instructions[self.counter])

    def execute_instruction(self, instruction):
        self.executed.add(self.counter)
        executor = self.get_executor(instruction.operation)
        executor(instruction)

    def get_executor(self, operation):
        return getattr(self, f"execute_{operation.lower()}")

    def execute_nop(self, instruction: Instruction):
        self.counter += 1

    def execute_jmp(self, instruction: Instruction):
        self.counter += instruction.argument

    def execute_acc(self, instruction: Instruction):
        self.accumulator += instruction.argument
        self.counter += 1


def parse_instructions(input_: str) -> typing.List[Instruction]:
    return list(map(parse_raw_instruction, input_.splitlines()))


def parse_raw_instruction(raw_instruction: str) -> Instruction:
    operation, raw_argument = raw_instruction.split()
    return Instruction(operation=operation, argument=int(raw_argument))


def switch_operation(instruction: Instruction) -> None:
    instruction.operation = (
        Instruction.NOP if instruction.operation == Instruction.JMP else Instruction.JMP
    )
