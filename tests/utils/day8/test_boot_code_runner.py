from utils.day8.boot_code import BootCodeRunner


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
        jmp -4
        acc +6
    """
    boot_code_runner = BootCodeRunner()

    # When
    value = boot_code_runner.run(test_input.strip())

    # Then
    assert value == 5
