from django.urls import path, include
from AutoHomeApp.views import *
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    #   path('auth/', include('djoser.urls')),
    #   path('auth/token', obtain_auth_token, name='token'),
    #   path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('user/<int:pk>', UserRetrieveUpdateView.as_view()),

    path('marka/', MarkasListView.as_view()),

    path('models/', ModelAutoListView.as_view()),
    path('models/<int:pk>', ModelAutoRetrieveView.as_view()),

    path('sold-car/', SoldCarListView.as_view()),
    path('sold-car/new/', SoldCarCreateView.as_view()),
    path('sold-car/<int:pk>', SoldCarDestroyView.as_view()),

    path('inquiry/', InquiryListView.as_view()),
    path('inquiry/new/', InquiryCreateView.as_view()),
    path('inquiry/<int:pk>', InquiryDestroyView.as_view()),

    path('test-drive/', TestDriveListView.as_view()),
    path('test-drive/new/', TestDriveCreateView.as_view()),
    path('test-drive/<int:pk>', TestDriveDestroyView.as_view()),

    path('service/', ServiceListView.as_view()),
    path('service/new/', ServiceCreateView.as_view()),
    path('service/<int:pk>', ServiceDestroyView.as_view()),
]
