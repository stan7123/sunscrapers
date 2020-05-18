from django.db import models
from project.apps.currency.validators import CurrencyTickerValidator


class ExchangeRate(models.Model):
    base = models.CharField(max_length=3, validators=[CurrencyTickerValidator], db_index=True)
    target = models.CharField(max_length=3, validators=[CurrencyTickerValidator], db_index=True)
    # Actually rate might be negative someday - we've seen some weird rates on Crude Oil contracts lately ;)
    rate = models.DecimalField(max_digits=15, decimal_places=6)
    date = models.DateTimeField()
