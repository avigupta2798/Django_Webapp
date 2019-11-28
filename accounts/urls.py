# accounts/urls.py
from django.urls import path
from accounts import views as accounts_views

app_name = 'accounts'

urlpatterns = [
    path('userprofileinfo/', accounts_views.user_login),
    path('register/', accounts_views.register, name='register'),
    path('login/', accounts_views.user_login, name='login'),
]