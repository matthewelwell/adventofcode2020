from utils.day7.luggage import parse_input, count_suitable_containers, build_graph


def test_bag_parse_input_valid_children():
    # Given
    input_ = f"light red bags contain 1 bright white bag, 2 muted yellow bags"

    # When
    node, edges = parse_input(input_)

    # Then
    assert node == "light red"
    assert len(edges) == 3
    assert set(edges) == {"bright white", "muted yellow"}


def test_bag_parse_input_no_children():
    # Given
    input_ = f"light red bags contain no other bags."

    # When
    node, edges = parse_input(input_)

    # Then
    assert node == "light red"
    assert edges == []


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
