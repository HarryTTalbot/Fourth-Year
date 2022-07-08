from django.db import models
from backend_api.api_views.students.models import Student
from django_cryptography.fields import encrypt

class Class(models.Model):
    id = models.AutoField(primary_key=True)

    name = models.CharField(max_length=50)

    created_at = models.DateTimeField(auto_now_add=True)
    last_modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Classes"


class Class_Student(models.Model):
    id = models.AutoField(primary_key=True)

    student = models.ForeignKey(
        Student, related_name='class_students', on_delete=models.CASCADE)
    class_fk = models.ForeignKey(
        Class, related_name='student_classes', on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    last_modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.student} → {self.class_fk}"

    class Meta:
        unique_together = ['student', 'class_fk']
