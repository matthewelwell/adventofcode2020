from utils.day18.helpers import evaluate_expression, simplify_expression


def part1(data: str):
    results = []
    for expression in data.splitlines():
        simplified_expression = simplify_expression(expression)
        results.append(evaluate_expression(simplified_expression))
    return sum(results)


def part2(data: str):
    results = []
    for expression in data.splitlines():
        simplified_expression = simplify_expression(expression, addition_first=True)
        results.append(evaluate_expression(simplified_expression, addition_first=True))
    return sum(results)
