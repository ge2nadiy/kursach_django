from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    birth_date = models.DateField(null=True, blank=True, verbose_name='Дата рождения')
    phone =models.CharField(max_length=30, verbose_name='Моб. номер')

    class Meta:
        verbose_name_plural = 'Данные пользователей'

    def __str__(self):
        return self.user.username


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


class Reserv(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='rezerv')
    marka = models.CharField(max_length=20, verbose_name='Марка')
    model = models.CharField(max_length=30, verbose_name='Модель')
    body_type = models.CharField(max_length=20, verbose_name='Тип кузова')
    power = models.IntegerField(default=0, verbose_name='Мощность,л.с.')
    engine_volume = models.IntegerField(default=0, verbose_name='Объём двигателя,куб. см')
    number_of_gears = models.IntegerField(default=0, verbose_name='Количество передач')
    year_of_issue = models.IntegerField(default=0, verbose_name='Год выпуска')
    price = models.IntegerField(default=0, verbose_name='Цена')
    logo = models.ImageField(upload_to='model_logo/', blank=False)

    class Meta:
        verbose_name_plural = 'Забронированные'
        ordering = ['user']

    def __str__(self):
        return self.user.username