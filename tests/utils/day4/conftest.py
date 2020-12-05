import pytest


@pytest.fixture()
def invalid_passports():
    with open("data/invalid_passports.txt", "r") as file:
        return file.read().split("\n\n")


@pytest.fixture()
def valid_passports():
    with open("data/valid_passports.txt", "r") as file:
        return file.read().split("\n\n")
