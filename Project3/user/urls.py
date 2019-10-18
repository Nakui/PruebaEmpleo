from django.urls import path
from user.views import UserRegister
from user.views import userListed, UserAPI
from . import views

app_name = 'user'

urlpatterns = [
    path('listed/', userListed, name='user_listed'),

    path('register/', UserRegister.as_view(), name='register'),
    path('api/', UserAPI.as_view(), name='api'),
]