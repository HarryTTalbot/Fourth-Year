from rest_framework import serializers

from .models import Subject, Subject_Level


class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = ['id', 'name']


class SubjectGetLevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject_Level
        fields = ['id', 'name']


class SubjectAddLevelSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=50)


class SubjectRemoveLevelSerializer(serializers.Serializer):
    id = serializers.PrimaryKeyRelatedField(
        queryset=Subject_Level.objects.all())
