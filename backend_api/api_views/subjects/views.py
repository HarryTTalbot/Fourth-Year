from rest_framework import viewsets
from rest_framework import filters
from rest_framework.response import Response
from rest_framework.decorators import action
from drf_spectacular.utils import extend_schema

from .models import *
from .serializers import *


class SubjectViewSet(viewsets.ModelViewSet):
    """
    Provides API functionality for viewing and editing subject and subject level information.
    """
    queryset = Subject.objects.all().order_by('name')
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']
    pagination_class = None

    serializer_class = SubjectSerializer
    serializer_classes = {
        'get_levels': SubjectGetLevelSerializer,
        'add_level': SubjectAddLevelSerializer,
        'remove_level': SubjectRemoveLevelSerializer
    }

    def get_serializer_class(self):
        return self.serializer_classes.get(self.action, self.serializer_class)

    @extend_schema(responses={200: SubjectGetLevelSerializer(many=True)})
    @action(methods=['get'], detail=True, name='Retrieve subject levels')
    def get_levels(self, request, pk=None):
        levels = Subject_Level.objects.filter(subject=self.get_object())
        serializer = self.get_serializer(instance=levels, many=True)
        return Response(serializer.data)

    @extend_schema(request=SubjectAddLevelSerializer, responses={200: None})
    @action(methods=['post'], detail=True, name='Add subject level')
    def add_level(self, request, pk=None):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        Subject_Level(subject=self.get_object(),
                      name=serializer.validated_data['name']).save()
        return Response(200)

    @extend_schema(request=SubjectRemoveLevelSerializer, responses={200: None})
    @action(methods=['post'], detail=True, name='Remove subject level')
    def remove_level(self, request, pk=None):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.validated_data['id'].delete()
        return Response(200)
