from rest_framework import serializers
from project.apps.currency.models import ExchangeRate


class ExchangeRateSerializer(serializers.ModelSerializer):

    class Meta:
        model = ExchangeRate
        fields = ('base', 'target', 'rate', 'date')
