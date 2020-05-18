import logging
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from django.conf import settings
from rest_framework.exceptions import ValidationError
from project.apps.currency.serializers import ExchangeRateSerializer
from project.apps.currency.models import ExchangeRate

logger = logging.getLogger(__name__)


def update_rates():
    main_url = settings.EXCHANGE_RATES_RSS_URL
    currencies_urls = get_currencies_xml_urls(main_url)
    rates = []
    for c_url in currencies_urls:
        r = get_last_rate(c_url)
        if r is not None:
            rates.append(r)
    save_rates(rates)


def get_currencies_xml_urls(url):
    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'html.parser')
    return [urljoin(url, a['href']) for a in soup.select('.zebraList a.rss') if a['href'].startswith('/rss/fxref')]


def get_last_rate(url):
    try:
        res = requests.get(url)
        soup = BeautifulSoup(res.text, 'xml')
        last_entry = soup.find_all('item')[0]
    except Exception as e:
        logger.warning("There was error during currency rate fetching: {}".format(str(e)))
        return {}

    return {
        'base': last_entry.find('cb:baseCurrency').text,
        'target': last_entry.find('cb:targetCurrency').text,
        'rate': last_entry.find('cb:value').text,
        'date': last_entry.find('dc:date').text
    }


def save_rates(rates):
    for r in rates:
        ser = ExchangeRateSerializer(data=r)
        try:
            ser.is_valid(raise_exception=True)
            defaults = {'rate': ser.validated_data['rate'], 'date': ser.validated_data['date']}
            ExchangeRate.objects.update_or_create(base=ser.validated_data['base'], target=ser.validated_data['target'],
                                                  defaults=defaults)
        except ValidationError as ve:
            logger.warning('There was error during rate validation: {}. Data: {}'.format(str(ve), ser.initial_data))
