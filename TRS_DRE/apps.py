from django.apps import AppConfig


class TrsDreConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'TRS_DRE'

    def ready(self) -> None:
        from . import auditlog
        return super().ready()