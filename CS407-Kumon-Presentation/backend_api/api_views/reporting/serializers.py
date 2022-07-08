from rest_framework import serializers

from backend_api.api_views.students.models import Student
from backend_api.api_views.subjects.models import Subject_Level


class StudentRecordSheetSerializer(serializers.Serializer):
    """ Serializer for creating a record sheet for a specific student. """
    student_id = serializers.PrimaryKeyRelatedField(
        queryset=Student.objects.all(), many=True)
    subject_level_id = serializers.PrimaryKeyRelatedField(
        queryset=Subject_Level.objects.all(), allow_null=True)
    start_date = serializers.DateField()
    num_days = serializers.IntegerField(min_value=1, max_value=50, default=7)
    sheets_per_day = serializers.IntegerField(min_value=1, default=1)
    completion_time = serializers.IntegerField(min_value=1)
    type = serializers.CharField(max_length=50, allow_blank=True)

