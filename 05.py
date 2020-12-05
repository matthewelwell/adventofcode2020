from utils.day5.boarding_pass import BoardingPass


def part1(data: str):
    return max(
        bp.seat_id for bp in map(lambda row: BoardingPass(row), data.split("\n"))
    )


def part2(data: str):
    """
    Find your seat id by iterating over the sorted list of seat ids and
    checking if the next seat id is equal to the current seat id + 1.
    If not, then your seat id is that seat id + 1.
    """
    seat_ids = sorted(
        [bp.seat_id for bp in map(lambda row: BoardingPass(row), data.split("\n"))]
    )

    for i, seat_id in enumerate(seat_ids):
        if seat_ids[i + 1] != seat_id + 1:
            return seat_id + 1

    raise Exception("Couldn't find a missing seat id")
