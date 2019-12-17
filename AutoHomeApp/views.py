from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from AutoHomeApp.forms import UserForm, ProfileForm, UserFormForEdit
from django.contrib.auth.models import User

from django.contrib.auth import authenticate, login

from AutoHomeApp.models import ModelAuto, Marka, Reserv

from .forms import AutoHomeFilterForm, AutoHomeRezervForm


# Create your views here.

def home(request):
    return redirect(AutoHome_home)


def AutoHome_home(request):
    return render(request, 'AutoHome/home.html', {})


@login_required(login_url='../../AutoHome/sign-in/')
def AutoHome_account(request):
    user_form = UserFormForEdit(instance=request.user)
    profile_form = ProfileForm(instance=request.user.profile)

    if request.method == "POST":
        user_form = UserFormForEdit(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()

    return render(request, 'AutoHome/account.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })


def AutoHome_auto(request):
    autos = ModelAuto.objects.all()
    form = AutoHomeFilterForm(request.GET)
    if form.is_valid():
        if form.cleaned_data['marka']:
            # all_marka = Marka.objects.distinct('marka')
            autos = autos.filter(marka__exact=form.cleaned_data['marka'])

        if form.cleaned_data['min_price']:
            autos = autos.filter(price__gte=form.cleaned_data['min_price'])

        if form.cleaned_data['max_price']:
            autos = autos.filter(price__lte=form.cleaned_data['max_price'])

        if form.cleaned_data['min_year_of_issue']:
            autos = autos.filter(year_of_issue__gte=form.cleaned_data['min_year_of_issue'])

        if form.cleaned_data['max_year_of_issue']:
            autos = autos.filter(year_of_issue__lte=form.cleaned_data['max_year_of_issue'])

    return render(request, 'AutoHome/auto.html', {
        'autos': autos,
        # 'markas': all_marka,
        'form': form
    })


def AutoHome_all_rezerv_auto(request):
    autos = Reserv.objects.filter(user=request.user)
   # if request.method == 'POST':
   #     emp = Reserv.objects.get(id=auto_id)
   #     emp.delete()
   #     return redirect(AutoHome_all_rezerv_auto())
    return render(request, 'AutoHome/rezerv_avto.html', {
        'autos': autos,
    })


def AutoHome_delete(request, modelauto):
    if request.method == 'POST':
     emp = Reserv.objects.get(id=modelauto)
     emp.delete()
     return redirect(AutoHome_all_rezerv_auto)

    return redirect(AutoHome_all_rezerv_auto)

def AutoHome_auto_rezerv(request, modelauto):
    # modelauto = get_object_or_404(ModelAuto, pk)
    # auto = get_object_or_404(ModelAuto, pk)
    auto = ModelAuto.objects.get(id=modelauto)
    form = AutoHomeRezervForm(initial={
        'marka': auto.marka,
        'model': auto.model,
        'body_type': auto.body_type,
        'power': auto.power,
        'engine_volume': auto.engine_volume,
        'number_of_gears': auto.number_of_gears,
        'year_of_issue': auto.year_of_issue,
        'price': auto.price,
        'logo': auto.logo
    })
    #form = AutoHomeRezervForm(instance=ModelAuto.objects.get(id=modelauto))
    if request.method == 'POST':
        form = AutoHomeRezervForm(request.POST, request.FILES, initial={
        'marka': auto.marka,
        'model': auto.model,
        'body_type': auto.body_type,
        'power': auto.power,
        'engine_volume': auto.engine_volume,
        'number_of_gears': auto.number_of_gears,
        'year_of_issue': auto.year_of_issue,
        'price': auto.price,
        'logo': auto.logo
         })
        if form.is_valid():
            autos = form.save(commit=False)
            autos.user = request.user
            autos.save()
            return redirect(AutoHome_auto)
    return render(request, 'AutoHome/rezerv.html', {
        'form': form,
        'auto': auto
    })


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
                username=user_form.cleaned_data['username'],
                password=user_form.cleaned_data['password']
            ))

            return redirect(AutoHome_home)

    return render(request, 'AutoHome/sign_up.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })
