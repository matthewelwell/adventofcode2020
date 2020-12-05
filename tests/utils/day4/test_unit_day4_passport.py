from utils.day4.passport import Passport


def test_passport_is_not_valid_for_invalid_passports(invalid_passports):
    assert not any(Passport(data).is_valid() for data in invalid_passports)


def test_passport_is_valid_for_valid_passports(valid_passports):
    assert all(Passport(data).is_valid() for data in valid_passports)
