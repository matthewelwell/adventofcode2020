import typing


def build_graph(data: str):
    return {
        node: edges for node, edges in [parse_input(line) for line in data.splitlines()]
    }


def parse_input(input_: str) -> typing.Tuple[str, typing.Set[typing.Tuple]]:
    node, edges_raw = input_.split("bags contain")
    edges = set()
    for child_bag_data in edges_raw.split(","):
        if child_bag_data.strip() == "no other bags.":
            break

        words = child_bag_data.split()
        words.pop()  # to remove the keyword bag / bags from the end of the list
        quantity = int(words.pop(0))
        colour = " ".join(words)
        edges.add((quantity, colour))

    return node.strip(), edges


def count_suitable_containers(graph: dict, target: str):
    return sum(
        can_contain_target(graph, key, target) for key in graph.keys() if key != target
    )


def can_contain_target(graph: dict, key: str, target: str):
    if not graph[key]:
        return False
    if target in map(lambda edge: edge[1], graph[key]):
        return True

    return any(
        can_contain_target(graph, child[1], target) for child in graph[key]
    )


def count_child_bags(graph: dict, target: str) -> int:
    return sum(key[0] * _count_child_bags(graph, key[1]) for key in graph[target])


def _count_child_bags(graph: dict, key: str) -> int:
    count = 1
    for child in graph[key]:
        count += child[0] * _count_child_bags(graph, child[1])
    return count
