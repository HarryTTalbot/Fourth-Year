from rest_framework import serializers

from .models import *
from backend_api.api_views.students.serializers import AddressSerializer


class CenterDetailsSerializer(serializers.ModelSerializer):
    address = AddressSerializer()

    class Meta:
        model = CenterDetails
        fields = ['name', 'phone_number', 'address']
