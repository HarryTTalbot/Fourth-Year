import datetime
import io

from django.shortcuts import render, redirect
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view, renderer_classes, authentication_classes, permission_classes
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer
from rest_framework import status
from rest_framework.views import APIView
from drf_spectacular.utils import extend_schema
from rest_framework.decorators import action, api_view
from drf_spectacular.types import OpenApiTypes

# Django imports to send a response to auto-download a file
from django.http import FileResponse
from django.http.response import HttpResponseBase

from .serializers import StudentRecordSheetSerializer

from backend_api.api_views.students.models import Student
from backend_api.api_views.subjects.models import Subject_Level

from . import make_report

# to have the returned PDF files download immediately instead of opening
# in a browser window, set as_attachment=True in the FileResponse
# constructor


class RecordSheetViewSet(viewsets.ViewSet):
    serializer_class = StudentRecordSheetSerializer
    serializer_classes = {
        'create_student_sheet': StudentRecordSheetSerializer
    }

    @extend_schema(request=StudentRecordSheetSerializer(many=False), responses={200: OpenApiTypes.BINARY})
    @action(methods=['post'], detail=False, name="New Record Sheet")
    def create_student_sheet(self, request):
        serializer = StudentRecordSheetSerializer(
            data=request.data, many=False)
        if serializer.is_valid():
            start_date = datetime.datetime.strptime(
                serializer.data["start_date"], "%Y-%m-%d").date()
            num_days = serializer.data["num_days"]

            sheets_per_day = serializer.data["sheets_per_day"]

            students = [Student.objects.get(
                pk=pk) for pk in serializer.data["student_id"]]

            if serializer.data["subject_level_id"] is None:
                subject_level = None
            else:
                subject_level = Subject_Level.objects.get(
                    pk=serializer.data["subject_level_id"])

            completion_time = serializer.data["completion_time"]

            record_sheet = make_report.get_record_sheet(
                start_date=start_date,
                num_days=num_days,
                sheets_per_day=sheets_per_day,
                students=students,
                subject_level=subject_level,
                completion_time=completion_time
            )
            buffer = io.BytesIO(record_sheet)

            response = FileResponse(
                buffer, filename="Record_Sheet.pdf", content_type='application/pdf')
            return response

        return Response(serializer.errors, status=400)
