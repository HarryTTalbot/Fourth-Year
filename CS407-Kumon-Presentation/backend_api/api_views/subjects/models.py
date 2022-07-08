from django.db import models


class Subject(models.Model):
    id = models.AutoField(primary_key=True)

    name = models.CharField(max_length=50)

    created_at = models.DateTimeField(auto_now_add=True)
    last_modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Subject_Level(models.Model):
    id = models.AutoField(primary_key=True)

    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)

    name = models.CharField(max_length=50)

    created_at = models.DateTimeField(auto_now_add=True)
    last_modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.subject} {self.name}"
