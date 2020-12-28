import re
import typing

from utils.day16.tickets import Condition, Rule, Ticket


def get_rules(data: str) -> typing.List[Rule]:
    pattern = r"([a-z ]+): ([0-9]+)-([0-9]+) or ([0-9]+)-([0-9]+)"
    rules = []
    for match in re.findall(pattern, data):
        name = match[0].strip()
        conditions = []
        for lower, upper in zip(match[1::2], match[2::2]):
            conditions.append(Condition(int(lower), int(upper)))
        rules.append(Rule(name=name, conditions=conditions))
    return rules


def get_tickets(data: str) -> typing.List[Ticket]:
    pattern = r"\n([0-9,]+)"
    tickets = []
    for match in re.findall(pattern, data):
        tickets.append(Ticket([int(value) for value in match.split(",")]))
    return tickets
