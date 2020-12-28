from utils.day16.helpers import get_rules, get_tickets

test_input = """
class: 1-3 or 5-7
row: 6-11 or 33-44
seat: 13-40 or 45-50

your ticket:
7,1,14

nearby tickets:
7,3,47
40,4,50
55,2,20
38,6,12
""".strip()


def test_get_rules():
    rules = get_rules(test_input)
    assert len(rules) == 3

    rule_0 = rules[0]
    assert rule_0.name == "class"
    assert len(rule_0.conditions) == 2
    assert rule_0.conditions[0].lower_bound == 1
    assert rule_0.conditions[0].upper_bound == 3
    assert rule_0.conditions[1].lower_bound == 5
    assert rule_0.conditions[1].upper_bound == 7

    assert rules[1].name == "row"
    assert rules[2].name == "seat"


def test_get_tickets():
    tickets = get_tickets(test_input)

    assert len(tickets) == 5
    assert tickets[0].values == [7, 1, 14]  # my ticket
    assert tickets[1].values == [7, 3, 47]  # nearby tickets
