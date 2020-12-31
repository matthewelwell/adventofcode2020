import pytest

from utils.day18.helpers import evaluate_expression, simplify_expression


@pytest.mark.parametrize(
    "expression, addition_first, expected_value",
    (
        ("1 + 2 * 3 + 4 * 5 + 6", False, 71),
        ("25920 * 2", False, 51840),
        ("1 + 2 * 3 + 4 * 5 + 6", True, 231),
        ("1 + 2 + 3 + 4 + 5 + 6", True, 21),
        ("1 + 3", True, 4),
        ("1 + 3 * 4", True, 16),
        ("8 * 3 + 9 + 3 * 4 * 3", True, 1440),
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
        ("(1 + 3 * 4) + (2 + 5) * (3 * 7)", 483),
        ("((1 + 3) * 7 + 6) + (5 + 10 * 2) * (9 + 1)", 820),
        ("4 + (8 + 9 * 5) + 5 + 9 + 6 + 2", 111),
        ("7 + 7 + 3 + 9 + ((6 + 5) * 8 * 2) * 6", 1212),
        ("9 * 4", 36),
        ("1 + 2 + 3 * 4", 24),
    ),
)
def test_simplify_and_evaluate(expression, expected_value):
    simplified_expression = simplify_expression(expression, addition_first=True)
    assert (
        evaluate_expression(simplified_expression, addition_first=True)
        == expected_value
    )
