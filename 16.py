from utils.day16.helpers import get_rules, get_tickets


def part1(data: str):
    rules = get_rules(data)
    tickets = get_tickets(data)

    nearby_tickets = tickets[1:]

    error_values = []
    for ticket in nearby_tickets:
        error_values.extend(ticket.get_invalid_values(rules))

    return sum(error_values)
