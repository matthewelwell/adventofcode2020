import typing


def evaluate_expression(expression: str) -> int:
    expression = expression.replace(" ", "")

    total = int(expression[0])
    operator = None

    for char in expression[1:]:
        if char.isdigit():
            next_digit = char
        else:
            operator = char
            continue

        total = eval(str(total) + operator + next_digit)

    return total
