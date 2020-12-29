import pytest

from utils.day18.helpers import evaluate_expression


@pytest.mark.parametrize("expression, expected_value", (
        ("1 + 2 * 3 + 4 * 5 + 6", 71),
        ("1 + (2 * 3) + (4 * (5 + 6))", 51)
))
def test_evaluate_expression(expression, expected_value):
    assert evaluate_expression(expression) == expected_value
