def part1(data):
    values = [int(value) for value in data.splitlines()]
    preamble = values[:25]
    counter = 25

    while True:
        value = values[counter]
        if value not in (x + y for i, x in enumerate(preamble) for j, y in enumerate(preamble) if i != j):
            return value

        preamble.pop(0)
        preamble.append(value)
        counter += 1


def part2(data):
    target_value = part1(data)
    values = [int(value) for value in data.splitlines()]

    starting_from = 0
    counter = 0
    sum_ = 0

    while True:
        sum_ += values[counter]
        if sum_ == target_value:
            contiguous_values = values[starting_from:counter]
            return min(contiguous_values) + max(contiguous_values)
        elif sum_ > target_value:
            starting_from += 1
            counter = starting_from
            sum_ = 0
        else:
            counter += 1
