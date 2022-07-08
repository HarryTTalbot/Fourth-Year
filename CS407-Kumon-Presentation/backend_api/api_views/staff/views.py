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

from .serializers import *

from backend_api.views import MakeGDPRDeletable

from backend_api.api_views.reporting import get_staff_data_report


@MakeGDPRDeletable
class StaffViewSet(viewsets.ModelViewSet):
    """
    Provides API functionality for viewing and editing staff information.
    """
    queryset = Staff.objects.all().order_by('last_name')
    filter_backends = [filters.SearchFilter]
    search_fields = ['first_name', 'last_name', 'job_title']

    serializer_class = StaffSerializer
    serializer_classes = {
        'create': StaffCreateSerializer,
    }

    def get_serializer_class(self):
        return self.serializer_classes.get(self.action, self.serializer_class)

    @extend_schema(responses={200: OpenApiTypes.BINARY})
    @action(methods=["get"], detail=True, name="Get all of a staff member's data")
    def get_data(self, request, pk=None) -> FileResponse:
        """Returns a summary of all of the data stored about a staff member in PDF format"""

        staff = self.get_object()
        report = get_staff_data_report(staff)

        buffer = io.BytesIO(report)

        return FileResponse(buffer, filename="gdpr-report.pdf", content_type='application/pdf')

    @extend_schema(request=StaffCreateSerializer(many=False))
    def create(self, request):
        serializer = StaffCreateSerializer(
            data=request.data, many=False)
        if serializer.is_valid():
            try:
                account = User.objects.get(
                    username=serializer.validated_data['username'])
            except:
                return Response(status=400)
            staff = Staff(first_name=serializer.validated_data['first_name'],
                          middle_name=serializer.validated_data['middle_name'],
                          last_name=serializer.validated_data['last_name'],
                          job_title=serializer.validated_data['job_title'],
                          join_date=serializer.validated_data['join_date'],
                          leave_date=serializer.validated_data['leave_date'],
                          user=account)
            try:
                staff.save()

                response = StaffSerializer(
                    instance=staff, many=False)
                return Response(response.data, status=201)
            except:
                return Response(status=400)
        return Response(status=400)
