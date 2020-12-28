from utils.day14.runner import Runner, Instruction


def part1(data):
    lines = data.splitlines()

    runner = Runner()
    mask = "X" * 36

    for line in lines:
        words = line.split()
        if words[0] == "mask":
            mask = words[-1]
            continue

        runner.store_value(Instruction.from_raw(line), mask)

    return runner.sum_of_values


def part2(data):
    pass
