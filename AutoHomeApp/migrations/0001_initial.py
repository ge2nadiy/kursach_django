# Generated by Django 3.0.3 on 2021-05-01 13:44

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='Marka',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marka', models.CharField(max_length=20, verbose_name='Марка')),
                ('description', models.TextField(verbose_name='Описание')),
                ('logo', models.ImageField(upload_to='marka_logo/')),
            ],
            options={
                'verbose_name': 'Марка',
                'verbose_name_plural': 'Марки',
            },
        ),
        migrations.CreateModel(
            name='ModelAuto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model', models.CharField(max_length=30, verbose_name='Модель')),
                ('body_type', models.CharField(max_length=20, verbose_name='Тип кузова')),
                ('power', models.IntegerField(default=0, verbose_name='Мощность,л.с.')),
                ('engine_volume', models.IntegerField(default=0, verbose_name='Объём двигателя,куб. см')),
                ('number_of_gears', models.IntegerField(default=0, verbose_name='Количество передач')),
                ('year_of_issue', models.IntegerField(default=0, verbose_name='Год выпуска')),
                ('price', models.IntegerField(default=0, verbose_name='Цена')),
                ('logo', models.ImageField(upload_to='model_logo/')),
                ('marka', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AutoHomeApp.Marka')),
            ],
            options={
                'verbose_name': 'Модель',
                'verbose_name_plural': 'Модели',
                'ordering': ['model'],
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('phone', models.CharField(max_length=30, verbose_name='Моб. номер')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name_plural': 'Данные пользователей',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='TestDrive',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_inquiry', models.DateField(null=True, verbose_name='Дата тест-драйва')),
                ('model', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AutoHomeApp.ModelAuto')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Тест-драйв',
                'ordering': ['user'],
            },
        ),
        migrations.CreateModel(
            name='SoldCars',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AutoHomeApp.ModelAuto')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Проданные авто',
            },
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model', models.CharField(max_length=20, verbose_name='Модель')),
                ('marka', models.CharField(max_length=20, verbose_name='Марка')),
                ('years', models.CharField(max_length=20, verbose_name='Год выпуска')),
                ('description', models.TextField(max_length=250, verbose_name='Описание проблемы')),
                ('date_service', models.DateField(verbose_name='Дата записи на сервис')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Записи на сервис',
            },
        ),
        migrations.CreateModel(
            name='Inquiry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_inquiry', models.DateField(blank=True, null=True)),
                ('model', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AutoHomeApp.ModelAuto')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Заявки',
                'ordering': ['user'],
            },
        ),
    ]
