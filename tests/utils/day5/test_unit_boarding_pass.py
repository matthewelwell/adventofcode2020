import pytest

from utils.day5.boarding_pass import BoardingPass


@pytest.mark.parametrize(
    "boarding_pass, expected_row",
    (("FBFBBFFRLR", 44), ("BFFFBBFRRR", 70), ("FFFBBBFRRR", 14), ("BBFFBBFRLL", 102)),
)
def test_boarding_pass(boarding_pass: str, expected_row: int):
    assert BoardingPass(boarding_pass).row == expected_row


@pytest.mark.parametrize(
    "boarding_pass, expected_column",
    (("FBFBBFFRLR", 5), ("BFFFBBFRRR", 7), ("FFFBBBFRRR", 7), ("BBFFBBFRLL", 4)),
)
def test_boarding_pass_column(boarding_pass: str, expected_column: int):
    assert BoardingPass(boarding_pass).column == expected_column


@pytest.mark.parametrize(
    "boarding_pass, expected_seat_id",
    (
        ("FBFBBFFRLR", 357),
        ("BFFFBBFRRR", 567),
        ("FFFBBBFRRR", 119),
        ("BBFFBBFRLL", 820),
    ),
)
def test_boarding_pass_seat_id(boarding_pass: str, expected_seat_id: int):
    assert BoardingPass(boarding_pass).seat_id == expected_seat_id
