from apscheduler.schedulers.background import BackgroundScheduler
from project.apps.currency.data_update import update_rates
from django.conf import settings


def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(update_rates, 'interval', minutes=settings.RATES_FETCH_INTERVAL_IN_MINUTES)
    scheduler.start()
