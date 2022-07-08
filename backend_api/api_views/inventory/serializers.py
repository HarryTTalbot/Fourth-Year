from rest_framework import serializers
from rest_framework.relations import PrimaryKeyRelatedField
from rest_framework.fields import IntegerField, SerializerMethodField
from drf_spectacular.utils import extend_schema_field
from drf_spectacular.types import OpenApiTypes
from django.db.models import Sum

from .models import BulkItem, BulkItemLog, Worksheet, WorksheetLog, LendableItem, ItemLoan, ItemLoanLog
from backend_api.api_views.staff.models import Staff

import backend_api.api_views.subjects.serializers as subjects_serializers


class BulkItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = BulkItem
        fields = ['id', 'name', 'quantity']


class BulkItemLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = BulkItemLog
        fields = ['staff_id', 'type', 'quantity', 'created_at']


class WorksheetViewSerializer(serializers.ModelSerializer):
    subject_level = subjects_serializers.SubjectGetLevelSerializer()
    subject = SerializerMethodField()

    class Meta:
        model = Worksheet
        fields = ['id', 'subject', 'subject_level', 'set', 'quantity']

    @extend_schema_field(subjects_serializers.SubjectSerializer)
    def get_subject(self, obj):
        try:
            return subjects_serializers.SubjectSerializer(instance=obj.subject_level.subject).data
        # If subject level has been deleted, return none
        except AttributeError:
            return None


class WorksheetEditSerializer(serializers.ModelSerializer):
    class Meta:
        model = Worksheet
        fields = ['id', 'subject_level', 'set', 'quantity']


class WorksheetLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorksheetLog
        fields = ['staff_id', 'type', 'quantity', 'created_at']


class ItemWithdrawSerializer(serializers.Serializer):
    staff_id = PrimaryKeyRelatedField(queryset=Staff.objects.all())
    quantity = IntegerField(min_value=1)

    def validate(self, attrs):
        if self.instance.quantity < attrs['quantity']:
            raise serializers.ValidationError(
                {'quantity': 'You cannot withdraw more items than are available.'})
        return attrs


class ItemRestockSerializer(serializers.Serializer):
    staff_id = PrimaryKeyRelatedField(queryset=Staff.objects.all())
    quantity = IntegerField(min_value=1)


class LendableItemViewSerializer(serializers.ModelSerializer):
    quantity_lent = SerializerMethodField()

    class Meta:
        model = LendableItem
        fields = ['id', 'name', 'quantity_available', 'quantity_lent']

    @extend_schema_field(OpenApiTypes.INT)
    def get_quantity_lent(self, obj):
        # Add up quantity lent of all ongoing loans
        return ItemLoan.objects.aggregate(
            Sum('quantity')).get('quantity__sum', 0)


class LendableItemEditSerializer(serializers.ModelSerializer):
    class Meta:
        model = LendableItem
        fields = ['id', 'name', 'quantity_available']


class ItemLoanSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemLoan
        fields = ['id', 'item_id', 'student_id', 'quantity', 'created_at']

    def validate(self, attrs):
        # Compare change in quantity being loaned to quantity available
        if self.instance:
            oldItem = self.instance.item_id
            newItem = attrs.get('item_id', oldItem)
            oldItem.quantity_available += self.instance.quantity
            newQuantity = newItem.quantity_available - \
                attrs.get('quantity', self.instance.quantity)
            oldItem.quantity_available -= self.instance.quantity
            if newQuantity < 0:
                raise serializers.ValidationError(
                    {'quantity': 'You cannot lend more items than are available.'})

        elif attrs['item_id'].quantity_available < attrs['quantity']:
            raise serializers.ValidationError(
                {'quantity': 'You cannot lend more items than are available.'})
        return attrs


class ReturnItemSerializer(serializers.Serializer):
    quantity = IntegerField(min_value=0)

    def validate(self, attrs):
        if attrs['quantity'] > self.instance.quantity:
            raise serializers.ValidationError(
                {'quantity': 'You cannot return more items than were loaned.'}
            )
        return attrs


class ItemLoanLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemLoanLog
        fields = ['id', 'item_id', 'student_id', 'quantity_lent',
                  'quantity_returned', 'loan_datetime', 'created_at']
