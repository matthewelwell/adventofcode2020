from utils.day12.ship import Ship


def test_process_instructions():
    # Given
    input = """
        F10
        N3
        F7
        R90
        F11
    """
    instructions = Ship.convert_instructions(input.strip().splitlines())
    ship = Ship()

    # When
    ship.process_instructions(instructions=instructions)

    # Then
    assert ship.manhattan_distance == 25
