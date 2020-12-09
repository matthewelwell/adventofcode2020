from copy import deepcopy, copy

from utils.day8.boot_code import BootCodeRunner, Instruction, parse_instructions

boot_code_runner = BootCodeRunner()


def part1(data):
    instructions = parse_instructions(data)
    boot_code_runner.run(instructions)
    return boot_code_runner.accumulator


def part2(data):
    original_instructions = parse_instructions(data)
    num_instructions = len(original_instructions)
    changed = set()

    instructions = copy(original_instructions)

    while True:
        boot_code_runner.run(instructions)
        if boot_code_runner.counter >= num_instructions:
            break

        # we didn't reach the end of the instructions so make a copy of the
        # original instructions and try changing the next nop or jmp value
        # that has not already been changed
        instructions = deepcopy(original_instructions)
        for i, instruction in enumerate(instructions):
            operation = instruction.operation
            if operation in {Instruction.JMP, Instruction.NOP} and i not in changed:
                instructions = deepcopy(original_instructions)
                instructions[i].switch_operation()
                changed.add(i)
                break

    return boot_code_runner.accumulator
