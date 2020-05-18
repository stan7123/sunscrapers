from rest_framework.generics import ListAPIView
from project.apps.currency.serializers import ExchangeRateSerializer
from project.apps.currency.models import ExchangeRate


class ExchangeRateListView(ListAPIView):
    serializer_class = ExchangeRateSerializer
    queryset = ExchangeRate.objects.all()
