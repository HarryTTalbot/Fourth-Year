from typing import List
from rest_framework import serializers
from drf_spectacular.utils import extend_schema_field
from drf_spectacular.types import OpenApiTypes

from .models import File
from backend_api.api_views.students.serializers import AddressSerializer


class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = '__all__'


def createListDeletedSerializer(list_serializer):
    class ListDeletedSerializer(list_serializer):
        permanent_deletion_date = serializers.SerializerMethodField()

        class Meta(list_serializer.Meta):
            fields = list_serializer.Meta.fields + \
                ['deleted_at', 'permanent_deletion_date']

        @extend_schema_field(OpenApiTypes.DATETIME)
        def get_permanent_deletion_date(self, obj):
            return obj.deleted_at + obj.GDPR_RETENTION_PERIOD

    modelName = list_serializer.Meta.model.__name__
    ListDeletedSerializer.__name__ = f'{modelName}DeletedSerializer'
    ListDeletedSerializer.__doc__ = f' Serializer for listing gdpr deleted {modelName.lower()} instances. '
    return ListDeletedSerializer
