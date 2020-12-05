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
