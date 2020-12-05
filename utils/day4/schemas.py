from marshmallow import Schema, fields, validate

from utils.day4.validators import HeightValidator, YearValidator


class PassportDataSchema(Schema):
    byr = fields.Str(
        required=True, validate=YearValidator(min_year=1920, max_year=2002)
    )
    iyr = fields.Str(
        required=True, validate=YearValidator(min_year=2010, max_year=2020)
    )
    eyr = fields.Str(
        required=True, validate=YearValidator(min_year=2020, max_year=2030)
    )
    hgt = fields.Str(required=True, validate=HeightValidator())
    hcl = fields.Str(required=True, validate=validate.Regexp(r"^#[0-9a-f]{6}$"))
    ecl = fields.Str(
        required=True,
        validate=validate.OneOf(("amb", "blu", "brn", "gry", "grn", "hzl", "oth")),
    )
    pid = fields.Str(required=True, validate=validate.Regexp(r"^[0-9]{9}$"))
    cid = fields.Str(required=False)
