from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from AutoHomeApp.forms import UserForm, MarkaForm


# Create your views here.

def home(request):
    return redirect(AutoHome_home)


@login_required(login_url='AutoHome/sign-in/')
def AutoHome_home(request):
    return render(request, 'AutoHome/home.html', {})

def AutoHome_sign_up(request):
    user_form = UserForm()
    marka_form = MarkaForm()
    return render(request, 'AutoHome/sign_up.html', {
        'user_form': user_form,
        'marka_form': marka_form
    })
