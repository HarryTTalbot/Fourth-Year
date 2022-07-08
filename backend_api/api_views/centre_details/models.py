from django.db import models

from backend_api.api_views.students.models import Address
from django_cryptography.fields import encrypt

class CenterDetails(models.Model):
    name = encrypt(models.CharField(max_length=50))
    phone_number = encrypt(models.CharField(max_length=17))
    address = models.ForeignKey(Address, on_delete=models.PROTECT)

    def save(self, *args, **kwargs):
        self.pk = '0'
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Center details"
