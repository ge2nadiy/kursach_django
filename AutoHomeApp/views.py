from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from AutoHomeApp.forms import UserForm, ProfileForm
from django.contrib.auth.models import User

from django.contrib.auth import authenticate, login


# Create your views here.

def home(request):
    return redirect(AutoHome_home)


@login_required(login_url='AutoHome/sign-in/')
def AutoHome_home(request):
    return render(request, 'AutoHome/home.html', {})

def AutoHome_sign_up(request):
    user_form = UserForm()
    profile_form = ProfileForm()

    if request.method == "POST":
        user_form = UserForm(request.POST)
        profile_form = ProfileForm(request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            new_user = User.objects.create_user(**user_form.cleaned_data)
            new_profile = profile_form.save(commit=False)
            new_profile.user = new_user
            new_profile.save()

            login(request, authenticate(
                username = user_form.cleaned_data['username'],
                password = user_form.cleaned_data['password']
            ))

            return redirect(AutoHome_home)

    return render(request, 'AutoHome/sign_up.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })
