from rest_framework import serializers

from django.contrib.auth.models import User
from rest_framework.fields import CharField
from backend_api.api_views.staff.models import Staff

# Serializer converts rows from model into JSON to be returned by API


class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password']


class AddAccountSerializer(serializers.Serializer):
    """ Serializer for creating a new account. """
    username = serializers.CharField(max_length=50)
    password = serializers.CharField(max_length=50)
    confirm_password = serializers.CharField(max_length=50)

    def validate(self, data):
        # Check whether the passwords match
        if data['password'] != data['confirm_password']:
            raise serializers.ValidationError(
                {"confirm_password": "Passwords do not match"})

        # Check if the username is already in use
        if len(User.objects.filter(username=data['username'])) != 0:
            raise serializers.ValidationError(
                {"username": "Username is already in use"})

        return data


class AddAdminAccountSerializer(serializers.ModelSerializer):
    username = CharField()
    password = CharField()
    confirm_password = CharField()
    passcode = CharField()
    confirm_passcode = CharField()

    class Meta:
        model = Staff
        fields = ['first_name', 'middle_name',
                  'last_name', 'job_title', 'username',
                  'password', 'confirm_password',
                  'passcode', 'confirm_passcode']


class EditPasswordSerializer(serializers.Serializer):
    """ Serializer for editing your password. """
    old_password = serializers.CharField(max_length=50)
    new_password = serializers.CharField(max_length=50)
    confirm_new_password = serializers.CharField(max_length=50)

    def validate(self, data):
        # Check that the new passwords match
        if data['new_password'] != data['confirm_new_password']:
            raise serializers.ValidationError(
                {"confirm_new_password": "Passwords do not match"})

        return data


class SetPasswordSerializer(serializers.Serializer):
    """ Serializer for the admin to set a password for an account. """
    staff_id = serializers.PrimaryKeyRelatedField(
        queryset=Staff.objects.all())
    new_password = serializers.CharField(max_length=50)
    confirm_new_password = serializers.CharField(max_length=50)

    def validate(self, data):
        # Check that the new passwords match
        if data['new_password'] != data['confirm_new_password']:
            raise serializers.ValidationError(
                {"confirm_new_password": "Passwords do not match"})

        return data


class ForgotAdminPasswordSerializer(serializers.Serializer):
    """ Serializer for setting a new admin password. """
    passcode = serializers.CharField(max_length=50)
    new_password = serializers.CharField(max_length=50)
    confirm_new_password = serializers.CharField(max_length=50)

    def validate(self, data):
        # Check that the new passwords match
        if data['new_password'] != data['confirm_new_password']:
            raise serializers.ValidationError(
                {"confirm_new_password": "Passwords do not match"})

        return data
