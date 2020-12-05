import pytest
from marshmallow import ValidationError

from utils.day4.validators import HeightValidator, YearValidator


@pytest.mark.parametrize(
    "height",
    (
        "1",
        "not a height",
        "1cm",
        "1in",
        "1234cm",
        "12345cm",
        "149cm",
        "194cm",
        "58in",
        "77in",
    ),
)
def test_height_validator_invalid(height):
    with pytest.raises(ValidationError):
        HeightValidator()(height)


@pytest.mark.parametrize("height", ("150cm", "193cm", "59in", "76in"))
def test_height_validator_valid(height):
    assert HeightValidator()(height) == height


@pytest.mark.parametrize(
    "year, min_year, max_year",
    (
        ("1", 2000, 2002),
        ("0001", 2000, 2002),
        ("12345", 2000, 2002),
        ("1999", 2000, 2002),
        ("2003", 2000, 2002),
    ),
)
def test_year_validator_invalid(year, min_year, max_year):
    with pytest.raises(ValidationError):
        YearValidator(min_year=min_year, max_year=max_year)(year)


@pytest.mark.parametrize(
    "year, min_year, max_year",
    (
        ("2000", 2000, 2002),
        ("2002", 2000, 2002),
    ),
)
def test_year_validator_valid(year, min_year, max_year):
    assert YearValidator(min_year=min_year, max_year=max_year)(year) == year
