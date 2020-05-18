from django.urls import path
from project.apps.currency.views import ExchangeRateListView

urlpatterns = [
    path('currency/', ExchangeRateListView.as_view())
]
