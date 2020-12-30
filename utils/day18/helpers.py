import re


def evaluate_expression(expression: str) -> int:
    total = None
    operator = None

    for token in expression.split():
        if token.isdigit():
            if not total:
                total = int(token)
                continue
            else:
                next_value = token
        else:
            operator = token
            continue

        total = eval(str(total) + operator + next_value)

    return total


def simplify_expression(expression: str) -> str:
    pattern = r"\([0-9*+ ]+\)"

    while expression.count("(") > 0:
        for sub_expression in re.findall(pattern, expression):
            expression = expression.replace(sub_expression, str(evaluate_expression(sub_expression[1:-1])))

    return expression
