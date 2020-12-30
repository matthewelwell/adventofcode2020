import pytest

from utils.day18.helpers import evaluate_expression, simplify_expression


@pytest.mark.parametrize("expression, expected_value", (
        ("1 + 2 * 3 + 4 * 5 + 6", 71),
        ("25920 * 2", 51840)
))
def test_evaluate_expression(expression, expected_value):
    assert evaluate_expression(expression) == expected_value


@pytest.mark.parametrize("expression, expected_value", (
        ("((1 + 2) * (3 + 4)) * 5 + 6", "21 * 5 + 6"),
))
def test_simplify_expression(expression, expected_value):
    assert simplify_expression(expression) == expected_value
