from django.db import models
from django.contrib.auth.models import User, AbstractUser


# Create your models here.
class User(AbstractUser):
    phone = models.CharField(max_length=30, verbose_name='Моб. номер')

    REQUIRED_FIELDS = ['first_name', 'last_name', 'phone']

    class Meta:
        verbose_name_plural = 'Данные пользователей'

    def __str__(self):
        return self.username


class Marka(models.Model):
    marka = models.CharField(max_length=20, verbose_name='Марка')
    description = models.TextField(verbose_name='Описание')
    logo = models.ImageField(upload_to='marka_logo/', blank=False)

    class Meta:
        verbose_name = 'Марка'
        verbose_name_plural = 'Марки'

    def __str__(self):
        return self.marka


class ModelAuto(models.Model):
    marka = models.ForeignKey(Marka, on_delete=models.CASCADE)
    model = models.CharField(max_length=30, verbose_name='Модель')
    body_type = models.CharField(max_length=20, verbose_name='Тип кузова')
    power = models.IntegerField(default=0, verbose_name='Мощность,л.с.')
    engine_volume = models.IntegerField(default=0, verbose_name='Объём двигателя,куб. см')
    number_of_gears = models.IntegerField(default=0, verbose_name='Количество передач')
    year_of_issue = models.IntegerField(default=0, verbose_name='Год выпуска')
    price = models.IntegerField(default=0, verbose_name='Цена')
    logo = models.ImageField(upload_to='model_logo/', blank=False)

    class Meta:
        verbose_name = 'Модель'
        verbose_name_plural = 'Модели'
        ordering = ['model']

    def __str__(self):
        return self.model


class SoldCars(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    model = models.ForeignKey(ModelAuto, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'Проданные авто'

    def __str__(self):
        return self.model.model


class Inquiry(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    model = models.ForeignKey(ModelAuto, on_delete=models.CASCADE)
    date_inquiry = models.DateField(null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Заявки'
        ordering = ['user']

    def __str__(self):
        return self.user.username


class TestDrive(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    model = models.ForeignKey(ModelAuto, on_delete=models.CASCADE)
    date_inquiry = models.DateField(null=True, verbose_name='Дата тест-драйва')

    class Meta:
        verbose_name_plural = 'Тест-драйв'
        ordering = ['user']

    def __str__(self):
        return self.user.username


class Service(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    model = models.ForeignKey(ModelAuto, on_delete=models.CASCADE)
    description = models.TextField(max_length=250, verbose_name='Описание проблемы')
    date_service = models.DateField(verbose_name='Дата записи на сервис')

    class Meta:
        verbose_name_plural = 'Записи на сервис'

    def __str__(self):
        return self.user.username

