from rest_framework import viewsets
from rest_framework import filters
from rest_framework.response import Response
from rest_framework.decorators import action
from drf_spectacular.utils import extend_schema

from .models import *
from backend_api.api_views.students.models import Student

from .serializers import *
from backend_api.api_views.students.serializers import StudentListSerializer

from backend_api.api_views.students.views import StudentViewSet



class ClassViewSet(viewsets.ModelViewSet):
    '''
    Provides API functionality for viewing and editing class information.
    '''
    queryset = Class.objects.all().order_by('name')
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']

    serializer_class = ClassSerializer
    serializer_classes = {
        'get_students': StudentListSerializer,
        'get_students_not_in_class': StudentListSerializer,
        'add_students': ClassStudentsSerializer,
        'remove_students': ClassStudentsSerializer,
        'set_students': ClassStudentsSerializer,
    }

    def get_serializer_class(self):
        return self.serializer_classes.get(self.action, self.serializer_class)

    def filter_queryset(self, queryset):
        if self.action in ['list']:
            return super().filter_queryset(queryset)
        return queryset

    @extend_schema(responses={200: StudentListSerializer(many=True)})
    @action(methods=['get'], detail=True, name='Retrieve class students', pagination_class=None)
    def get_students(self, request, pk=None):
        ''' Gets the students in the specified class. '''
        students = Student.objects.filter(
            class_students__class_fk=self.get_object())
        serializer = self.get_serializer(
            instance=students, many=True, read_only=True)
        return Response(serializer.data)

    @extend_schema(responses={200: StudentListSerializer(many=True)})
    @action(methods=['get'], detail=True, name='Retrieve non-class students')
    def get_students_not_in_class(self, request, pk=None):
        ''' Gets the students who are not in the specified class. '''
        students = Student.objects.exclude(
            class_students__class_fk=self.get_object()).order_by('id')
        page = self.paginate_queryset(filters.SearchFilter().filter_queryset(request, students, StudentViewSet))
        if page is not None:
            serializer = self.get_serializer(
                instance=page, many=True, read_only=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(
            instance=page, many=True, read_only=True)
        return self.get_paginated_response(serializer.data)

    @extend_schema(operation_id='classes_add_students', request=ClassStudentsSerializer(many=True), responses={200: None})
    @action(methods=['post'], detail=True, name='Add class students')
    def add_students(self, request, pk=None):
        ''' Adds the given students to the specified class. '''
        serializer = self.get_serializer(data=request.data, many=True)
        serializer.is_valid(raise_exception=True)
        for s in serializer.validated_data:
            Class_Student.objects.get_or_create(
                class_fk=self.get_object(), student=s['student_id'])
        return Response(status=200)

    @extend_schema(operation_id='classes_remove_students', request=ClassStudentsSerializer(many=True), responses={200: None})
    @action(methods=['post'], detail=True, name='Remove class students')
    def remove_students(self, request, pk=None):
        ''' Removes the given students from the specified class. '''
        serializer = self.get_serializer(
            data=request.data, many=True)
        serializer.is_valid(raise_exception=True)
        for s in serializer.validated_data:
            Class_Student.objects.filter(
                class_fk=self.get_object(), student=s['student_id']
            ).delete()
        return Response(status=200)

    @extend_schema(operation_id='classes_set_students', request=ClassStudentsSerializer(many=True), responses={200: None})
    @action(methods=['post'], detail=True, name='Set class students')
    def set_students(self, request, pk=None):
        ''' Sets the students for the specified class. '''
        serializer = self.get_serializer(
            data=request.data, many=True)
        serializer.is_valid(raise_exception=True)

        # Add students who are not already in the class
        for s in serializer.validated_data:
            Class_Student.objects.get_or_create(
                class_fk=self.get_object(), student=s['student_id'])

        # Remove students who are no longer in the class
        ids = [s['student_id'] for s in serializer.validated_data]
        Class_Student.objects.filter(class_fk=self.get_object()).exclude(
            student__in=ids).delete()

        return Response(status=200)
