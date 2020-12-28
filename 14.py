from utils.day14.runner import Runner, Instruction


def part1(data):
    lines = data.splitlines()

    runner = Runner()

    for line in lines:
        words = line.split()
        if words[0] == "mask":
            runner.mask = words[-1]
        else:
            runner.store_value(Instruction.from_raw(line))

    return runner.sum_of_values


def part2(data):
    pass
