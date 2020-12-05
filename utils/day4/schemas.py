from marshmallow import Schema, fields, validate

from utils.day4.validators import HeightValidator


class PassportDataSchema(Schema):
    byr = fields.Int(required=True, validate=validate.Range(min=1920, max=2002))
    iyr = fields.Int(required=True, validate=validate.Range(min=2010, max=2020))
    eyr = fields.Int(required=True, validate=validate.Range(min=2020, max=2030))
    hgt = fields.Str(required=True, validate=HeightValidator())
    hcl = fields.Str(required=True, validate=validate.Regexp(r"^#[0-9a-f]{6}$"))
    ecl = fields.Str(
        required=True,
        validate=validate.OneOf(("amb", "blu", "brn", "gry", "grn", "hzl", "oth")),
    )
    pid = fields.Str(required=True, validate=validate.Regexp(r"^[0-9]{9}$"))
    cid = fields.Str(required=False)
