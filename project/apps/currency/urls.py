from django.urls import path
from project.apps.currency.views import ExchangeRateListView, ExchangeRateRetrieveView

urlpatterns = [
    path('currency/', ExchangeRateListView.as_view()),
    path('currency/<base>/<target>/', ExchangeRateRetrieveView.as_view())
]
