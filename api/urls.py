# api/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.ListUser.as_view(), name='User'),
    path('UserProfileInfo/', views.ListUserProfileInfo.as_view(), name='UserProfileInfo'),
]