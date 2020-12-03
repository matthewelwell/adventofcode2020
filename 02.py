def part1(data):
    num_valid_passwords = 0
    for password_data in data.split("\n"):
        password_checker = PasswordChecker(password_data)
        if password_checker.contains_correct_num_occurrences():
            num_valid_passwords += 1
    return num_valid_passwords


def part2(data):
    num_valid_passwords = 0
    for password_data in data.split("\n"):
        password_checker = PasswordChecker(password_data)
        if password_checker.match_at_one_index():
            num_valid_passwords += 1
    return num_valid_passwords


class PasswordChecker:
    first_integer: int
    second_integer: int
    search_char: str
    password: str

    def __init__(self, password_data: str):
        """
        Takes a row from the data file and converts it to an object with the 
        relevant attributes. Expects the password_data to be in the format: 

            '{first_integer}-{second_integer} {search_char}: {password}'

        :param password_data: row from the data file, e.g. '1-3 e: abcde'
        """
        boundaries, char, self.password = password_data.split()

        first_integer, second_integer = boundaries.split("-")
        self.first_integer = int(first_integer)
        self.second_integer = int(second_integer)

        self.search_char = char[0]

    def contains_correct_num_occurrences(self):
        return (
            self.first_integer
            <= self.password.count(self.search_char)
            <= self.second_integer
        )

    def match_at_one_index(self):
        first_index_match = self.password[self.first_integer - 1] == self.search_char
        second_index_match = self.password[self.second_integer - 1] == self.search_char
        return (first_index_match and not second_index_match) or (
            not first_index_match and second_index_match
        )
