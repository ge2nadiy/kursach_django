from rest_framework import serializers
from django.contrib.auth.models import User
from AutoHomeApp.models import *
from django.core.mail import send_mail


class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','username', 'first_name', 'last_name', 'email', 'phone']


class UpdateUserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'phone']

        def update(self, instance, validated_data):
            instance.username = validated_data['username']
            instance.first_name = validated_data['first_name']
            instance.last_name = validated_data['last_name']
            instance.email = validated_data['email']
            instance.phone = validated_data['phone']

            instance.save()

            return instance


class MarkaSerializers(serializers.ModelSerializer):
    class Meta:
        model = Marka
        fields = '__all__'


class ModelAutoSerializers(serializers.ModelSerializer):
    marka = MarkaSerializers(many=False)

    class Meta:
        model = ModelAuto
        fields = '__all__'


class UpdateModelAutoSerializers(serializers.ModelSerializer):
    class Meta:
        model = ModelAuto
        fields = ['model','body_type', 'power', 'engine_volume', 'number_of_gears', 'year_of_issue','price','logo']


class CreateModelAutoSerializers(serializers.ModelSerializer):
    class Meta:
        model = ModelAuto
        fields = '__all__'


class SoldCarsSerializers(serializers.ModelSerializer):
    user = UserSerializers(many=False)
    model = ModelAutoSerializers(many=False)

    class Meta:
        model = SoldCars
        fields = '__all__'


class CreateSoldCarsSerializers(serializers.ModelSerializer):

    def create(self, validated_data, ):
        print(validated_data['user'])
        user = User.objects.get(username=validated_data['user'])
        send_mail(
            'Заявка на покупку автомобиля.', #tema
            'Здравствуйте уважаемый ' + user.first_name + '. Ваша заявка на покупку автомобиля одобрена. Для уточнения можете связаться с нами: autohome228@gmail.com',
            'autohome228@gmail.com',
            [user.email],
            False
        )
        return super().create(validated_data=validated_data)

    class Meta:
        model = SoldCars
        fields = '__all__'


class InquirySerializers(serializers.ModelSerializer):
    user = UserSerializers(many=False)
    model = ModelAutoSerializers(many=False)

    class Meta:
        model = Inquiry
        fields = '__all__'


class CreateInquirySerializers(serializers.ModelSerializer):
    class Meta:
        model = Inquiry
        fields = '__all__'


class TestDriveSerializers(serializers.ModelSerializer):
    user = UserSerializers(many=False)
    model = ModelAutoSerializers(many=False)

    class Meta:
        model = TestDrive
        fields = '__all__'


class CreateTestDriveSerializers(serializers.ModelSerializer):
    def create(self, validated_data, ):
        print(validated_data['user'])
        user = User.objects.get(username=validated_data['user'])
        send_mail(
            'Заявка на тест-драйв.', #tema
            'Здравствуйте уважаемый ' + user.first_name + '! Ваша заявка на тест-драйв успешно оформлена. Подробную информацию Вы можете увидеть в Вашем личном кабинете на сайте. Для уточнения можете связаться с нами: autohome228@gmail.com',
            'autohome228@gmail.com',
            [user.email],
            False
        )
        return super().create(validated_data=validated_data)

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
        model = Service
        fields = '__all__'
