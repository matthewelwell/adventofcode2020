from utils.day8.boot_code import BootCodeRunner, parse_instructions


def test_boot_code_runner_run():
    # Given
    test_input = """
        nop +0
        acc +1
        jmp +4
        acc +3
        jmp -3
        acc -99
        acc +1
        nop -4
        acc +6
    """
    boot_code_runner = BootCodeRunner()
    instructions = parse_instructions(test_input.strip())

    # When
    boot_code_runner.run(instructions)

    # Then
    assert boot_code_runner.accumulator == 8
    assert boot_code_runner.counter == 9
