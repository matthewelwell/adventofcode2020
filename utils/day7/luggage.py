import typing

valid_containers = set()


def build_graph(data: str):
    return {
        node: edges for node, edges in [parse_input(line) for line in data.splitlines()]
    }


def parse_input(input_: str) -> typing.Tuple[str, typing.List[str]]:
    node, edges_raw = input_.split("bags contain")
    edges = []
    for child_bag_data in edges_raw.split(","):
        if child_bag_data.strip() == "no other bags.":
            break

        words = child_bag_data.split()
        words.pop()  # to remove the keyword bag / bags from the end of the list
        quantity = int(words.pop(0))
        colour = " ".join(words)
        edges.extend([colour.strip() for _ in range(quantity)])

    return node.strip(), edges


def count_suitable_containers(graph: dict, target: str):
    suitable_containers = set()
    for key in graph.keys():
        if key != target and key not in suitable_containers and can_contain_target(graph, key, target):
            suitable_containers.add(key)
    return len(suitable_containers)


def can_contain_target(graph: dict, key: str, target: str):
    if not graph[key]:
        return False
    if target in graph[key]:
        return True

    return any(
        can_contain_target(graph, child, target) for child in graph[key]
    )
