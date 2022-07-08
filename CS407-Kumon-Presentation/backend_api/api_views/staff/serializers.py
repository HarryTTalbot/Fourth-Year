from rest_framework import serializers
from drf_spectacular.utils import extend_schema_field
from drf_spectacular.types import OpenApiTypes

from .models import Staff


class StaffSerializer(serializers.ModelSerializer):
    # job_title = serializers.SlugRelatedField(
    #    read_only=True, slug_field='job_title')

    class Meta:
        model = Staff
        fields = ['id', 'first_name', 'middle_name',
                  'last_name', 'job_title', 'join_date', 'leave_date']


class StaffCreateSerializer(serializers.ModelSerializer):
    # job_title = serializers.SlugRelatedField(
    #    read_only=True, slug_field='job_title')
    username = serializers.CharField()

    class Meta:
        model = Staff
        fields = ['first_name', 'middle_name',
                  'last_name', 'job_title', 'username']


class StaffDeletedSerializer(serializers.ModelSerializer):
    """ Serializer for listing deleted students. """
    permanent_deletion_date = serializers.SerializerMethodField()

    class Meta:
        model = Staff
        fields = ['id', 'first_name', 'middle_name', 'last_name', 'job_title',
                  'deleted_at', 'permanent_deletion_date']

    @extend_schema_field(OpenApiTypes.DATETIME)
    def get_permanent_deletion_date(self, obj):
        return obj.deleted_at + obj.GDPR_RETENTION_PERIOD
