import os
from django.apps import AppConfig


class UsersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'users'

    def ready(self):
        import users.signals

        if os.environ.get('RUN_MAIN'):
            from users.services import start_scheduler
            start_scheduler()