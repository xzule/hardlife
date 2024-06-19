from django.apps import AppConfig


class MainConfig(AppConfig):
        default_auto_field = 'django.db.models.BigAutoField'
        name = 'main'

        @classmethod
        def ready(cls):
                import main.signals
