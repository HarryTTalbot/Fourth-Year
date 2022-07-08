
'''
Contains the views for the import and export endpoints.
'''

import os

# Rest Framework
from django.core.files.storage import FileSystemStorage
from django.http.response import FileResponse, HttpResponseBase
from drf_spectacular.types import OpenApiTypes
from drf_spectacular.utils import extend_schema
from rest_framework import status
from rest_framework.decorators import action, permission_classes, authentication_classes
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from rest_framework.permissions import IsAuthenticated, AllowAny
# File Storage Locations
from django.conf import settings

# Business Logic
from . import full, import_k_sis
from backend_api.models import File
from backend_api.api_views.staff.models import Staff
from backend_api.serializers import FileSerializer


class ExportViewSet(GenericViewSet):
    '''
    Provides API functionality for exporting data to a backup file.
    '''
    @extend_schema(parameters=None, responses={200: OpenApiTypes.BINARY})
    def list(self, request) -> HttpResponseBase:
        ''' Exports the database contents to a backup file. '''
        return full.export_full()


class ImportViewSet(GenericViewSet):
    '''
    Provides API functionality for importing data from either K-SIS or a backup.
    '''
    serializer_class = FileSerializer
    queryset = File.objects.all()
    pagination_class = None

    @extend_schema(
        request={'multipart/form-data': FileSerializer},
        responses={201: FileSerializer}
    )
    def create(self, request) -> HttpResponseBase:
        ''' Imports data from either a K-SIS export or an existing backup file. '''
        # Ensure import type is correct
        if request.data["type"] not in ["k_sis", "dumps"]:
            return Response(f"Invalid import type \'{request.data['type']}\'",
                            status=status.HTTP_400_BAD_REQUEST)

        # Create the directory to store the file if it doesn't already exist
        if not os.path.exists(settings.KSIS_ROOT):
            os.makedirs(settings.KSIS_ROOT)
        if not os.path.exists(settings.DUMP_IMPORT_ROOT):
            os.makedirs(settings.DUMP_IMPORT_ROOT)

        # Check that the input parameters are valid
        check = FileSerializer(data=request.data)
        check.is_valid(raise_exception=True)

        # Save the file to the system storage
        if request.data["type"] == "dumps":
            path = os.path.join(
                settings.DUMP_IMPORT_ROOT, check.validated_data["file"].name)
        else:
            path = os.path.join(settings.KSIS_ROOT,
                                check.validated_data["file"].name)

        file_storage = FileSystemStorage()
        filename = file_storage.save(path, check.validated_data["file"])

        # Save the input parameters
        file = File(
            name=check.validated_data["name"],
            type=check.validated_data["type"],
            file=filename)
        file.save()

        # Import the contents of the file into the database
        if request.data["type"] == "dumps":
            success, message = full.import_full(file.file.path)
        elif request.data["type"] == "k_sis":
            success, message = import_k_sis.import_k_sis(file.file.path)

        # Return a response based on the success of reading the contents of the file
        if success:
            return Response(message, status=status.HTTP_201_CREATED)

        # If unsuccessful, the file and File object needs to be removed from the storage
        file.delete()
        file_storage.delete(filename)

        return Response(message, status=status.HTTP_400_BAD_REQUEST)

    @extend_schema(
        responses={201: FileSerializer}
    )
    def list(self, request) -> HttpResponseBase:
        ''' Lists all of the imports that were previously performed on this database. '''
        imports = File.objects.all()
        serializer = FileSerializer(instance=imports, many=True)
        return Response(serializer.data)

    @extend_schema(
        responses={200: OpenApiTypes.BINARY}
    )
    @action(methods=['get'], detail=True, name='Download Import File')
    def download(self, request, pk=None) -> HttpResponseBase:
        ''' Downloads the import file associated with the given import ID. '''
        existing_import = self.get_object()

        file_storage = FileSystemStorage()
        response = FileResponse(file_storage.open(
            existing_import.file.path, 'rb'), content_type='application/force-download')

        basename = os.path.basename(existing_import.file.path)
        response['Content-Disposition'] = f'attachment; filename="{basename}"'

        return response

    @extend_schema(
        request={'multipart/form-data': FileSerializer},
        responses={201: FileSerializer}
    )
    @ action(methods=['post'], detail=False, name="Import From Scratch", permission_classes=[])
    def first_import(self, request) -> HttpResponseBase:
        ''' Imports data from  an existing backup file. '''
        # Check whether the database is empty
        if len(Staff.objects.all()) != 0:
            return Response("Database is not empty", status=status.HTTP_400_BAD_REQUEST)

        # Create the directory to store the file if it doesn't already exist
        if not os.path.exists(settings.DUMP_IMPORT_ROOT):
            os.makedirs(settings.DUMP_IMPORT_ROOT)

        # Check that the input parameters are valid
        check = FileSerializer(data=request.data)
        check.is_valid(raise_exception=True)

        # Save the file to the system storage
        

        file_storage = FileSystemStorage(location = settings.DUMP_IMPORT_ROOT)
        filename = file_storage.save(check.validated_data["file"].name, check.validated_data["file"])

        path = os.path.join(
            settings.DUMP_IMPORT_ROOT, filename)

        # Save the input parameters
        file = File(
            name=check.validated_data["name"],
            type="dumps",
            file=filename)
        file.save()

        # Import the contents of the file into the database
        success, message = full.import_full(path)

        # Return a response based on the success of reading the contents of the file
        if success:
            return Response(message, status=status.HTTP_201_CREATED)

        # If unsuccessful, the file and File object needs to be removed from the storage
        file.delete()
        file_storage.delete(filename)

        return Response(message, status=status.HTTP_400_BAD_REQUEST)
