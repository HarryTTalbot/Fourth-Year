from django.db import models
from django.contrib.auth.models import User
import datetime
from django_cryptography.fields import encrypt


class Staff(models.Model):
    id = models.AutoField(primary_key=True)

    first_name = models.CharField(max_length=50)
    middle_name = encrypt(models.CharField(max_length=50, blank=True))
    last_name = models.CharField(max_length=50)

    job_title = models.CharField(max_length=50)

    join_date = encrypt(models.DateField(blank=True, null=True))
    leave_date = encrypt(models.DateField(blank=True, null=True))

    user = models.OneToOneField(User, null=True, on_delete=models.SET_NULL)
    passcode = models.CharField(max_length=50, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    last_modified_at = models.DateTimeField(auto_now=True)

    deleted_at = encrypt(models.DateTimeField(blank=True, null=True))
    GDPR_RETENTION_PERIOD = datetime.timedelta(days=60 * 30)

    class Meta:
        verbose_name_plural = "Staff"

    def __str__(self):
        names = filter(
            bool, (self.first_name, self.middle_name, self.last_name))
        return " ".join(names)
