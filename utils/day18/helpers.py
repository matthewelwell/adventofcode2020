import re


def evaluate_expression(expression: str, addition_first: bool = False) -> int:
    """
    Takes an expression like 1 + 2 * 3 and evaluates it. This is done in the order
    that the equation is defined, or by carrying out any addition before multiplication
    if the addition_first flag is passed.

    Note: expects the expression to be a simplified expression (i.e. contains no
    parentheses)
    """

    # if we want to carry out addition first, then we can simply replace any of the
    # addition expressions with brackets and call simplify expression on them
    # before evaluating the expression.
    # Note that we only care about expressions that contain both + and * operations,
    # otherwise the order doesn't matter.
    if addition_first and "+" in expression and "*" in expression:
        pattern = r"(?:(?:[0-9]+)* \+ [0-9]+)+"
        for match in re.findall(pattern, expression):
            expression = expression.replace(match, f"({match})")
        expression = simplify_expression(expression, addition_first=True)

    total = None
    operator = None

    # iterate over each token in the expression and calculate the totals by building
    # simple expressions and evaluating them using python's `eval` method
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


def simplify_expression(expression: str, addition_first: bool = False) -> str:
    pattern = r"\([0-9*+ ]+\)"

    while expression.count("(") > 0:
        for sub_expression in re.findall(pattern, expression):
            expression = expression.replace(
                sub_expression,
                str(
                    evaluate_expression(
                        sub_expression[1:-1], addition_first=addition_first
                    )
                ),
            )

    return expression
