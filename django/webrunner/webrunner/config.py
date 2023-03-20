from django.apps import AppConfig

class Config(AppConfig):

    def ready(self) -> None:
        import webrunner.celery
        return super().ready()