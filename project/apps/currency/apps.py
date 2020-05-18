from django.apps import AppConfig


class CurrencyConfig(AppConfig):
    name = 'project.apps.currency'

    def ready(self):
        from project.apps.currency import scheduler
        scheduler.start()
