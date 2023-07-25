from django.apps import AppConfig


class Signalapp1Config(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'SignalApp1'

    def ready(self) -> None:
        import SignalApp1.signals
