import re

from utils.day4.schemas import PassportDataSchema


class Passport:
    schema = PassportDataSchema()

    required_attributes = ("byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid")

    def __init__(self, data: str):
        self.attributes = dict()
        for attribute_data in re.split(r" |\n", data):
            key, value = attribute_data.split(":")
            self.attributes[key] = value

    def has_required_attributes(self):
        return all(attr in self.attributes for attr in self.required_attributes)

    def is_valid(self):
        errors = self.schema.validate(self.attributes)
        return not errors
