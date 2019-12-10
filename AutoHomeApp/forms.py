from django import forms
from django.contrib.auth.models import User
from AutoHomeApp.models import Marka

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'username', 'password')

class MarkaForm(forms.ModelForm):
    class Meta:
        model = Marka
        fields = ('marka', 'description', 'logo')