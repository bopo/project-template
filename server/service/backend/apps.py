from django.apps import AppConfig


class BackendConfig(AppConfig):
    name = 'service.backend'
    verbose_name = '后端数据'

    def ready(self):
        try:
            from .signals import handlers
            from . import tasks
        except ImportError as e:
            raise e
