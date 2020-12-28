import pytest

from utils.day14.utils import process_floating_bits


@pytest.mark.parametrize(
    "binary_string, expected_values",
    (
        ("000000000000000000000000000000X1101X", [26, 27, 58, 59]),
        ("00000000000000000000000000000001X0XX", [16, 17, 18, 19, 24, 25, 26, 27]),
        ("000000000000000000000000000000000000", [0]),
        ("0000000000000000000000000000000000X0", [0, 2]),
    ),
)
def test_process_floating_bits(binary_string, expected_values):
    assert list(process_floating_bits(binary_string)) == expected_values
