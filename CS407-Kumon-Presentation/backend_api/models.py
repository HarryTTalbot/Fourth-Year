from django.db import models

import os

from django.conf import settings

import backend_api.api_views.attendance.models
# import backend_api.api_views.authentication.models
import backend_api.api_views.centre_details.models
import backend_api.api_views.classes.models
# import backend_api.api_views.data_import.models
import backend_api.api_views.inventory.models
# import backend_api.api_views.reporting.models
import backend_api.api_views.staff.models
import backend_api.api_views.students.models
import backend_api.api_views.subjects.models

from django_cryptography.fields import encrypt


# ---------------------------------------------------------------------------- #
# Import Data Files
CSV_TYPES = (
    ('k_sis', 'K_SIS'),     # In the format exported from K-SIS
    ('dumps', 'DUMPS')      # In the format exported from this app
)


def path(instance, filename):
    if instance.type == "dumps":
        return os.path.join(settings.DUMP_IMPORT_ROOT, filename)
    else:
        return os.path.join(settings.KSIS_ROOT, filename)


class File(models.Model):
    id = models.AutoField(primary_key=True)
    name = encrypt(models.CharField(max_length=100))
    type = encrypt(models.CharField(
        max_length=5, choices=CSV_TYPES, default='dumps'))
    file = encrypt(models.FileField(upload_to=path, max_length=256))
    created_at = encrypt(models.DateTimeField(auto_now_add=True))
