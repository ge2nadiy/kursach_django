from django import forms
from django.contrib.auth.models import User
from django.forms import PasswordInput

from AutoHomeApp.models import Profile


class UserForm(forms.ModelForm):
    username = forms.CharField(max_length=40, required=True)
    password = forms.CharField(widget=PasswordInput())
    class Meta:
        model = User
        fields = ('username', 'password', 'first_name', 'last_name', 'email')


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('birth_date', 'phone')
