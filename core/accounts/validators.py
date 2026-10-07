from django.core.exceptions import ValidationError
import re


def validation_iranian_cellphone(value):
    pattern = r"^(\+98|0)?9\d{9}$"
    if not re.match(pattern, value):
        raise ValidationError("Enter a valid Iraniran Cellphone")
