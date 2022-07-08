from django.apps import apps
from django.core.exceptions import AppRegistryNotReady

# Guard to stop pyinstaller trying to import models which leads to an error
try:
    apps.check_apps_ready()
    from .make_report import *
except AppRegistryNotReady:
    pass
