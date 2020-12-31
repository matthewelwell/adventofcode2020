import pytest

from utils.day19.helpers import parse_input, get_matching_patterns

test_input = """
0: 4 1 5
1: 2 3 | 3 2
2: 4 4 | 5 5
3: 4 5 | 5 4
4: "a"
5: "b"

ababbb
bababa
abbbab
aaabbb
aaaabbb
"""


def test_parse_input():
    rules, _ = parse_input(test_input)
    assert len(rules) == 6


@pytest.mark.parametrize("key, rules_dict, expected_pattern", (
        (0, {0: "\"a\""}, {"a"}),
        (0, {0: "1", 1: "\"a\""}, {"a"}),
        (0, {0: "1 | 2", 1: "\"a\"", 2: "\"b\""}, {"a", "b"}),
        (0, {0: "1 2 | 2 1", 1: "\"a\"", 2: "\"b\""}, {"ab", "ba"}),
        (0, {0: "1 3 | 2 1", 1: "\"a\"", 2: "\"b\"", 3: "1 1 | 2 2"}, {"aaa", "abb", "ba"}),
))
def test_get_matching_patterns(key, rules_dict, expected_pattern):
    assert get_matching_patterns(key, rules_dict) == expected_pattern
