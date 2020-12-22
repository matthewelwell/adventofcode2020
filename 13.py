import numpy

from utils.day13.bus import Bus
from utils.day13.utils import lcm


def part1(data):
    lines = data.splitlines()

    earliest_timestamp = int(lines[0])
    bus_ids = [id_.strip() for id_ in lines[1].split(",")]

    bus_ids_in_service = filter(lambda id_: id_ != "x", bus_ids)
    buses = map(lambda id_: Bus(int(id_)), bus_ids_in_service)

    earliest_departure_time = None
    bus_id_to_catch = None

    for bus in buses:
        next_departure = bus.next_departure_time(earliest_timestamp)
        if not earliest_departure_time or next_departure < earliest_departure_time:
            bus_id_to_catch = bus.id
            earliest_departure_time = next_departure

    return (earliest_departure_time - earliest_timestamp) * bus_id_to_catch


def part2(data):
    lines = data.splitlines()
    bus_ids = [id_.strip() for id_ in lines[1].split(",")]
    buses = {i: Bus(int(id_)) for i, id_ in enumerate(bus_ids) if id_ != "x"}

    timestamp = 0
    wait_time = 1

    for i, bus in buses.items():
        while True:
            if (timestamp + i) % bus.id == 0:
                wait_time *= bus.id
                break
            timestamp += wait_time

    return timestamp
