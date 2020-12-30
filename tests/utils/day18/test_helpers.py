import pytest

from utils.day18.helpers import evaluate_expression, simplify_expression


@pytest.mark.parametrize(
    "expression, addition_first, expected_value",
    (
        ("1 + 2 * 3 + 4 * 5 + 6", False, 71),
        ("25920 * 2", False, 51840),
        ("1 + 2 * 3 + 4 * 5 + 6", True, 231),
        ("1 + 2 + 3 + 4 + 5 + 6", True, 21),
    ),
)
def test_evaluate_expression(expression, addition_first, expected_value):
    assert (
        evaluate_expression(expression, addition_first=addition_first) == expected_value
    )


@pytest.mark.parametrize(
    "expression, expected_value", (("((1 + 2) * (3 + 4)) * 5 + 6", "21 * 5 + 6"),)
)
def test_simplify_expression(expression, expected_value):
    assert simplify_expression(expression) == expected_value


@pytest.mark.parametrize(
    "expression, expected_value",
    (
        ("1 + (2 * 3) + (4 * (5 + 6))", 51),
        ("2 * 3 + (4 * 5)", 46),
        ("5 + (8 * 3 + 9 + 3 * 4 * 3)", 1445),
        ("5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))", 669060),
        ("((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2", 23340),
    ),
)
def test_simplify_and_evaluate(expression, expected_value):
    simplified_expression = simplify_expression(expression, addition_first=True)
    assert evaluate_expression(simplified_expression, addition_first=True)
