from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics, permissions, status
from rest_framework.exceptions import PermissionDenied

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from django.contrib.auth.models import User

from django.contrib.auth import authenticate, login

from AutoHomeApp.models import *
from AutoHomeApp.serializers import *



# Create your views here.

class Logout(APIView):

    def get(self, request):
        request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)


class UserUpdateView(generics.RetrieveUpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializers


class MarkasListView(generics.ListAPIView):
    queryset = Marka.objects.all()
    serializer_class = MarkaSerializers


class ModelAutoRetrieveView(generics.RetrieveAPIView):
    queryset = ModelAuto.objects.all()
    serializer_class = ModelAutoSerializers


class ModelAutoListView(generics.ListAPIView):
    queryset = ModelAuto.objects.all()
    serializer_class = ModelAutoSerializers


class SoldCarListView(generics.ListAPIView):
    queryset = SoldCars.objects.all()
    serializer_class = SoldCarsSerializers


class SoldCarCreateView(generics.CreateAPIView):
    queryset = SoldCars.objects.all()
    serializer_class = CreateSoldCarsSerializers


class SoldCarDestroyView(generics.DestroyAPIView):
    queryset = SoldCars.objects.all()
    serializer_class = CreateSoldCarsSerializers


class InquiryListView(generics.ListAPIView):
    queryset = Inquiry.objects.all()
    serializer_class = InquirySerializers


class InquiryCreateView(generics.CreateAPIView):
    queryset = Inquiry.objects.all()
    serializer_class = CreateInquirySerializers


class InquiryDestroyView(generics.DestroyAPIView):
    queryset = Inquiry.objects.all()
    serializer_class = CreateInquirySerializers


class TestDriveListView(generics.ListAPIView):
    queryset = TestDrive.objects.all()
    serializer_class = TestDriveSerializers


class TestDriveCreateView(generics.CreateAPIView):
    queryset = TestDrive.objects.all()
    serializer_class = CreateTestDriveSerializers


class TestDriveDestroyView(generics.DestroyAPIView):
    queryset = TestDrive.objects.all()
    serializer_class = CreateTestDriveSerializers


class ServiceListView(generics.ListAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializers


class ServiceCreateView(generics.CreateAPIView):
    queryset = Service.objects.all()
    serializer_class = CreateServiceSerializers


class ServiceDestroyView(generics.DestroyAPIView):
    queryset = Service.objects.all()
    serializer_class = CreateServiceSerializers
