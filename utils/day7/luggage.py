import typing

valid_containers = set()


def build_graph(data: str):
    return {
        node: set(edges) for node, edges in [parse_input(line) for line in data.splitlines()]
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
