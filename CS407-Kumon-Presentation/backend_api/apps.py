from django.apps import AppConfig
from django.conf import settings
from django.core.management import call_command

import sys
import importlib

class BackendApiConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'backend_api'

    def ready(self):
        # Make neccessary local dirs

        settings.APP_DATA_DIR.mkdir(parents=True, exist_ok=True)
        (settings.APP_DATA_DIR / 'database').mkdir(parents=True, exist_ok=True)
        sys.path.append(str(settings.APP_DATA_DIR))

        # Only run migrations in production to create db if it doesn't exist
        # Don't want to risk corrupting db by running migrations every time
        if not settings.DATABASES['default']['NAME'].exists():
            call_command('makemigrations', 'backend_api')
            call_command('migrate')


