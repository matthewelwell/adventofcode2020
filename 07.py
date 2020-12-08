from utils.day7.luggage import build_graph, count_suitable_containers

target = "shiny gold"


def part1(data):
    graph = build_graph(data)
    return count_suitable_containers(graph, target)


def part2(data):
    pass
