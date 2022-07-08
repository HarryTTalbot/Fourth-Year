from rest_framework import viewsets
from rest_framework import filters
from rest_framework.response import Response
from rest_framework.decorators import action
from drf_spectacular.utils import extend_schema
from django.http import HttpResponse

import datetime

from .models import *

from .serializers import *

from backend_api.api_views.reporting import get_record_sheet


class BulkItemViewSet(viewsets.ModelViewSet):
    """
    Provides API functionality for managing bulk item inventory.
    """
    queryset = BulkItem.objects.all().order_by('name')
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']

    serializer_class = BulkItemSerializer
    serializer_classes = {
        'withdraw': ItemWithdrawSerializer,
        'restock': ItemRestockSerializer,
        'history': BulkItemLogSerializer
    }

    def get_serializer_class(self):
        return self.serializer_classes.get(self.action, self.serializer_class)

    @extend_schema(request=ItemWithdrawSerializer, responses={200: None})
    @action(methods=['post'], detail=True, name='Withdraw bulk item')
    def withdraw(self, request, pk=None):
        serializer = self.get_serializer(
            data=request.data, instance=self.get_object())
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data
        item = self.get_object()
        item.quantity -= data['quantity']
        item.save()
        BulkItemLog(
            item_id=item, staff_id=data['staff_id'], type='W', quantity=data['quantity']).save()
        return Response(200)

    @extend_schema(request=ItemRestockSerializer, responses={200: None})
    @action(methods=['post'], detail=True, name='Restock bulk item')
    def restock(self, request, pk=None):
        serializer = self.get_serializer(
            data=request.data, instance=self.get_object())
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data
        item = self.get_object()
        item.quantity += data['quantity']
        item.save()
        BulkItemLog(
            item_id=item, staff_id=data['staff_id'], type='R', quantity=data['quantity']).save()
        return Response(200)

    @extend_schema(responses={200: BulkItemLogSerializer(many=True)})
    @action(methods=['get'], detail=True, name='Bulk item history')
    def history(self, request, pk=None):
        item = self.get_object()
        logs = BulkItemLog.objects.filter(
            item_id=item).order_by('-created_at')
        serializer = self.get_serializer(instance=logs, many=True)
        return Response(serializer.data)


class WorksheetViewSet(viewsets.ModelViewSet):
    """
    Provides API functionality for managing worksheet inventory.
    """
    queryset = Worksheet.objects.all().order_by('set')
    filter_backends = [filters.SearchFilter]
    search_fields = ['subject_level__subject__name', 'subject_level__name', 'set']

    serializer_class = WorksheetEditSerializer
    serializer_classes = {
        'retrieve': WorksheetViewSerializer,
        'list': WorksheetViewSerializer,
        'withdraw': ItemWithdrawSerializer,
        'restock': ItemRestockSerializer,
        'history': WorksheetLogSerializer
    }

    def get_serializer_class(self):
        return self.serializer_classes.get(self.action, self.serializer_class)

    @extend_schema(request=ItemWithdrawSerializer, responses={200: None})
    @action(methods=['post'], detail=True, name='Withdraw worksheet')
    def withdraw(self, request, pk=None):
        serializer = self.get_serializer(
            data=request.data, instance=self.get_object())
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data
        worksheet = self.get_object()
        worksheet.quantity -= data['quantity']
        worksheet.save()
        WorksheetLog(
            worksheet_id=worksheet, staff_id=data['staff_id'], type='W', quantity=data['quantity']).save()
        return Response(200)

    @extend_schema(request=ItemRestockSerializer, responses={200: None})
    @action(methods=['post'], detail=True, name='Restock worksheet')
    def restock(self, request, pk=None):
        serializer = self.get_serializer(
            data=request.data, instance=self.get_object())
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data
        worksheet = self.get_object()
        worksheet.quantity += data['quantity']
        worksheet.save()
        WorksheetLog(
            worksheet_id=worksheet, staff_id=data['staff_id'], type='R', quantity=data['quantity']).save()
        return Response(200)

    @extend_schema(responses={200: WorksheetLogSerializer(many=True)})
    @action(methods=['get'], detail=True, name='Worksheet history')
    def history(self, request, pk=None):
        worksheet = self.get_object()
        logs = WorksheetLog.objects.filter(
            worksheet_id=worksheet).order_by('-created_at')
        serializer = self.get_serializer(instance=logs, many=True)
        return Response(serializer.data)

    @action(methods=['get'], detail=False, name='Record sheet')
    def record_sheet(self, request, pk=None):

        rs = get_record_sheet(datetime.date.today())

        return HttpResponse(rs, content_type="application/pdf")


class LendableItemViewSet(viewsets.ModelViewSet):
    """
    Provides API functionality for managing lendable items.
    """
    queryset = LendableItem.objects.all().order_by('name')
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']

    serializer_class = LendableItemEditSerializer
    serializer_classes = {
        'retrieve': LendableItemViewSerializer,
        'list': LendableItemViewSerializer,
    }

    def get_serializer_class(self):
        return self.serializer_classes.get(self.action, self.serializer_class)


class ItemLoanViewSet(viewsets.ModelViewSet):
    """
    Provides API functionality for managing lending of lendable items.
    """
    queryset = ItemLoan.objects.all().order_by('-created_at')

    serializer_class = ItemLoanSerializer
    serializer_classes = {
        'return_item': ReturnItemSerializer,
        'history': ItemLoanLogSerializer,
    }

    def get_serializer_class(self):
        return self.serializer_classes.get(self.action, self.serializer_class)

    # Override perform_create to decrease item quantity available by loaned amount.
    def perform_create(self, serializer):
        item = serializer.validated_data['item_id']
        item.quantity_available -= serializer.validated_data['quantity']
        item.save()
        super().perform_create(serializer)

    # Override perform_update to change item quantity available to reflect changes to loan amount.
    def perform_update(self, serializer):
        oldItem = serializer.instance.item_id
        newItem = serializer.validated_data.get('item_id', oldItem)
        oldItem.quantity_available += serializer.instance.quantity
        newItem.quantity_available -= serializer.validated_data.get(
            'quantity', serializer.instance.quantity)
        oldItem.save()
        newItem.save()
        super().perform_update(serializer)

    # Override perform_destroy to re-add loaned items to total if a loan is deleted.
    def perform_destroy(self, instance):
        item = instance.item_id
        item.quantity_available += instance.quantity
        item.save()
        super().perform_destroy(instance)

    @extend_schema(request=ReturnItemSerializer, responses={200: None})
    @action(methods=['post'], detail=True, name="Return loaned items")
    def return_item(self, request, pk=None):
        loan = self.get_object()
        serializer = self.get_serializer(data=request.data, instance=loan)
        serializer.is_valid(raise_exception=True)
        quantity_returned = serializer.validated_data['quantity']
        ItemLoanLog(item_id=loan.item_id, student_id=loan.student_id, quantity_lent=loan.quantity,
                    quantity_returned=quantity_returned, loan_datetime=loan.created_at).save()
        item = loan.item_id
        item.quantity_available += quantity_returned
        item.save()
        loan.delete()
        return Response(200)

    @extend_schema(responses={200: ItemLoanLogSerializer(many=True)})
    @action(methods=['get'], detail=False, name='Lending history')
    def history(self, request, pk=None):
        loans = ItemLoanLog.objects.all().order_by('-created_at')
        serializer = self.get_serializer(instance=loans, many=True)
        return Response(serializer.data)
