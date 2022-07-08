from rest_framework.decorators import action, api_view
from rest_framework.response import Response
from drf_spectacular.utils import extend_schema
import datetime

from backend_api.api_views.staff.models import Staff
from backend_api.api_views.students.models import Student

from .serializers import createListDeletedSerializer


class GDPRDeletable():
    "doing it this way is very possibly a bad idea :-)"

    @action(methods=['delete'], detail=True, name='GDPR-compliant deletion')
    def gdpr_delete(self, request, pk=None):
        "Deletes records in a GDPR-compliant manner"
        staff = self.get_object()
        staff.deleted_at = datetime.datetime.now()
        staff.save()
        return Response(status=204)

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.action == 'list':
            return queryset.filter(deleted_at__isnull=True)
        elif self.action == 'list_deleted':
            return queryset.filter(deleted_at__isnull=False)
        return queryset

    @action(methods=['get'], detail=False, name='Get GDPR deleted', pagination_class=None)
    def list_deleted(self, request):
        results = self.get_queryset()
        serialized_results = self.get_serializer(instance=results, many=True)
        return Response(serialized_results.data)

    @extend_schema(request=None, responses={201: None})
    @action(methods=['post'], detail=True, name='Restore GDPR deleted object')
    def gdpr_restore(self, request, pk=None):
        instance = self.get_object()
        instance.deleted_at = None
        instance.save()
        return Response(201)


# Decorator to make a viewset GDPR deletetable.
# Automatically creates a list_deleted serializer and applies @extend_schema
# with the new serializer to the list_deleted method
def MakeGDPRDeletable(viewset):
    viewset.__bases__ = (GDPRDeletable, *viewset.__bases__)
    list_serializer = viewset.serializer_classes.get(
        'list', viewset.serializer_class)

    list_deleted_serializer = createListDeletedSerializer(list_serializer)
    viewset.serializer_classes['list_deleted'] = list_deleted_serializer

    viewset.list_deleted = extend_schema(request=None, responses={
        200: list_deleted_serializer(many=True)})(GDPRDeletable.list_deleted)

    return viewset


@api_view(("GET",))
def delete_expired(request):
    # mostly here to suppress Django's warning about naïve datetimes
    tz_offset = datetime.timedelta(hours=0)
    tz = datetime.timezone(tz_offset)
    now = datetime.datetime.now(tz=tz)

    Student.objects.filter(
        deleted_at__lt=now - Student.GDPR_RETENTION_PERIOD).delete()
    Staff.objects.filter(
        deleted_at__lt=now - Staff.GDPR_RETENTION_PERIOD).delete()
    return Response(status=204)
