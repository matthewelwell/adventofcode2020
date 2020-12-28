import typing


class Condition:
    def __init__(self, lower: int, upper: int):
        self.lower_bound = lower
        self.upper_bound = upper

    def matches(self, number: int) -> bool:
        return self.lower_bound <= number <= self.upper_bound


class Rule:
    def __init__(self, name: str, conditions: typing.List[Condition]):
        self.name = name
        self.conditions = conditions

    def matches(self, number: int) -> bool:
        return any(condition.matches(number) for condition in self.conditions)


class Ticket:
    def __init__(self, values: typing.List[int]):
        self.values = values

    def get_invalid_values(self, rules: typing.List[Rule]) -> typing.List[int]:
        invalid_values = []
        for value in self.values:
            if not any(rule.matches(value) for rule in rules):
                invalid_values.append(value)
        return invalid_values
