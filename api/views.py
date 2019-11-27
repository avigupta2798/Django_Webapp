#api/views.py

from django.shortcuts import render
from rest_framework import generics

from accounts import models
from . import serializers

# Create your views here.

class ListUserProfileInfo(generics.ListCreateAPIView):
    queryset = models.UserProfileInfo.objects.all()
    serializer_class = serializers.UserProfileInfoSerializer

class ListUser(generics.ListCreateAPIView):
    queryset = models.User.objects.all()
    serializer_class = serializers.UserSerializer