import typing
from dataclasses import dataclass


@dataclass
class Edge:
    weight: int
    colour: str

    def __hash__(self):
        return hash(f"{self.weight}_{self.colour}")


def build_graph(data: str):
    return {
        node: edges for node, edges in [parse_input(line) for line in data.splitlines()]
    }


def parse_input(input_: str) -> typing.Tuple[str, typing.Set[Edge]]:
    node, edges_raw = input_.split("bags contain")
    edges = set()
    for child_bag_data in edges_raw.split(","):
        if child_bag_data.strip() == "no other bags.":
            break

        words = child_bag_data.split()
        words.pop()  # to remove the keyword bag / bags from the end of the list
        quantity = int(words.pop(0))
        colour = " ".join(words)
        edges.add(Edge(weight=quantity, colour=colour))

    return node.strip(), edges


def count_suitable_containers(graph: dict, target: str):
    return sum(
        can_contain_target(graph, key, target) for key in graph.keys() if key != target
    )


def can_contain_target(graph: dict, key: str, target: str):
    if not graph[key]:
        return False
    if target in map(lambda edge: edge.colour, graph[key]):
        return True

    return any(
        can_contain_target(graph, child.colour, target) for child in graph[key]
    )


def count_child_bags(graph: dict, target: str) -> int:
    return sum(key.weight * _count_child_bags(graph, key.colour) for key in graph[target])


def _count_child_bags(graph: dict, key: str) -> int:
    count = 1
    for child in graph[key]:
        count += child.weight * _count_child_bags(graph, child.colour)
    return count
