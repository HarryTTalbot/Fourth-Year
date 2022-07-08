"""
Override production settings with development settings here
"""
from pathlib import Path

DEBUG = True

APP_DATA_DIR = Path(__file__).resolve().parent.parent / 'dev_app_data'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': APP_DATA_DIR / 'database' / 'db.sqlite3',
    }
}

DUMP_EXPORT_ROOT = APP_DATA_DIR / "dump_export"

DUMP_IMPORT_ROOT = APP_DATA_DIR / "dump_import"

KSIS_ROOT = APP_DATA_DIR / "k_sis"

REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': [
        'rest_framework.renderers.JSONRenderer',
        'rest_framework.renderers.BrowsableAPIRenderer',
    ],
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 5,
    #'DEFAULT_PERMISSION_CLASSES': ['rest_framework.permissions.IsAuthenticated'],
    #'DEFAULT_AUTHENTICATION_CLASSES': ['rest_framework.authentication.TokenAuthentication'],
}
