from rest_framework import serializers
from django.contrib.auth.models import User
from AutoHomeApp.models import *


class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']


class CreateProfileSerializers(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'


class ProfileSerializers(serializers.ModelSerializer):
    user = UserSerializers(many=False)

    class Meta:
        model = Profile
        fields = '__all__'


class MarkaSerializers(serializers.ModelSerializer):
    class Meta:
        model = Marka
        fields = '__all__'


class ModelAutoSerializers(serializers.ModelSerializer):
    marka = MarkaSerializers

    class Meta:
        model = ModelAuto
        fields = '__all__'


class CreateModelAutoSerializers(serializers.ModelSerializer):
    class Meta:
        model = ModelAuto
        fields = '__all__'


class ReservSerializers(serializers.ModelSerializer):
    user = UserSerializers

    class Meta:
        model = Reserv
        fields = '__all__'


class CreateReservSerializers(serializers.ModelSerializer):
    class Meta:
        model = Reserv
        fields = '__all__'
