from rest_framework import serializers
from rest_framework.fields import SerializerMethodField
from drf_spectacular.utils import extend_schema_field
from drf_spectacular.types import OpenApiTypes

from .models import Class, Class_Student
from backend_api.api_views.students.models import Student


class ClassSerializer(serializers.ModelSerializer):
    size = SerializerMethodField()

    class Meta:
        model = Class
        fields = ['id', 'name', 'size']

    @extend_schema_field(OpenApiTypes.INT)
    def get_size(self, obj):
        ''' Returns the size of the class. '''
        return Class_Student.objects.filter(class_fk=obj).count()


class ClassStudentsSerializer(serializers.Serializer):
    ''' Serializer for managing class students. '''
    student_id = serializers.PrimaryKeyRelatedField(
        queryset=Student.objects.all())
