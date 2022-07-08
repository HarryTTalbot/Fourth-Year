from rest_framework import serializers
from rest_framework.fields import SerializerMethodField
from drf_spectacular.utils import extend_schema_field


from .models import Attendance, Lesson, LongTermAbsence, ATTENDANCE_TYPES
from backend_api.api_views.students.models import Student

import backend_api.api_views.classes.serializers as classes_serializers
import backend_api.api_views.students.serializers as student_serializers
import backend_api.api_views.subjects.serializers as subjects_serializers


class LessonViewSerializer(serializers.ModelSerializer):
    class_fk = classes_serializers.ClassSerializer()
    subject_level = subjects_serializers.SubjectGetLevelSerializer()
    subject = SerializerMethodField()

    class Meta:
        model = Lesson
        fields = ['id', 'start_datetime', 'end_datetime',
                  'class_fk', 'subject', 'subject_level', 'created_at', 'last_modified_at']

    @extend_schema_field(subjects_serializers.SubjectSerializer)
    def get_subject(self, obj):
        try:
            return subjects_serializers.SubjectSerializer(instance=obj.subject_level.subject).data
        # If subject level has been deleted, return none
        except AttributeError:
            return None


class LessonEditSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = ['id', 'start_datetime', 'end_datetime',
                  'class_fk', 'subject_level']
        # While these fields can be null on the database side, they must be provided when creating new instances
        extra_kwargs = {'class_fk': {'required': True, 'allow_null': False},
                        'subject_level': {'required': True, 'allow_null': False}}


class LessonGetAttendanceSerializer(serializers.ModelSerializer):
    student = student_serializers.StudentListSerializer()

    class Meta:
        model = Attendance
        fields = ['student', 'status', 'last_modified_at']


class LessonSetAttendanceSerializer(serializers.Serializer):
    student = serializers.PrimaryKeyRelatedField(
        queryset=Student.objects.all())
    status = serializers.ChoiceField(choices=ATTENDANCE_TYPES)


class LongTermAbsenceViewSerializer(serializers.ModelSerializer):
    student = student_serializers.StudentSerializer()

    class Meta:
        model = LongTermAbsence
        fields = ['id', 'student', 'start_date', 'end_date', 'reason']


class LongTermAbsenceEditSerializer(serializers.ModelSerializer):
    class Meta:
        model = LongTermAbsence
        fields = ['id', 'student', 'start_date', 'end_date', 'reason']


class StudentGetAttendanceSerializer(serializers.ModelSerializer):
    """ Serializer for retrieving student attendance records. """
    lesson = LessonViewSerializer()

    class Meta:
        model = Attendance
        fields = ['lesson', 'status']
