import re

from utils.day19.helpers import parse_input, get_matching_patterns


def part1(data: str):
    raw_rules_dict, messages = parse_input(data)

    # TODO: parse the raw_rules_dict to build a new
    #  dict of sets of valid message strings
    patterns = get_matching_patterns(id_=0, raw_rules_dict=raw_rules_dict)

    valid_messages = list(filter(lambda m: m in patterns, messages))

    return len(valid_messages)


def part2(data: str):
    pass
