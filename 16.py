from copy import copy

from utils.day16.helpers import get_rules, get_tickets
from utils.day16.tickets import TicketScanner


def part1(data: str):
    rules = get_rules(data)
    tickets = get_tickets(data)

    nearby_tickets = tickets[1:]

    error_values = []
    for ticket in nearby_tickets:
        error_values.extend(ticket.get_invalid_values(rules))

    return sum(error_values)


def part2(data: str):
    rules = get_rules(data)
    tickets = get_tickets(data)

    num_rules = len(rules)

    my_ticket = tickets[0]
    nearby_tickets = tickets[1:]

    scanner = TicketScanner(rules)

    valid_tickets = list(filter(lambda t: t.get_invalid_values(rules) == [], nearby_tickets))

    position_possible_rules = {}

    for position in range(num_rules):
        values = set(map(lambda t: t.values[position], valid_tickets))
        for rule in scanner.rules:
            if all(rule.rule.matches(v) for v in values):
                current_possible_rules = position_possible_rules.get(position, set())
                current_possible_rules.add(rule)
                position_possible_rules[position] = current_possible_rules

    allocated_rules = set()
    while not len(allocated_rules) == len(rules):
        for key, value in position_possible_rules.items():
            possible_rules = list(value.difference(allocated_rules))
            if len(possible_rules) == 1:
                rule = possible_rules[0]
                rule.position = key
                allocated_rules.add(rule)

    value = 1
    for rule in filter(lambda r: r.rule.name.startswith("departure"), scanner.rules):
        value *= my_ticket.values[rule.position]

    return value
