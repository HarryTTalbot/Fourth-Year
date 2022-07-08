from django.contrib import admin
from django.apps import apps

# Register your models here.

models = apps.get_app_config('backend_api').get_models()

for model in models:
    admin.site.register(model)