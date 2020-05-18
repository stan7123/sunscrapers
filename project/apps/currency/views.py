from django.shortcuts import get_object_or_404
from rest_framework.generics import ListAPIView, RetrieveAPIView
from project.apps.currency.serializers import ExchangeRateSerializer
from project.apps.currency.models import ExchangeRate


class ExchangeRateListView(ListAPIView):
    serializer_class = ExchangeRateSerializer
    queryset = ExchangeRate.objects.all()


class ExchangeRateRetrieveView(RetrieveAPIView):
    serializer_class = ExchangeRateSerializer
    queryset = ExchangeRate.objects.all()
    lookup_fields = ('base', 'target')

    def get_object(self):
        queryset = self.get_queryset()
        queryset = self.filter_queryset(queryset)
        fltr = {field: self.kwargs.get(field, None) for field in self.lookup_fields}
        return get_object_or_404(queryset, **fltr)
