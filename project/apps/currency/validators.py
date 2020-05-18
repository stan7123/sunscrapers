from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator

CurrencyTickerValidator = RegexValidator(regex=r'^[A-Z]{3}$', message='Currency code must be 3 letters uppercase.')
