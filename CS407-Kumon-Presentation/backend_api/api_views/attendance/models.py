from django.db import models
from backend_api.api_views.classes.models import Class
from backend_api.api_views.students.models import Student
from backend_api.api_views.subjects.models import Subject_Level
from django_cryptography.fields import encrypt

class Lesson(models.Model):
    id = models.AutoField(primary_key=True)

    start_datetime = models.DateTimeField()
    end_datetime = models.DateTimeField()

    # Past lessons should remain even if class or subject no longer exists
    class_fk = models.ForeignKey(Class, null=True, on_delete=models.SET_NULL)

    subject_level = models.ForeignKey(
        Subject_Level, null=True, on_delete=models.SET_NULL)

    created_at = models.DateTimeField(auto_now_add=True)
    last_modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.class_fk} ({self.subject_level}) at {self.start_datetime:%Y-%m-%d %H:%M}"


ATTENDANCE_TYPES = [
    ('P', 'Present'),
    ('L', 'Late'),
    ('A', 'Authorized Absence'),
    ('U', 'Unauthorized Absence')
]


class Attendance(models.Model):
    id = models.AutoField(primary_key=True)

    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    status = models.CharField(max_length=1, choices=ATTENDANCE_TYPES)

    created_at = models.DateTimeField(auto_now_add=True)
    last_modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ['lesson', 'student']

    def __str__(self):
        return f"{self.student} {self.status} in {self.lesson}"


class LongTermAbsence(models.Model):
    id = models.AutoField(primary_key=True)

    student = models.ForeignKey(Student, on_delete=models.CASCADE)

    start_date = models.DateField()
    end_date = models.DateField()

    reason = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
    last_modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.student} {self.start_date}–{self.end_date}"
