def part1(data):
    filtered_integers = list(int(x) for x in data.split("\n") if int(x) <= 2020)
    products = ((x + y, x, y) for x in filtered_integers for y in filtered_integers)
    for i, product_ in enumerate(products):
        if product_[0] == 2020:
            return product_[1] * product_[2]


def part2(data):
    filtered_integers = list(int(x) for x in data.split("\n") if int(x) <= 2020)
    products = ((x + y + z, x, y, z) for x in filtered_integers for y in filtered_integers for z in filtered_integers)
    for i, product_ in enumerate(products):
        if product_[0] == 2020:
            return product_[1] * product_[2] * product_[3]
