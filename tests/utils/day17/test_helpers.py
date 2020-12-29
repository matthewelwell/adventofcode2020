from utils.day17.helpers import parse_input, perform_cycle, ACTIVE, print_grid

test_input = """
.#.
..#
###
""".strip()


def test_parse_input():
    # When
    active_cubes = parse_input(test_input)

    # Then
    assert len(active_cubes) == test_input.count(ACTIVE)

    assert (1, 0, 0) in active_cubes
    assert (2, 1, 0) in active_cubes


def test_perform_cycle():
    # Given
    active_cubes = parse_input(test_input)

    # When
    after_first_cycle = perform_cycle(active_cubes)

    # Then
    assert len(after_first_cycle) == 1
    print_grid(active_cubes)
