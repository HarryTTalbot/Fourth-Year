from rest_framework import serializers
from drf_spectacular.utils import extend_schema_field
from drf_spectacular.types import OpenApiTypes


from .models import *


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ['line_one', 'line_two', 'line_three', 'city_town',
                  'province_district', 'post_code', 'country']

    def create(self, validated_data):
        return Address(**validated_data)


class StudentSerializer(serializers.ModelSerializer):
    address = AddressSerializer()

    class Meta:
        model = Student
        fields = ['id', 'k_sis_id', 'first_name', 'middle_name', 'last_name', 'date_of_birth',
                  'join_date', 'leave_date', 'phone_number', 'school', 'grade', 'address', 'email']

    # When a new student is created, use an exisiting matching address record or if one doesn't exist, or create one
    def create(self, validated_data):
        address_data = validated_data.pop('address')
        address, _ = Address.objects.get_or_create(**address_data)
        student = Student.objects.create(
            address=address, **validated_data)
        return student

    def update(self, instance, validated_data):
        # If address fields are specified, update those too
        if address_data := validated_data.pop('address', None):
            for a, v in address_data.items():
                setattr(instance.address, a, v)
            instance.address.save()
        for a, v in validated_data.items():
            setattr(instance, a, v)
        instance.save()
        return instance


class StudentListSerializer(serializers.ModelSerializer):
    """ Serializer for students which only includes their name and IDs. """
    class Meta:
        model = Student
        fields = ['id', 'k_sis_id', 'first_name', 'middle_name', 'last_name',
                  'date_of_birth', 'school', 'grade']


class StudentDeletedSerializer(serializers.ModelSerializer):
    """ Serializer for listing deleted students. """
    permanent_deletion_date = serializers.SerializerMethodField()

    class Meta:
        model = Student
        fields = ['id', 'k_sis_id', 'first_name', 'middle_name', 'last_name',
                  'date_of_birth', 'school', 'grade', 'deleted_at', 'permanent_deletion_date']

    @extend_schema_field(OpenApiTypes.DATETIME)
    def get_permanent_deletion_date(self, obj):
        return obj.deleted_at + obj.GDPR_RETENTION_PERIOD


class ContactSerializer(serializers.ModelSerializer):
    """ Serializer for contact details. """
    address = AddressSerializer()

    class Meta:
        model = Contact_Detail
        fields = ['id', 'first_name', 'middle_name', 'last_name',
                  'phone_home', 'phone_business', 'phone_mobile', 'email', 'address']

    # When a new contact is created, use an exisiting matching address record or if one doesn't exist, or create one
    def create(self, validated_data):
        address_data = validated_data.pop('address')
        address, created = Address.objects.get_or_create(**address_data)
        contact = Contact_Detail.objects.create(
            address=address, **validated_data)
        return contact

    def update(self, instance, validated_data):
        # If address fields are specified, update those too
        if address_data := validated_data.pop('address', None):
            for a, v in address_data.items():
                setattr(instance.address, a, v)
            instance.address.save()
        for a, v in validated_data.items():
            setattr(instance, a, v)
        instance.save()
        return instance


class ContactListSerializer(serializers.ModelSerializer):
    """ Serializer for contact details which only includes ID and name. """
    class Meta:
        model = Contact_Detail
        fields = ['id', 'first_name', 'middle_name', 'last_name', 'email']


class StudentGetContactsSerializer(serializers.ModelSerializer):
    """ Serializer for retrieving student contact relations """
    contact_id = ContactListSerializer()

    class Meta:
        model = Student_Contact
        fields = ['contact_id', 'relationship']


class StudentAddContactsSerializer(serializers.Serializer):
    """ Serializer for adding contacts to a student. """
    contact_id = serializers.PrimaryKeyRelatedField(
        queryset=Contact_Detail.objects.all())
    relationship = serializers.CharField(max_length=50)

    def validate(self, attrs):
        if Student_Contact.objects.filter(student_id=self.instance, contact_id=attrs['contact_id']).exists():
            raise serializers.ValidationError(
                {'contact_id': 'This contact is already assigned to this student.'}
            )
        return attrs


class StudentRemoveContactsSerializer(serializers.Serializer):
    """ Serializer for removing contacts from a student. """
    contact_id = serializers.PrimaryKeyRelatedField(
        queryset=Contact_Detail.objects.all())

    def validate(self, attrs):
        if not Student_Contact.objects.filter(student_id=self.instance, contact_id=attrs['contact_id']).exists():
            raise serializers.ValidationError(
                {'contact_id': 'This contact is not assigned to this student.'}
            )
        return attrs


class ContactGetStudentsSerializer(serializers.ModelSerializer):
    student_id = StudentListSerializer()

    class Meta:
        model = Student_Contact
        fields = ['student_id', 'relationship']
