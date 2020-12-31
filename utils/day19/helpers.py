import re
import typing


def parse_input(data: str) -> typing.Tuple[typing.Dict[int, str], typing.List[str]]:
    rules, messages = data.strip().split("\n\n")
    rules_dict = _parse_rules(rules)
    return rules_dict, messages.splitlines()


def _parse_rules(rules: str) -> typing.Dict[int, str]:
    rules_dict = {}

    pattern = r"^(\d+): ([0-9 |]+|\"[a-z]\")$"
    for raw_rule in rules.splitlines():
        id_, rule_content = re.match(pattern, raw_rule.strip()).groups()
        rules_dict[int(id_)] = rule_content

    return rules_dict


def get_matching_patterns(
    key: int,
    raw_rules_dict: typing.Dict[int, str],
    current_matching_patterns: typing.Set[str] = None,
) -> typing.Set[str]:
    value = raw_rules_dict[key]
    current_matching_patterns = current_matching_patterns or set()
    new_matching_patterns = set()

    if re.match(r"^\"[a-z]\"$", value):
        return set(value.strip('"'))

    for or_section in value.split("|"):
        for key in or_section.split():
            new_matching_patterns.update(get_matching_patterns(int(key), raw_rules_dict, current_matching_patterns))

    return new_matching_patterns
