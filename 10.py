def part1(data):
    joltages = sorted([int(joltage) for joltage in data.splitlines()])

    # add the port and device joltages
    joltages.insert(0, 0)
    joltages.append(joltages[-1] + 3)

    joltage_differences = {1: 0, 3: 0}
    for joltage_1, joltage_2 in zip(joltages[:-1], joltages[1:]):
        diff = joltage_2 - joltage_1
        joltage_differences[diff] += 1

    return joltage_differences[1] * joltage_differences[3]


def part2(data):
    adaptors = sorted([int(adaptor) for adaptor in data.splitlines()])
    # outlet joltage
    adaptors.insert(0, 0)
    # device joltage
    adaptors.append(adaptors[-1] + 3)

    total_adaptors = len(adaptors)

    # seed with the initial arrangement
    permutations = [1]

    # count the number of ways to reach each element in the series by summing the
    # ways to reach each of the previous values
    for i in range(1, total_adaptors):
        # start with the number of ways to reach the previous value
        ways_to_reach = permutations[i - 1]
        # set j to be the index of the adaptor 3 places behind the current index
        j = i - 2
        # while that index is valid (>=0) and the difference between the adaptors
        # at the two indexes is less than or equal to 3
        while j >= 0 and adaptors[i] - adaptors[j] <= 3:
            # add the number of permutations possible to reach the value at index j
            ways_to_reach += permutations[j]
            # decrement j to check the number 1 index closer to the current index (i)
            j -= 1

        permutations.append(ways_to_reach)

    # return the final element in the list of permutations as it will contain the
    # number of possible permutations to reach it (based on the sum of the number of
    # permutations to reach the numbers within 3 joltages before it)
    return permutations[-1]
