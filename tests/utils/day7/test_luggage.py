from utils.day7.luggage import parse_input, count_suitable_containers, build_graph, count_child_bags


def test_bag_parse_input_valid_children():
    # Given
    input_ = f"light red bags contain 1 bright white bag, 2 muted yellow bags"

    # When
    node, edges = parse_input(input_)

    # Then
    assert node == "light red"
    assert len(edges) == 2
    assert edges == {(1, "bright white"), (2, "muted yellow")}


def test_bag_parse_input_no_children():
    # Given
    input_ = f"light red bags contain no other bags."

    # When
    node, edges = parse_input(input_)

    # Then
    assert node == "light red"
    assert edges == set()


def test_count_suitable_containers():
    # Given
    sample_input = """
        light red bags contain 1 bright white bag, 2 muted yellow bags.
        dark orange bags contain 3 bright white bags, 4 muted yellow bags.
        bright white bags contain 1 shiny gold bag.
        muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
        shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
        dark olive bags contain 3 faded blue bags, 4 dotted black bags.
        vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
        faded blue bags contain no other bags.
        dotted black bags contain no other bags.
    """
    graph = build_graph(sample_input.strip())

    # When
    suitable_containers = count_suitable_containers(graph, "shiny gold")

    # Then
    assert suitable_containers == 4


def test_count_child_bags_simple():
    # Given
    input = """
        shiny gold bags contain 2 dark red bags.
        dark red bags contain no other bags.
    """
    graph = build_graph(input.strip())

    # When
    count = count_child_bags(graph, "shiny gold")

    # Then
    assert count == 2


def test_count_child_bags():
    # Given
    test_input = """
        shiny gold bags contain 2 dark red bags.
        dark red bags contain 2 dark orange bags.
        dark orange bags contain 2 dark yellow bags.
        dark yellow bags contain 2 dark green bags.
        dark green bags contain 2 dark blue bags.
        dark blue bags contain 2 dark violet bags.
        dark violet bags contain no other bags.
        plum bags contain no other bags.
    """
    graph = build_graph(test_input.strip())

    # When
    child_bags = count_child_bags(graph, "shiny gold")

    # Then
    assert child_bags == 126
