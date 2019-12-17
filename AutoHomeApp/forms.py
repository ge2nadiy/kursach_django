from django import forms
from django.contrib.auth.models import User
from django.forms import PasswordInput

from AutoHomeApp.models import Profile, Marka, Reserv


class UserForm(forms.ModelForm):
    email = forms.CharField(max_length=40, required=True)
    password = forms.CharField(widget=PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'password', 'first_name', 'last_name', 'email')


class UserFormForEdit(forms.ModelForm):
    email = forms.CharField(max_length=40, required=True)

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('birth_date', 'phone')


class AutoHomeFilterForm(forms.Form):
    marka = forms.ModelChoiceField(required=False, label='Марка', queryset=Marka.objects.distinct('marka'))
    min_price = forms.IntegerField(required=False, label='Цена: от')
    max_price = forms.IntegerField(required=False, label='Цена: до')
    min_year_of_issue = forms.IntegerField(required=False, label='Год выпуска: от')
    max_year_of_issue = forms.IntegerField(required=False, label='Год выпуска: до')


class AutoHomeRezervForm(forms.ModelForm):
    class Meta:
        model = Reserv
        exclude = ('user',)
