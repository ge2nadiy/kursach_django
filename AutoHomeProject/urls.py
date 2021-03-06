"""AutoHomeProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from AutoHomeApp import views

from django.contrib.auth import views as auth_views

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),

    path('AutoHome/sign-in/', auth_views.LoginView.as_view(template_name='AutoHome/sign_in.html'),
         name='AutoHome-sign-in'),

    path('AutoHome/sign-out/', auth_views.LogoutView.as_view(next_page='/'),
         name='AutoHome-sign-out'),

    path('AutoHome', views.AutoHome_home, name='AutoHome-home'),

    path('AutoHome/sign-up/', views.AutoHome_sign_up, name='AutoHome-sign-up'),

    path('AutoHome/account/', views.AutoHome_account, name='AutoHome-account'),

    path('AutoHome/auto/', views.AutoHome_auto, name='AutoHome-auto'),

    path('AutoHome/bron/<int:modelauto>/', views.AutoHome_auto_rezerv, name='AutoHome-auto-rezerv'),

    path('AutoHome/auto/rezerv/', views.AutoHome_all_rezerv_auto, name='AutoHome-all-rezerv-auto'),

    path('AutoHome/auto/rezerv/<int:modelauto>/', views.AutoHome_delete, name='AutoHome-delete'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
