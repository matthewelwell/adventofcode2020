from utils.day12.ship import ShipPart1, ShipPart2


def test_ship_part_1_process_instructions():
    # Given
    input = """
        F10
        N3
        F7
        R90
        F11
    """
    instructions = ShipPart1.convert_instructions(input.strip().splitlines())
    ship = ShipPart1()

    # When
    ship.process_instructions(instructions=instructions)

    # Then
    assert ship.manhattan_distance == 25


def test_ship_part_2_process_instructions():
    # Given
    input = """
        F10
        N3
        F7
        R90
        F11
    """
    instructions = ShipPart2.convert_instructions(input.strip().splitlines())
    ship = ShipPart2()

    # When
    ship.process_instructions(instructions=instructions)

    # Then
    assert ship.manhattan_distance == 286
