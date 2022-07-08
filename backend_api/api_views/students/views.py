import io

from rest_framework import viewsets
from rest_framework import filters
from rest_framework.response import Response
from rest_framework.decorators import action
from drf_spectacular.utils import extend_schema
from drf_spectacular.types import OpenApiTypes
from django.http import FileResponse
import io

from .models import *
from backend_api.api_views.classes.models import Class
from backend_api.api_views.attendance.models import Attendance, Lesson

from .serializers import *
from backend_api.api_views.classes.serializers import ClassSerializer
from backend_api.api_views.attendance.serializers import LessonViewSerializer, StudentGetAttendanceSerializer

from backend_api.api_views.reporting import get_student_data_report

from backend_api.views import MakeGDPRDeletable


@MakeGDPRDeletable
class StudentViewSet(viewsets.ModelViewSet):
    """
    Provides API functionality for viewing and editing student information.
    """
    queryset = Student.objects.all().order_by('last_name')
    filter_backends = [filters.SearchFilter]
    search_fields = ['first_name', 'last_name']

    serializer_class = StudentSerializer
    serializer_classes = {
        'list': StudentListSerializer,
        'get_classes': ClassSerializer,
        'get_contacts': StudentGetContactsSerializer,
        'add_contacts': StudentAddContactsSerializer,
        'remove_contacts': StudentRemoveContactsSerializer,
        'get_lessons': LessonViewSerializer,
        'get_attendance': StudentGetAttendanceSerializer,
    }

    def get_serializer_class(self):
        return self.serializer_classes.get(self.action, self.serializer_class)

    @extend_schema(responses={200: ClassSerializer(many=True)})
    @action(methods=['get'], detail=True,
            name='Retrieve student classes', pagination_class=None)
    def get_classes(self, request, pk=None):
        """ Retrieves classes for the specified student belongs to. """
        student = self.get_object()
        classes = Class.objects.filter(
            student_classes__student=student)
        serializer = self.get_serializer(
            instance=classes, many=True, read_only=True)
        return Response(serializer.data)

    @extend_schema(responses={200: StudentGetContactsSerializer(many=True)})
    @action(methods=['get'], detail=True,
            name='Retrieve student contacts', pagination_class=None)
    def get_contacts(self, request, pk=None):
        """ Retrieves the contacts for the specified student. """
        student_contacts = Student_Contact.objects.filter(
            student_id=self.get_object())
        serializer = self.get_serializer(
            instance=student_contacts, many=True)
        return Response(serializer.data)

    @extend_schema(request=StudentAddContactsSerializer(many=True), responses={200: None})
    @action(methods=['post'], detail=True,
            name='Add student contacts')
    def add_contacts(self, request, pk=None):
        """ Adds the given contacts to the specified student. """
        student = self.get_object()
        serializer = self.get_serializer(
            data=request.data, many=True, instance=student)
        serializer.is_valid(raise_exception=True)
        for c in serializer.validated_data:
            Student_Contact.objects.get_or_create(
                student_id=student, contact_id=c['contact_id'], relationship=c['relationship'])
        return Response(status=200)

    @extend_schema(request=StudentRemoveContactsSerializer(many=True), responses={200: None})
    @action(methods=['post'], detail=True,
            name='Remove student contacts')
    def remove_contacts(self, request, pk=None):
        """ Removes the given contacts from the specified student. """
        student = self.get_object()
        serializer = self.get_serializer(
            data=request.data, many=True, instance=student)
        serializer.is_valid(raise_exception=True)
        for c in serializer.validated_data:
            Student_Contact.objects.get(
                student_id=student, contact_id=c['contact_id']).delete()
        return Response(status=200)

    @extend_schema(responses={200: LessonViewSerializer(many=True)})
    @action(methods=['get'], detail=True, name='Retrieve student lessons')
    def get_lessons(self, request, pk=None):
        """ Retrieves the specified student's lessons. """
        student = self.get_object()
        student_classes = Class.objects.filter(
            student_classes__student=student)
        student_lessons = Lesson.objects.filter(
            class_fk__in=student_classes).order_by('start_datetime')
        serializer = self.get_serializer(instance=student_lessons, many=True)
        return Response(serializer.data)

    @extend_schema(responses={200: StudentGetAttendanceSerializer(many=True)})
    @action(methods=['get'], detail=True, name='Retrieve student addendance')
    def get_attendance(self, request, pk=None):
        """ Retrieves the lesson attendance record for the specified student. """
        student = self.get_object()
        student_classes = Class.objects.filter(
            student_classes__student=student)
        student_lessons = Lesson.objects.filter(
            class_fk__in=student_classes).order_by('start_datetime')
        recorded_lessons = {
            a.lesson: a for a in Attendance.objects.filter(student=student)}
        attendance = []
        for l in student_lessons:
            if l in recorded_lessons:
                attendance.append(recorded_lessons[l])
            else:
                attendance.append(Attendance(
                    lesson=l, student=student, status=''))

        serializer = self.get_serializer(instance=attendance, many=True)
        return Response(serializer.data)

    @extend_schema(responses={200: OpenApiTypes.BINARY})
    @action(methods=["get"], detail=True, name="Get all of a student's data")
    def get_data(self, request, pk=None) -> FileResponse:
        """Returns a summary of all of the data stored about a student in PDF format"""

        student = self.get_object()
        report = get_student_data_report(student)

        buffer = io.BytesIO(report)

        return FileResponse(buffer, filename="gdpr-report.pdf", content_type='application/pdf')


class ContactViewSet(viewsets.ModelViewSet):
    """
    Provides API functionality for viewing and editing student contacts information.
    """
    queryset = Contact_Detail.objects.all().order_by('last_name')
    filter_backends = [filters.SearchFilter]
    search_fields = ['first_name', 'last_name']

    serializer_class = ContactSerializer
    serializer_classes = {
        'list': ContactListSerializer,
        'get_students': ContactGetStudentsSerializer
    }

    def get_serializer_class(self):
        return self.serializer_classes.get(self.action, self.serializer_class)

    @extend_schema(responses={200: ContactGetStudentsSerializer(many=True)})
    @action(methods=['get'], detail=True,
            name='Retrieve contact students', pagination_class=None)
    def get_students(self, request, pk=None):
        """ Retrieves the students for the specified contact. """
        contact = self.get_object()
        student_contacts = Student_Contact.objects.filter(
            contact_id=contact)
        serializer = self.get_serializer(
            instance=student_contacts, many=True)
        return Response(serializer.data)
