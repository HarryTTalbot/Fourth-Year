from rest_framework import viewsets
from rest_framework import filters
from rest_framework.response import Response
from rest_framework.decorators import action
from drf_spectacular.utils import extend_schema
from drf_spectacular.types import OpenApiTypes
from django.http import FileResponse

import datetime
import io

from .models import *
from backend_api.api_views.students.models import Student

from .serializers import *

from backend_api.api_views.reporting import get_attendance_sheet


class LessonViewSet(viewsets.ModelViewSet):
    """
    Provides API functionality for viewing and editing lesson information.
    """
    queryset = Lesson.objects.all().order_by('-start_datetime')
    filter_backends = [filters.SearchFilter]
    search_fields = ['class_fk__name', 'subject_level__subject__name']

    serializer_class = LessonEditSerializer
    serializer_classes = {
        'retrieve': LessonViewSerializer,
        'list': LessonViewSerializer,
        'today': LessonViewSerializer,
        'past': LessonViewSerializer,
        'get_attendance': LessonGetAttendanceSerializer,
        'set_attendance': LessonSetAttendanceSerializer,
    }

    def get_serializer_class(self):
        return self.serializer_classes.get(self.action, self.serializer_class)

    @extend_schema(responses={200: LessonViewSerializer(many=True)})
    @action(methods=['get'], detail=False, name="Retrieve today's lessons", pagination_class=None)
    def today(self, request):
        today = datetime.datetime.today()
        tomorrow = today + datetime.timedelta(1)
        today_start = datetime.datetime.combine(
            today, datetime.time(), tzinfo=datetime.timezone.utc)
        today_end = datetime.datetime.combine(
            tomorrow, datetime.time(), tzinfo=datetime.timezone.utc)
        lessons_today = self.get_queryset().filter(
            start_datetime__gte=today_start, start_datetime__lt=today_end).order_by('start_datetime')
        serializer = self.get_serializer(instance=lessons_today, many=True)
        return Response(serializer.data)

    @extend_schema(responses={200: LessonViewSerializer(many=True)})
    @action(methods=['get'], detail=False, name="Retrieve previous's lessons")
    def past(self, request):
        today = datetime.datetime.combine(
            datetime.datetime.today(), datetime.time(), tzinfo=datetime.timezone.utc)
        lessons_past = self.get_queryset().filter(
            start_datetime__lt=today).order_by('-start_datetime')
        page = self.paginate_queryset(lessons_past)
        serializer = self.get_serializer(page, many=True)
        return self.get_paginated_response(serializer.data)

    @extend_schema(responses={200: LessonGetAttendanceSerializer(many=True)})
    @action(methods=['get'], detail=True, name='Retrieve lesson attendance', pagination_class=None)
    def get_attendance(self, request, pk=None):
        lesson = self.get_object()
        lesson_class_students = Student.objects.filter(
            class_students__class_fk=lesson.class_fk.id)

        # Create base attendance for class
        attendance = {}
        for s in lesson_class_students:
            absent = len(LongTermAbsence.objects.filter(
                student=s, start_date__lte=lesson.start_datetime.date(), end_date__gte=lesson.start_datetime.date())) > 0
            attendance[s] = Attendance(
                lesson=lesson, student=s, status='A' if absent else '')

        # Update with attendance data already in database
        for a in Attendance.objects.filter(lesson=lesson):
            attendance[a.student] = a

        serializer = self.get_serializer(
            instance=attendance.values(), many=True)
        return Response(serializer.data)

    @extend_schema(request=LessonSetAttendanceSerializer(many=True), responses={200: None})
    @action(methods=['post'], detail=True, name='Set lesson attendance')
    def set_attendance(self, request, pk=None):
        serializer = self.get_serializer(data=request.data, many=True)
        serializer.is_valid(raise_exception=True)
        for a in serializer.validated_data:
            values = {'lesson': self.get_object(),
                      'student': a['student'], 'status': a['status']}
            Attendance.objects.update_or_create(
                lesson=self.get_object(), student=a['student'], defaults=values)
        return Response(200)

    @extend_schema(responses={200: OpenApiTypes.BINARY})
    @action(methods=["get"], detail=True, name="Get a sheet for taking attendance on paper")
    def get_attendance_sheet(self, request, pk=None) -> FileResponse:
        """Returns a printable PDF for recording attendance"""

        lesson = self.get_object()
        report = get_attendance_sheet(lesson)

        buffer = io.BytesIO(report)

        return FileResponse(buffer, filename="attendance-sheet.pdf", content_type='application/pdf')


class LongTermAbsenceViewSet(viewsets.ModelViewSet):
    """
    Provides API functionality for viewing and editing student long term absences.
    """
    queryset = LongTermAbsence.objects.all().order_by('-last_modified_at')
    filter_backends = [filters.SearchFilter]
    search_fields = ['student__first_name', 'student__last_name']
    serializer_class = LongTermAbsenceEditSerializer
    serializer_classes = {
        'retrieve': LongTermAbsenceViewSerializer,
        'list': LongTermAbsenceViewSerializer,
    }

    def get_serializer_class(self):
        return self.serializer_classes.get(self.action, self.serializer_class)
