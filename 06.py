from utils.utils import split_on_blank_lines


def part1(data):
    sum_ = 0
    for group in split_on_blank_lines(data):
        sum_ += len(set.union(*[set(answers) for answers in group.splitlines()]))
    return sum_


def part2(data):
    sum_ = 0
    for group in split_on_blank_lines(data):
        sum_ += len(set.intersection(*[set(answers) for answers in group.splitlines()]))
    return sum_
