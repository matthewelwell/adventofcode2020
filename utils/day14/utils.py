import typing
from itertools import product


def get_binary_representation(integer_value: int) -> str:
    return "{:036b}".format(integer_value)


def process_floating_bits(binary_string: str) -> typing.Iterable[int]:
    """
    Given a binary string, process all floating bits (X) to return all possible
    values of the string as integers.
    """

    values = []

    # generate the possible permutations of 1 & 0 according to the
    # quantity of X's that appear in the string
    permutations = product([0, 1], repeat=binary_string.count("X"))

    # for each permutation, generate a binary string that replaces
    # each X with the relevant 1 or 0 as per the permutation
    for permutation in permutations:
        output = ""
        for bit in binary_string:
            if bit == "X":
                bit = str(permutation[0])
                permutation = permutation[1:]
            output += bit
        values.append(output)

    return (int(value, 2) for value in values)


