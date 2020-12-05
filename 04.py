from utils.day4.passport import Passport


def part1(data):
    passport_data = data.split("\n\n")
    print(passport_data[0])
    print(passport_data[-1])

    return sum(
        (
            1 if Passport(passport_data).has_required_attributes() else 0
            for passport_data in data.split("\n\n")
        )
    )


def part2(data):
    return sum(
        (
            1 if Passport(passport_data).is_valid() else 0
            for passport_data in data.split("\n\n")
        )
    )
