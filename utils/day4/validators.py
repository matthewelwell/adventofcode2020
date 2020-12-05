from marshmallow import ValidationError
from marshmallow.validate import Validator


class HeightValidator(Validator):
    def __init__(self, *args, **kwargs):
        super(HeightValidator, self).__init__(*args, **kwargs)

    def __call__(self, value):
        try:
            height_value = int(value[:-2])
            unit = value[-2:]

            if (unit == "cm" and not 150 <= height_value <= 193) or (
                unit == "in" and not 59 <= height_value <= 76
            ):
                raise ValidationError("Height was not in valid range.")

            return value

        except (IndexError, ValueError):
            raise ValidationError("Height value was not in the correct format.")
