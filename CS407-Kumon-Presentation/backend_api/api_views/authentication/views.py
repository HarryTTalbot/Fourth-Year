from django.shortcuts import render, redirect
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view, renderer_classes, authentication_classes, permission_classes
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.permissions import IsAuthenticated
from drf_spectacular.utils import extend_schema
from rest_framework.decorators import action, api_view
from django.contrib.auth.hashers import make_password, check_password, is_password_usable

from django.contrib.auth.models import User
from backend_api.api_views.staff.models import Staff
from .serializers import *
from backend_api.api_views.staff.serializers import StaffSerializer


class UserViewSet(viewsets.ViewSet):
    permission_classes = ()
    serializer_class = AuthTokenSerializer
    serializer_classes = {
        'login': AuthTokenSerializer,
        'new_account': AddAccountSerializer,
    }

    @extend_schema(responses={200: AuthTokenSerializer()})
    @ action(methods=['post'], detail=False, name="Login")
    def login(self, request):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({'token': token.key})

    @extend_schema(responses={200: StaffSerializer(many=False)})
    @ action(methods=['get'], detail=False, name="Get Logged In Staff Details")
    def get_logged_in_staff(self, request):
        user = request.user

        try:
            staff = Staff.objects.get(user_id=user.id)

            serializer = StaffSerializer(
                instance=staff, many=False)
            return Response(serializer.data, 200)
        except:
            return Response("Staff Object not found", 404)

    @extend_schema(request=AddAccountSerializer(many=False), responses={200: None})
    @ action(methods=['post'], detail=False, name="New Account")
    def new_account(self, request):
        # Check it is the admin which has sent the request
        if request.user.is_superuser == False:
            return Response('Must be Admin', status=403)
            
        serializer = AddAccountSerializer(
            data=request.data, many=False)
        if serializer.is_valid():
            account = User.objects.create_user(username=serializer.validated_data['username'],
                                               password=serializer.validated_data['password'])
            account.save()
            return Response(status=200)
        return Response(serializer.errors, status=400)

    @extend_schema(request=EditPasswordSerializer(many=False), responses={200: None})
    @ action(methods=['post'], detail=False, name="Edit Password")
    def edit_password(self, request):
        serializer = EditPasswordSerializer(
            data=request.data, many=False)
        if serializer.is_valid():
            # Get the user account
            account = request.user

            # Check if the old password given is correct
            if account.check_password(serializer.validated_data['old_password']) == False:
                return Response("Old password is incorrect!", status=400)

            account.set_password(serializer.validated_data['new_password'])
            account.save()
            return Response(status=200)

        return Response(serializer.errors, status=400)

    @extend_schema(request=SetPasswordSerializer(many=False), responses={200: None})
    @ action(methods=['post'], detail=False, name="Admin Set Password")
    def admin_set_password(self, request):
        # Check it is the admin which has sent the request
        if request.user.is_superuser == False:
            return Response('Must be Admin', status=403)

        serializer = SetPasswordSerializer(
            data=request.data, many=False)
        if serializer.is_valid():
            # Find the account
            try:
                account = serializer.validated_data['staff_id'].user
            except:
                return Response('User account not found', status=400)

            account.set_password(serializer.validated_data['new_password'])
            account.save()
            return Response(status=200)

        return Response(serializer.errors, status=400)

    @extend_schema(request=ForgotAdminPasswordSerializer(many=False), responses={200: None})
    @ action(methods=['post'], detail=False, name="Admin Forgot Password")
    def admin_forgot_password(self, request):
        serializer = ForgotAdminPasswordSerializer(
            data=request.data, many=False)

        if serializer.is_valid():
            # Find the admin account
            try:
                account = User.objects.get(is_superuser=True)
                staff = Staff.objects.get(user=account)
            except:
                return Response('Admin account not found', status=404)

            # Check whether the passcode matches
            if check_password(serializer.validated_data['passcode'], staff.passcode) == False:
                return Response('Invalid Passcode', status=400)

            account.set_password(serializer.validated_data['new_password'])
            account.save()
            return Response(status=200)

        return Response(serializer.errors, status=400)

    @extend_schema(request=AddAdminAccountSerializer(many=False), responses={200: None})
    @ action(methods=['post'], detail=False, name="New Admin Account", permission_classes=[])
    def new_admin_account(self, request):
        # Check if the database is empty
        if len(Staff.objects.all()) != 0:
            return Response("Database is not empty", status=status.HTTP_400_BAD_REQUEST)

        serializer = AddAdminAccountSerializer(
            data=request.data, many=False)
        if serializer.is_valid():
            # Check whether the two passwords are the same
            if serializer.validated_data['password'] != serializer.validated_data['confirm_password']:
                return Response("Passwords don't match", status=400)

            # Check whether the two passcodes are the same
            if serializer.validated_data['passcode'] != serializer.validated_data['confirm_passcode']:
                return Response("Passcodes don't match", status=400)

            # Create the hashed passcide
            hashedCode = make_password(serializer.validated_data['passcode'])

            account = User.objects.create_superuser(username=serializer.validated_data['username'],
                                                    password=serializer.validated_data['password'])
            try:
                account.save()
            except:
                return Response("Could not create Account", status=400)

            # Create the staff account
            staff = Staff(first_name=serializer.validated_data['first_name'],
                          middle_name=serializer.validated_data['middle_name'],
                          last_name=serializer.validated_data['last_name'],
                          job_title=serializer.validated_data['job_title'],
                          user=account,
                          passcode=hashedCode)

            try:
                staff.save()
            except:
                return Response("Could not create Staff Member", status=400)

            return Response(status=200)
        return Response(serializer.errors, status=400)

    @extend_schema(responses={200: None})
    @ action(methods=['get'], detail=False, name="Is Setup", permission_classes=[])
    def is_setup(self, request):
        if len(Staff.objects.all()) != 0:
            return Response("The database is setup", status=200)
        else:
            return Response("The database is not setup", status=400)
