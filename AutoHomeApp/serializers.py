from rest_framework import serializers
from django.contrib.auth.models import User
from AutoHomeApp.models import *


class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'phone']


class MarkaSerializers(serializers.ModelSerializer):
    class Meta:
        model = Marka
        fields = '__all__'


class ModelAutoSerializers(serializers.ModelSerializer):
    marka = MarkaSerializers(many=False)

    class Meta:
        model = ModelAuto
        fields = '__all__'


class CreateModelAutoSerializers(serializers.ModelSerializer):
    class Meta:
        model = ModelAuto
        fields = '__all__'


class SoldCarsSerializers(serializers.ModelSerializer):
    user = UserSerializers(many=False)
    models = ModelAutoSerializers(many=False)

    class Meta:
        model = SoldCars
        fields = '__all__'


class CreateSoldCarsSerializers(serializers.ModelSerializer):
    class Meta:
        model = SoldCars
        fields = '__all__'


class InquirySerializers(serializers.ModelSerializer):
    user = UserSerializers(many=False)
    models = ModelAutoSerializers(many=False)

    class Meta:
        model = Inquiry
        fields = '__all__'


class CreateInquirySerializers(serializers.ModelSerializer):
    class Meta:
        model = Inquiry
        fields = '__all__'


class TestDriveSerializers(serializers.ModelSerializer):
    user = UserSerializers(many=False)
    models = ModelAutoSerializers(many=False)

    class Meta:
        model = TestDrive
        fields = '__all__'


class CreateTestDriveSerializers(serializers.ModelSerializer):
    class Meta:
        model = TestDrive
        fields = '__all__'


class ServiceSerializers(serializers.ModelSerializer):
    user = UserSerializers(many=False)
    models = ModelAutoSerializers(many=False)

    class Meta:
        model = Service
        fields = '__all__'


class CreateServiceSerializers(serializers.ModelSerializer):
    class Meta:
        model = TestDrive
        fields = '__all__'
