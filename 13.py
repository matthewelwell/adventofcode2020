from utils.day13.bus import Bus


def part1(data):
    lines = data.splitlines()

    earliest_timestamp = int(lines[0])
    bus_ids = [id_.strip() for id_ in lines[1].split(",")]

    bus_ids_in_service = filter(lambda id_: id_.strip() != "x", bus_ids)
    buses = map(lambda id_: Bus(int(id_.strip())), bus_ids_in_service)

    earliest_departure_time = None
    bus_id_to_catch = None

    for bus in buses:
        next_departure = bus.next_departure_time(earliest_timestamp)
        if not earliest_departure_time or next_departure < earliest_departure_time:
            bus_id_to_catch = bus.id
            earliest_departure_time = next_departure

    return (earliest_departure_time - earliest_timestamp) * bus_id_to_catch


def part2(data):
    pass
